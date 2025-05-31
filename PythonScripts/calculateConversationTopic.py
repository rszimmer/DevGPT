import json
import os
import re
import random
import math

output_path = "./conversarion_media.json"
randomSampleList = []
testing = 0
requirements = 0
project = 0
coding = 0
maintenance = 0
    
with open(f"../topic_extraction_results.json", 'r') as json_data:
    data = json.load(json_data)
    for entry in data:
        testing = 0
        requirements = 0
        project = 0
        coding = 0
        maintenance = 0
        for prompt in entry:
            if prompt["topic"] == "Testing":
                testing += prompt["score"]
                
            elif prompt["topic"] == "Requirements":
                requirements += prompt["score"]
                
            elif prompt["topic"] == "Project":
                project += prompt["score"]
                
            elif prompt["topic"] == "Coding":
                coding += prompt["score"]
                
            elif prompt["topic"] == "Maintenance":
                maintenance += prompt["score"]
                                
        count = len(entry) if len(entry) != 0 else 1
        testingMedia = testing / count
        requirementsMedia = requirements / count
        projectMedia = project / count 
        codingMedia = coding / count
        maintenanceMedia = maintenance / count
        # print(count)
        # print([testing, requirements, project, coding, maintenance])
        # print([testingMedia, requirementsMedia, projectMedia, codingMedia, maintenanceMedia])
        max_media = max([testingMedia, requirementsMedia, projectMedia, codingMedia, maintenanceMedia])
        if testingMedia == max_media:
            entry.append({"topicMedia": max_media,"mainTopic": "Testing"})
        elif requirementsMedia == max_media:
            entry.append({"topicMedia": max_media,"mainTopic": "Requirements"})
        elif projectMedia == max_media:
            entry.append({"topicMedia": max_media,"mainTopic": "Project"})
        elif codingMedia == max_media:
            entry.append({"topicMedia": max_media,"mainTopic": "Coding"})
        elif maintenanceMedia == max_media:
            entry.append({"topicMedia": max_media,"mainTopic": "Maintenance"})

with open(output_path, "w", encoding="utf-8") as output_file:

    json.dump(data, output_file, indent=2)