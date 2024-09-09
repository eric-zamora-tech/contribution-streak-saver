from ghgraphql import get_commit_contributions
from datetime import date
from git import Repo

remote_repo_url = "git@github.com:eric-zamora-tech/eric-zamora-tech.git"

update_file = "README.md"

start = str(date.today()) + "T00:00:00Z"
end = str(date.today()) + "T23:59:59Z"

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