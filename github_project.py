import config
import requests
import json

#-------------

def connect_github(user):
   
    token = config.gh_api_key
    gh_session = requests.Session()
    gh_session.auth = (user, token)
    return gh_session

#---------------

def get_repos(user):
   
    repos_url = 'https://api.github.com/user/repos'
    gh_session = connect_github(user)
    repos = json.loads(gh_session.get(repos_url).text)
    repo_language = []    
    for repo in repos:
        json_format = json.dumps(repo,indent=4)
        repo_language.append(repo['language'])
    return repo_language

#a = get_repos('repoZtrees')
#print(a)

#-----------

def get_fav_language(user_name):

    languages = get_repos(user_name)
    counter = 0
    num = languages[0]   

    for i in languages:
        prog_languages = languages.count(i)
        if(prog_languages>counter):
            counter = prog_languages
            pl = i
    return pl 
        
#a = get_fav_language('RepoZTrees')
#print(a)

#---------

def recommend_project(user):
    project_name = [] 
    search_language = get_fav_language(user)
    sort_by = 'updated'
    repos_url = 'https://api.github.com/search/repositories?q=language:'+search_language+'&sort='+sort_by+'&order=desc'
    gh_session = connect_github(user)
    repos = json.loads(gh_session.get(repos_url).text)
     
    for project in repos['items']:
        json_format = json.dumps(project,indent=4)
        project_name.append(project['full_name'])
    return project_name

rec = recommend_project('RepoZTrees')
print(rec)
