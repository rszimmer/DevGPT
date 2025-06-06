import json
import os
import re
import random
import math

output_path = "./topic_comparison.json"
results = []
sommerville = []
chavan = []
champa = []

with open(f"../topic_extraction_results.json", 'r') as json_data:
    sommerville = json.load(json_data)
with open(f"../topic_extraction_results_literatur1.json", 'r') as json_data:
    chavan = json.load(json_data)
with open(f"../topic_extraction_results_literatur2.json", 'r') as json_data:
    champa = json.load(json_data)
number_conversations =  len(sommerville)

for i in range(0, number_conversations-1):
    conversation = []
    number_prompts = len(sommerville[i])
    if number_prompts > 0:
        for j in range(0, number_prompts - 1):
            conversation.append({
                "prompt": sommerville[i][j]["prompt"],
                "topic": [sommerville[i][j]["topic"], chavan[i][j]["topic"], champa[i][j]["topic"]],
                "score": [sommerville[i][j]["score"], chavan[i][j]["score"], champa[i][j]["score"]]
            })
        results.append(conversation)

with open(output_path, "w", encoding="utf-8") as output_file:
    json.dump(results, output_file, indent=2)
