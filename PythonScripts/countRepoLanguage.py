import json
import os
import re

repoLanguages = {"null": 0}

folders = [x for x in os.listdir('../.') if re.match('^snapshot_.+', x)]

for folder in folders:
    files = [x for x in os.listdir(f'../{folder}') if re.search('.+\.json$', x)]
    for file in files:
        with open(f"../{folder}/{file}", 'r') as json_data:
            data = json.load(json_data)
            itemsArray = data["Sources"]
            for item in itemsArray:
                if not "RepoLanguage" in item:
                    repoLanguages["null"]+=1
                else:
                    if item["RepoLanguage"] in repoLanguages:
                        repoLanguages[item["RepoLanguage"]]+=1
                    else:
                        repoLanguages[item["RepoLanguage"]] = 1
print(repoLanguages)