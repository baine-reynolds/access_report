import requests
import getpass
import json

url = input("Please enter the Source instance's Base URL (i.e. https://bitbucket.mycompany.com (Server)):\n")
admin_user = input("Please enter the Admin username for your source environment:\n")
admin_password = getpass.getpass("Please enter the Admin password for your source environment:\n")

session = requests.Session()
session.auth = (admin_user, admin_password)

users = []
projects = []
repos = []

def get_global_group_details(start=None, limit=None):
    while True:
        params = {'start': start, 'limit': limit}
        endpoint = url + "/rest/api/1.0/admin/permissions/groups"
        r = session.get(endpoint, params=params)
        r_data = r.json()
        for line in r_data['values']:
            print(line)
        if r_data['isLastPage'] == True:
            return
        start = r_data['nextPageStart']

def get_global_user_details(start=None, limit=None):
    while True:
        params = {'start': start, 'limit': limit}
        endpoint = url + "/rest/api/1.0/admin/permissions/users"
        r = session.get(endpoint, params=params)
        r_data = r.json()
        for line in r_data['values']:
            print(line)
        if r_data['isLastPage'] == True:
            return
        start = r_data['nextPageStart']

def get_user_groups(user, start=None, limit=None):
    while True:
        params = {'start': start, 'limit': limit, 'context': user}
        endpoint = url + "/rest/api/1.0/admin/users/more-members"
        r = session.get(endpoint, params=params)
        r_data = r.json()
        for line in r_data['values']:
            print(line)
        if r_data['isLastPage'] == True:
            return
        start = r_data['nextPageStart']

def get_proj_group_details(project, start=None, limit=None):
    while True:
        params = {'start': start, 'limit': limit}
        endpoint = url + "/rest/api/1.0/projects/" + project + "/permissions/groups"
        r = session.get(endpoint, params=params)
        r_data = r.json()
        for line in r_data['values']:
            print(line)
        if r_data['isLastPage'] == True:
            return
        start = r_data['nextPageStart']

def get_proj_user_details(project, start=None, limit=None):
    while True:
        params = {'start': start, 'limit': limit}
        endpoint = url + "/rest/api/1.0/projects/" + project + "/permissions/users"
        r = session.get(endpoint, params=params)
        r_data = r.json()
        for line in r_data['values']:
            print(line)
        if r_data['isLastPage'] == True:
            return
        start = r_data['nextPageStart']

def get_repo_group_details(proj, repo, start=None, limit=None):
    while True:
        params = {'start': start, 'limit': limit}
        endpoint = url + "/rest/api/1.0/projects/" + proj + "/repos/" + repo + "/permissions/groups"
        r = session.get(endpoint, params=params)
        r_data = r.json()
        for line in r_data['values']:
            print(line)
        if r_data['isLastPage'] == True:
            return
        start = r_data['nextPageStart']

def get_repo_user_detais(proj, repo, start=None, limit=None):
    while True:
        params = {'start': start, 'limit': limit}
        endpoint = url + "/rest/api/1.0/projects/" + proj + "/repos/" + repo + "/permissions/users"
        r = session.get(endpoint, params=params)
        r_data = r.json()
        for line in r_data['values']:
            print(line)
        if r_data['isLastPage'] == True:
            return
        start = r_data['nextPageStart']

def get_info():
    # Global details
    print("\n=====GLOBAL=====")
    print("Global Groups:")
    get_global_group_details()
    print("Global Users:")
    get_global_user_details()
    # user details
    print("\n=====USER=====")
    for user in users:
        print(f"Groups found for user: \"{user}\"")
        get_user_groups(user)
    # project details
    print("\n=====PROJECT=====")
    for project in projects:
        print(f"==={project}===")
        print(f"Group data for project {project}:")
        get_proj_group_details(project.upper())
        print(f"User data for project {project}:")
        get_proj_user_details(project.upper())
    # repo details
    print("\n=====REPOSITORY=====")
    for pair in repos:
        proj = pair.split(':')[0].upper()
        repo = pair.split(':')[1].lower()
        print(f"==={proj}==={repo}===")
        print(f"Group data for repo {repo}:")
        get_repo_group_details(proj, repo)
        print(f"User data for repo {repo}:")
        get_repo_user_detais(proj, repo)

if __name__ == '__main__':
    get_info()