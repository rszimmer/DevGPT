# "score": 0.(5|6|7|8|9)
import json
import os
import re
import random
import math

output_path = "./score_five_literature.json"
result = []

with open(f"../topic_extraction_results_literatur1.json", 'r') as json_data:
    data = json.load(json_data)
    for entry in data:
        for prompt in entry:
            if prompt["score"] >= 0.5:
                result.append(prompt)
with open(output_path, "w", encoding="utf-8") as output_file:
    json.dump(result, output_file, indent=2)