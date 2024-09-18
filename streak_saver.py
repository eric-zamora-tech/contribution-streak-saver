#####################################
#####       Module Imports      #####
#####################################

from github import Github, Auth
from datetime import date
from openai import OpenAI
from git import Repo
import requests
import dotenv
import shutil
import time
import os

######################################
#####       .ENV Variables       #####
######################################

dotenv.load_dotenv()

OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')
GITHUB_AUTH_TOKEN = os.getenv('GITHUB_PERSONAL_ACCESS_TOKEN')
GITHUB_USERNAME = os.getenv('GITHUB_USERNAME')

#############################
#####       Main        #####
#############################

##### GET TODAY'S CONTRIBUTION COUNT #####
FROM_DATE = f'{date.today()}T00:00:00Z'
TO_DATE = f'{date.today()}T23:59:59Z'

headers = {'Authorization': f'Bearer {GITHUB_AUTH_TOKEN}'}
query = """
    {
        user(login: "%s") {
            contributionsCollection(from: "%s", to: "%s") {
                contributionCalendar {
                    totalContributions
                }
            }
        }
    }
""" % (GITHUB_USERNAME, FROM_DATE, TO_DATE)

try:
    print('Checking total contributions for today...')
    time.sleep(2)
    contribution_count = requests.post('https://api.github.com/graphql', json={'query': query}, headers=headers).json()['data']['user']['contributionsCollection']['contributionCalendar']['totalContributions']
except:
    raise Exception('ERROR: GitHub GraphQL query failed to run.')

##### EXIT IF THERE IS AT LEAST ONE CONTRIBUTION FOR TODAY #####
if contribution_count >= 1:
    print(f'Great job, you have {contribution_count} new contribution(s)! No further action needed.')
    time.sleep(2)
    exit(0)

##### CONNECT TO GITHUB API v3 #####
print('You have no contributions for today. Initializing "SHAME PROTOCOL"...')
time.sleep(2)

auth = Auth.Token(GITHUB_AUTH_TOKEN)
g = Github(auth=auth)

##### CHECK IF HALL OF SHAME REPO EXISTS IN GITHUB ACCOUNT  #####
print('Checking if "Hall of Shame" repo exists in your account...', end='')
time.sleep(2)

shame_repo_name = 'hall-of-shame'

for repo in g.get_user().get_repos():
    if repo.name == shame_repo_name:
        print('EXISTS')
        shame_repo_origin = repo.ssh_url
        shame_clone_url = shame_repo_origin
        time.sleep(2)
        break
else:
    print('DOES NOT EXIST')
    shame_clone_url = 'git@github.com:eric-zamora-tech/hall-of-shame.git'
    time.sleep(2)

    print('Creating remote "Hall of Shame" repo...', end='')
    time.sleep(2)

    headers = {
        'Authorization': f'token {GITHUB_AUTH_TOKEN}',
        'Accept': 'application/vnd.github.v3+json'
    }
    data = {
        'name': shame_repo_name,
        'private': False,
        'auto_init': False,
    }

    response = requests.post('https://api.github.com/user/repos', json=data, headers=headers)

    if response.status_code == 201:
        print('SUCCESS')
        shame_repo_origin = response.json()['ssh_url']
    else:
        print(f'FAILED: {response.json()}')
time.sleep(2)

##### CLONE REPO TO EDIT #####
local_repo_dir = f'./{shame_repo_name}'
if os.path.exists(local_repo_dir):
    print('Repo already exists in target directory. Removing files...', end='')
    time.sleep(2)
    shutil.rmtree(local_repo_dir)
    print("SUCCESS")

print('Cloning Hall of Shame repo...', end='')
time.sleep(2)
repo = Repo.clone_from(shame_clone_url, local_repo_dir)
print('SUCCESS')
time.sleep(2)

##### APPEND CARD TO REPO #####
print('Writing new Shame Card to project...', end='')
time.sleep(2)
file_path = f'{local_repo_dir}/src/App.js'
with open(file_path, 'r') as f:
    file_contents = f.readlines()

insert_index = -1
for i, line in enumerate(file_contents):
    if '</div>' in line:
        card_index = i
        break

if card_index != -1:
    today = date.today()
    today_formatted = today.strftime('%B %d, %Y').replace(' 0', ' ')
    client = OpenAI(api_key=OPENAI_API_KEY)

    shame_card_content = client.chat.completions.create(
        model='gpt-3.5-turbo',
        messages=[
            {'role': 'system', 'content': 'You are a helpful assistant.'},
            {
                'role': 'user',
                'content': 'Finish the sentence "The reason why I could not keep up my GitHub contribution streak is because..." Make your response funny, witty, and embarassing. Only respond with the second part of the sentence. Include the ellipses. Do not repeat your answers.'
            }
        ]
    ).choices[0].message.content.replace('"', "'")

    new_card_jsx = f'<ShameCard title="{today_formatted}" content="{shame_card_content}" />\n'
    file_contents.insert(card_index, new_card_jsx)

with open(file_path, 'w') as f:
    f.writelines(file_contents)

print('SUCCESS')
time.sleep(2)

##### COMMIT AND PUSH CHANGES #####
print('Staging, committing, and pushing changes...', end='')
time.sleep(2)
try:
    origin = repo.remote(name='origin')
    origin.set_url(shame_repo_origin)
except ValueError:
    origin = repo.create_remote('origin', shame_repo_origin)

repo.git.add('--all')
repo.index.commit('Added Shame Card')
repo.remotes.origin.push()
print('SUCCESS')

shutil.rmtree(local_repo_dir)

g.close()