import json
 
# Opening JSON file
with open('result.json') as json_file:
    data = json.load(json_file)
    
    for analysis in data:
        #print(analysis)
        analysis['categories'] = ['Bug Risk']
        if 'end' not in analysis['location']['lines']:
            analysis['location']['lines']['end'] = analysis['location']['lines']['begin']
        print(json.dumps(analysis) + '\0')

