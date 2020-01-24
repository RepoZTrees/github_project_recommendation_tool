import config
import requests
import json
import argparse

#---------

def connect_github(user):
   
    token = config.gh_api_key
    gh_session = requests.Session()
    gh_session.auth = (user, token)
    return gh_session

#---------

def get_repos(user):
   
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

    languages = get_repos(user_name)
    counter = 0
    num = languages[0]   

    for i in languages:
        prog_languages = languages.count(i)
        if(prog_languages>counter):
            counter = prog_languages
            pl = i
    print('Your language of choice is:',pl)
    return pl

#---------

def get_popular_projects(user):
    search_language = get_fav_language(user)
    sort_by = 'updated'
    repos_url = 'https://api.github.com/search/repositories?q=language:'+search_language+'&sort='+sort_by+'&order=desc'
    gh_session = connect_github(user)
    repos = json.loads(gh_session.get(repos_url).text)
    return repos

def recommend_project(repos):
    for project in repos['items']:
        json_format = json.dumps(project,indent=4)
        project_name.append(project['full_name'])
    project_names = []
    
    for i in project_name:
        project_names.append(i)
    return project_names

#---------

def arg_parse():
    
    parser = argparse.ArgumentParser()
    parser.add_argument("-u","--user", help="Enter your GitHub username.")
    args = parser.parse_args()
    return args.user

if __name__ == "__main__":
    user_name = arg_parse()
    rec_projects =  recommend_project_by_language_and_sort_by_updated(user_name)
    print('\n')
    print("Repositories Committed Recently")
    print('\n')
    for i in rec_projects:    
        print("GitHub Username/Repository Name: {} \n".format(i))



def sample():
    # Sample API
    session = gh_session(user)
    gh_query_url = make_query(site = "github", language = "python", date_from = dt, sort_by = "updated", ...) # Test this
    response = session.get(gh_query_url)
    repos = recommend(response) # Test this

    
