import json
import os
import re

files = [x for x in os.listdir(f'../snapshot_20230727') if re.search('.+\.json$', x)]
for file in files:
    with open(f"../snapshot_20230727/{file}", 'r') as json_data:
        data = json.load(json_data)
        print(list(data["Sources"][0].keys()))
