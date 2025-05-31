import json
import os
import re
import random
import math

output_path = "./conversarion_media_literature.json"
randomSampleList = []
documentation = 0
issue = 0
configuration = 0
test = 0
refactoring = 0
feature = 0
other = 0

    
with open(f"../topic_extraction_results_literatur1.json", 'r') as json_data:
    data = json.load(json_data)
    for entry in data:
        documentation = 0
        issue = 0
        configuration = 0
        test = 0
        refactoring = 0
        feature = 0
        other = 0
        
        for prompt in entry:
            if prompt["topic"] == "Documentation":
                documentation += prompt["score"]
            elif prompt["topic"] == "Issue":
                issue += prompt["score"]
            elif prompt["topic"] == "Configuration":
                configuration += prompt["score"]
            elif prompt["topic"] == "Test":
                test += prompt["score"]
            elif prompt["topic"] == "Refactoring":
                refactoring += prompt["score"]
            elif prompt["topic"] == "New Feature":
                feature += prompt["score"]
            elif prompt["topic"] == "Other":
                other += prompt["score"]
                
        count = len(entry) if len(entry) != 0 else 1
        documentationMedia = documentation / count
        issueMedia = issue /  count
        configurationMedia = configuration / count
        refactoringMedia = refactoring / count
        testMedia = test / count
        featureMedia = feature / count
        otherMedia = other / count
        max_media = max([documentationMedia, issueMedia, configurationMedia, testMedia, refactoringMedia, featureMedia, otherMedia])
        if documentationMedia == max_media:
            entry.append({"topicMedia": max_media,"mainTopic": "Documentation"})
        elif issueMedia == max_media:
            entry.append({"topicMedia": max_media,"mainTopic": "Issue"})
        elif configurationMedia == max_media:
            entry.append({"topicMedia": max_media,"mainTopic": "Configuration"})
        elif testMedia == max_media:
            entry.append({"topicMedia": max_media,"mainTopic": "Test"})
        elif refactoringMedia == max_media:
            entry.append({"topicMedia": max_media,"mainTopic": "Refactoring"})
        elif featureMedia == max_media:
            entry.append({"topicMedia": max_media,"mainTopic": "New Feature"})
        elif otherMedia == max_media:
            entry.append({"topicMedia": max_media,"mainTopic": "Other"})

with open(output_path, "w", encoding="utf-8") as output_file:
    json.dump(data, output_file, indent=2)