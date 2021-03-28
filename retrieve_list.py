import os
import requests
import json


api_key = os.environ['API_KEY']
api_path = 'https://codeplexarchive-search.search.windows.net/indexes/codeplexarchive-index/docs'
top = 10000000

params = {
    'api-version': '2016-09-01',
    'api-key': api_key,
    '$top': top,
    'highlight': 'Title',
    'search': '*'
}
next_link = ''
projects = []

while True:
    try:
        if not next_link:
            response = requests.get(api_path, params=params)
        else:
            response = requests.get(next_link)
        
        response_json = response.json()

        results = response_json['value']
        for project in results:
            print(project['ProjectName'])
            projects.append(project)

        next_link = response_json['@odata.nextLink']

    except Exception as e:
        print(e, "- I guess we're done for now.")
        with open('projects.json', 'w') as projects_file:
            json.dump(projects, projects_file)
        break