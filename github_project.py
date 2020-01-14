import config
import requests
import json

username = ''
token = config.gh_api_key

repos_url = 'https://api.github.com/user/repos'

gh_session = requests.Session()
gh_session.auth = (username, token)

repos = json.loads(gh_session.get(repos_url).text)

for repo in repos:
    json_format = json.dumps(repo,indent=4)
    repo_name = repo['name']
    repo_programming_language_name = repo['language']
    print(repo_name,repo_programming_language_name)
    



