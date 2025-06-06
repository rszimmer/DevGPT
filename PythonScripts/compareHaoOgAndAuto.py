import json
import os
import re
import pandas as pd

output_path = "./hao_comparison.json"
output_path_equals = "./hao_comparison_equals.json"
output_path_different = "./hao_comparison_different.json"
results = []
og = []
auto = []
equals = []
different =[]

excel_file = pd.ExcelFile("../final_rq1_data.xlsx")
data = excel_file.parse()

for prompt in data["prompt"]:
    og.append({"prompt": prompt})
for index, category in enumerate(data["Category"]):
    og[index]["topic"] = category

with open(f"../hao_topics_zero_shot_classification.json", 'r') as json_data:
    auto = json.load(json_data)

og = og[0:len(auto)]

for index, item in enumerate(og):
    results.append({
        "prompt": item["prompt"],
        "manual":item["topic"],
        "zeroshot":auto[index]["topic"],
    })

for item in results:
    if(item["manual"] == item["zeroshot"]):
        equals.append(item)
    else:
        different.append(item)

with open(output_path, "w", encoding="utf-8") as output_file:
    json.dump(results, output_file, indent=2)
with open(output_path_equals, "w", encoding="utf-8") as output_file:
    json.dump(equals, output_file, indent=2)
with open(output_path_different, "w", encoding="utf-8") as output_file:
    json.dump(different, output_file, indent=2)
