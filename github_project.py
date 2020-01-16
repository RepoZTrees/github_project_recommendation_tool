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
        prog_languages = languages.count(i)
        if(prog_languages>counter):
            counter = prog_languages
            pl = i
    #print('winner is:',pl)
    return pl 
        
#a = get_fav_language('RepoZTrees')
#print(a)

def recommend_project(user, order_by='update'):
    project_name = []
    search_language = get_fav_language(user)
    sort_by = 'updated'
    token = config.gh_api_key 

    #r = 'https://api.github.com/search/repositories?q=language:'+search_language+'&sort=stars&order=desc'
    #r = 'https://api.github.com/search/repositories?q=language:'+search_language+'&sort=updated&order=desc'
    r = 'https://api.github.com/search/repositories?q=language:'+search_language+'&sort='+sort_by+'&order=desc'
    gh_session = requests.Session()
    gh_session.auth = (user, token)
    repos = json.loads(gh_session.get(r).text)
    
    for project in repos['items']:
        json_format = json.dumps(project,indent=4)
        project_name.append(project['full_name'])
    return project_name
    #print(type(project_name))

rec = recommend_project('RepoZTrees')
print(rec)

#------

#def sort_query():
   # by update, by stars, help wanted
    
    

#-------
