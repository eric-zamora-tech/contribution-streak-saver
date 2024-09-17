from githubgraphql import get_commit_contributions_count
from datetime import date
from git import Repo

remote_repo_url = "git@github.com:eric-zamora-tech/eric-zamora-tech.git"

update_file = "README.md"

start = str(date.today()) + "T00:00:00Z"
end = str(date.today()) + "T23:59:59Z"

GH_PERSONAL_ACCESS_TOKEN = os.getenv('GH_PERSONAL_ACCESS_TOKEN')
headers = {"Authorization": f"Bearer {GH_PERSONAL_ACCESS_TOKEN}"}
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
     """ % (start_date, end_date)

request = requests.post('https://api.github.com/graphql', json={'query': query},headers=headers)
if request.status_code == 200:
     return request.json()["data"]["user"]["contributionsCollection"]["commitContributionsByRepository"]
else:
     raise Exception("Query fialed to run by returning code of {}. {}".format(request.status_code, query))

result = get_commit_contributions(start, end)
print(result)
if(len(result) < 1):
    print("We need to push a commit...")
    try:
         repo = Repo.clone_from(remote_repo_url, "/home/eric-zamora/Development/eric-zamora-tech")
    except:
         repo = Repo("/home/eric-zamora/Development/eric-zamora-tech")
         print(Exception)
    print("Repo is cloned...")

    with open(f"/home/eric-zamora/Development/eric-zamora-tech/{update_file}", "a") as f:
        f.write("## Uh oh, I forgot to commit :/")
    print("Updated file")

    repo.index.add([f"/home/eric-zamora/Development/eric-zamora-tech/{update_file}"])
    print("File has been added to staging area")
    
    diffs = repo.index.diff(None)
    for d in diffs:
            print(d.a_path)

    tree = repo.head.commit.tree
    files_and_dirs = [(entry, entry.name, entry.type) for entry in tree]
    print(files_and_dirs)

    repo.index.commit("Test commit message")
    print("Commit has been submitted")
    repo.remotes.origin.push()