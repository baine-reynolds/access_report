## Dependency
* Python 3
* [Requests Package](http://docs.python-requests.org/en/master/)

`
pip3 install requests --user
`

## Usage
Option 1.
1. Update lines 12-14 with the string values of the resources you would like to check (see below for examples).
2. Run the script. This will prompt you for your environment url (i.e. https://bitbucket.example.com) and an admin username/password.
3. Collect the Output and provide it for review

Option 2.
1. Update lines 12-14 with the string values of the resources you would like to check (see below for examples). (Same as option 1)
2. Update lines 5-7 with the string values of your URL, username, and password so that the script does not need to prompt for these values
3. Collect the Output and provide it for review. (same as option 1)

## Running the Script
```python
python3 /path/to/run_report.py
```

## Examples
For lines 12-14:
```python
users = ["username1", "username2"]  # ["admin", "john_doe"]
projects = ["PROJECT_KEY_1", "PROJECT_KEY_2"]  # ["MAIN", "CORS"]
repos = ["PROJECT_KEY1:repo_slug_1_of_project1", "PROJECT_KEY1:repo_slug_2_of_project1", "PROJECT_KEY2:repo_slug_1_of_project2"]  # ["MAIN:primary", "CORS:test"]
```

For lines 5-7: (optional)
```python
url = "https://bitbucket.example.com"
admin_user = "admin"
admin_password = "password"
```