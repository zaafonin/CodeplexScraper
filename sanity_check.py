import json


with open('projects.json', 'r') as projects_file:
    projects = json.load(projects_file)

print(len(projects))
print(projects[-10:-1])