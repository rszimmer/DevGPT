import json
import os
import re

sourceCounts = {'hn': [], 'pr': [], 'issue': [], 'discussion': [], 'commit': [], 'file': []}
regex = re.compile('pr|issue|hn|discussion|commit|file')

folders = [x for x in os.listdir('../.') if re.match('^snapshot_.+', x)]

for folder in folders:
    files = [x for x in os.listdir(f'../{folder}') if re.search('.+\.json$', x)]
    for file in files:
        with open(f"../{folder}/{file}", 'r') as json_data:
            data = json.load(json_data)
            result = regex.search(file)
            sourceCounts[result.group(0)] = sourceCounts[result.group(0)] + [len(data["Sources"])]
print(sourceCounts)