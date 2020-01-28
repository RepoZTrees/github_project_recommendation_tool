import config
import requests
import json
import argparse
from urllib.parse import urlparse
from urllib.parse import urljoin

#---------

def connect_github(user):
   
    token = config.gh_api_key
    gh_session = requests.Session()
    gh_session.auth = (user, token)
    return gh_session

#---------

def get_languages(user):
   
    repos_url = 'https://api.github.com/user/repos'
    gh_session = connect_github(user)
    repos = json.loads(gh_session.get(repos_url).text)
    repo_language = []    
    for repo in repos:
        json_format = json.dumps(repo,indent=4)
        repo_language.append(repo['language'])
    return repo_language

#---------

def get_fav_language(user_name):

    languages = get_languages(user_name)
    counter = 0
    num = languages[0]   

    for i in languages:
        prog_languages = languages.count(i)
        if(prog_languages>counter):
            counter = prog_languages
            pl = i
    print('Your language of choice is:',pl)
    return pl

#----------

def query_params(l='python', sort_key='updated', order='desc'):
    return dict(q=f'language:{l}',sort = sort_key, order=order)

def get_repos(user):
    
    search_language = get_fav_language(user)
    url = 'https://api.github.com/search/repositories'    
    get_repos_url = requests.get(url,params=query_params(l=search_language))
    repos_url = get_repos_url
    return repos_url

# a = url_construction('repoZTrees')
# print(a)

#--------

def fetch_repos(user):
    
    repos_url = get_repos(user)
    repos = repos_url.json()
    return repos


def recommend_project(user):
    
    project_name = []
    repos = fetch_repos(user)
    for project in repos['items']:
        json_format = json.dumps(project,indent=4)
        project_name.append(project['full_name'])

    project_names = [] 
    for i in project_name:
        project_names.append(i)
    return project_names

#a = recommend_project('repoZTrees')
#print(a)

#---------

def arg_parse():
    
    parser = argparse.ArgumentParser()
    parser.add_argument("-u","--user", help="Enter your GitHub username.")
    args = parser.parse_args()
    return args.user

if __name__ == "__main__":
    user_name = arg_parse()
    rec_projects = recommend_project(user_name)
    print('\n')
    print("Repositories Committed Recently")
    print('\n')
    for i in rec_projects:    
        print("GitHub Username/Repository Name: {} \n".format(i))
