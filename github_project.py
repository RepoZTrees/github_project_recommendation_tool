import config
import requests
import json

#repos_url = 'https://api.github.com/user/repos'

def get_repos(user):
    
    repo_language = []
    username = user
    token = config.gh_api_key
    repos_url = 'https://api.github.com/user/repos'
    gh_session = requests.Session()
    gh_session.auth = (username, token)
    repos = json.loads(gh_session.get(repos_url).text)
    for repo in repos:
        json_format = json.dumps(repo,indent=4)
        repo_language.append(repo['language'])
    return repo_language

#a = get_repos('repoZtrees')
#print(a)

#------

def get_fav_language(user_name):

    languages = get_repos(user_name)
    #print ("Hi", languages)
    counter = 0
    num = languages[0]   
   
    for i in languages:
        curr_frequency = languages.count(i)
        if(curr_frequency> counter):
            counter = curr_frequency
            num = i
    return num
        
a = get_fav_language('RepoZTrees')
print(a)
