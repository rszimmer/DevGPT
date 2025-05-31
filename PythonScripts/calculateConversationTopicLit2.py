import json
import os
import re
import random
import math

output_path = "./conversarion_media_literature2.json"
randomSampleList = []
quality = 0
issue = 0
documentations = 0
featuret = 0
manipulation = 0
energy = 0
test = 0
setup = 0
debug = 0
learning = 0
security = 0
optimization = 0

    
with open(f"../topic_extraction_results_literatur2.json", 'r') as json_data:
    data = json.load(json_data)
    for entry in data:
        quality = 0
        issue = 0
        documentations = 0
        featuret = 0
        manipulation = 0
        energy = 0
        test = 0
        setup = 0
        debug = 0
        learning = 0
        security = 0
        optimization = 0
        for prompt in entry:
            if prompt["topic"] ==     "Code Quality Management":
                quality += prompt["score"]
            elif prompt["topic"] ==     "Commit Issue Resolution":
                issue += prompt["score"]
            elif prompt["topic"] ==     "Documentation Generation":
                documentations += prompt["score"]
            elif prompt["topic"] ==     "New Feature Implementation":
                featuret += prompt["score"]
            elif prompt["topic"] ==     "Code Manipulation and Generation":
                manipulation += prompt["score"]
            elif prompt["topic"] == "Energy-aware Development":
                energy += prompt["score"]
            elif prompt["topic"] ==     "Testing and Quality Assurance":
                test += prompt["score"]
            elif prompt["topic"] ==     "Development and Environment Setup":
                setup += prompt["score"]
            elif prompt["topic"] ==     "Debugging and Error Management":
                debug += prompt["score"]
            elif prompt["topic"] ==     "Code Learning":
                learning += prompt["score"]
            elif prompt["topic"] ==     "Security Management":
                security += prompt["score"]
            elif prompt["topic"] ==     "Software Development Management and Optimization":
                optimization += prompt["score"]
                
        count = len(entry) if len(entry) != 0 else 1
        qualityMedia = quality / count
        issueMedia = issue /  count
        documentationsMedia = documentations / count
        featuretMedia = featuret / count
        manipulationMedia = manipulation / count
        energyMedia = energy / count
        testMedia = test / count
        setupMedia = setup / count
        debugMedia = debug / count
        learningMedia = learning / count
        securityMedia = security / count
        optimizationMedia = optimization / count
        max_media = max([qualityMedia,
                        issueMedia,
                        documentationsMedia,
                        featuretMedia,
                        manipulationMedia,
                        energyMedia,
                        testMedia,
                        setupMedia,
                        debugMedia,
                        learningMedia,
                        securityMedia,
                        optimizationMedia])
        if qualityMedia == max_media:
            entry.append({"topicMedia": max_media,"mainTopic": "Code Quality Management"})
        elif issueMedia == max_media:
            entry.append({"topicMedia": max_media,"mainTopic": "Commit Issue Resolution"})
        elif documentationsMedia == max_media:
            entry.append({"topicMedia": max_media,"mainTopic": "Documentation Generation"})
        elif featuretMedia == max_media:
            entry.append({"topicMedia": max_media,"mainTopic": "New Feature Implementation"})
        elif manipulationMedia == max_media:
            entry.append({"topicMedia": max_media,"mainTopic": "Code Manipulation and Generation"})
        elif energyMedia == max_media:
            entry.append({"topicMedia": max_media,"mainTopic": "Energy-aware Development"})
        elif testMedia == max_media:
            entry.append({"topicMedia": max_media,"mainTopic": "Testing and Quality Assurance"})
        elif setupMedia == max_media:
            entry.append({"topicMedia": max_media,"mainTopic": "Development and Environment Setup"})
        elif debugMedia == max_media:
            entry.append({"topicMedia": max_media,"mainTopic": "Debugging and Error Management"})
        elif learningMedia == max_media: 
            entry.append({"topicMedia": max_media,"mainTopic":     "Code Learning"})
        elif securityMedia == max_media:
            entry.append({"topicMedia": max_media,"mainTopic": "Security Management"})
        elif optimizationMedia == max_media:
            entry.append({"topicMedia": max_media,"mainTopic": "Software Development Management and Optimization"})

with open(output_path, "w", encoding="utf-8") as output_file:
    json.dump(data, output_file, indent=2)