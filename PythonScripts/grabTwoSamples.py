import json
import os
import re
import random
import math

output_path = "./trying_random.json"
randomSampleList = []

folders = [x for x in os.listdir('../.') if re.match('^snapshot_.+', x)]

for folder in folders:
    files = [x for x in os.listdir(f'../{folder}') if re.search('.+\.json$', x)]
    for file in files:
        with open(f"../{folder}/{file}", 'r') as json_data:
            data = json.load(json_data)
            itemsArray = data["Sources"]
            randomSampleList.append(itemsArray[math.trunc(random.uniform(0, len(itemsArray)))])
            randomSampleList.append(itemsArray[math.trunc(random.uniform(0, len(itemsArray)))])

with open(output_path, "w", encoding="utf-8") as output_file:

    json.dump(randomSampleList, output_file, indent=2)
            