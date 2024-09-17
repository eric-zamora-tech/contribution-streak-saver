from github import Github, Auth
from datetime import date
from git import Repo
import requests
import dotenv
import shutil
import os

dotenv.load_dotenv()

##### GET TODAY'S CONTRIBUTION COUNT #####
AUTH_TOKEN = os.getenv('GITHUB_PERSONAL_ACCESS_TOKEN')
FROM_DATE = f'{date.today()}T00:00:00Z'
TO_DATE = f'{date.today()}T23:59:59Z'

headers = {'Authorization': f'Bearer {AUTH_TOKEN}'}
query = """
    {
        user(login: "eric-zamora-tech") {
            contributionsCollection(from: "%s", to: "%s") {
                commitContributionsByRepository {
                    repository {
                        name
                    }
                    contributions(first: 100) {
                        nodes {
                            occurredAt
                            commitCount
                        }
                    }
                }
            }
        }
    }
""" % (FROM_DATE, TO_DATE)

try:
    request = requests.post('https://api.github.com/graphql', json={'query': query}, headers=headers).json()['data']['user']['contributionsCollection']['commitContributionsByRepository']
except:
    raise Exception('Query failed to run.')

##### EXIT IF THERE IS AT LEAST ONE CONTRIBUTION FOR TODAY #####
if len(request) >= 1:
    print("Great job, your streak is looking good!")
    exit(0)

##### CONNECT TO GITHUB API v3 #####
print("Uh oh! You did not contribute to your GitHub account today!")
print("Initializing Shame Protocol...")

auth = Auth.Token(AUTH_TOKEN)
g = Github(auth=auth)

##### CHECK IF HALL OF SHAME REPO EXISTS IN GITHUB ACCOUNT  #####
print("Checking if Hall of Shame repo already exists in your account...", end="")
for repo in g.get_user().get_repos():
    if repo.name == "hall-of-shame":
        print("EXISTS")
        remote_url = f"git@github.com:{repo.full_name}.git"
        break
else:
    print("DOES NOT EXIST")
    print("Cloning from remote url...")
    remote_url = "git@github.com:eric-zamora-tech/hall-of-shame.git"

##### CLONE REPO TO EDIT #####
local_repo_dir = "../hall-of-shame"
if os.path.exists(local_repo_dir):
    print("Repo has already been cloned...")
    print("Removing existing folder...")
    shutil.rmtree(local_repo_dir)

print("Cloning Hall of Shame repo...")
repo = Repo.clone_from(remote_url, local_repo_dir)

##### APPEND CARD TO REPO #####
file_path = f'{local_repo_dir}/src/App.js'
with open(file_path, 'r') as f:
    file_contents = f.readlines()

insert_index = -1
for i, line in enumerate(file_contents):
    if '</div>' in line:
        card_index = i
        break

if card_index != -1:
    new_card_jsx = '<ShameCard title="Example" content="Lorem ipsum" />\n'
    file_contents.insert(card_index, new_card_jsx)

with open(file_path, 'w') as f:
    f.writelines(file_contents)

print("Added new Shame Card...")

##### COMMIT AND PUSH CHANGES #####
print("Staging, committing, and pushing changes...")
repo.git.add('--all')
repo.index.commit("Added Shame Card")
repo.remotes.origin.push()
print("Changes have been pushed. Complete!")

g.close()