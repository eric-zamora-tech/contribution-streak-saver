from dotenv import load_dotenv
import requests
import os

# Load environment variables
load_dotenv()

def get_commit_contributions_count(start_date, end_date):
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
