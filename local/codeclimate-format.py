import json
import sys

with open(sys.argv[1]) as json_file:
    json_data = json.load(json_file)

    for analysis in json_data:
        analysis['categories'] = ['Bug Risk']
        if 'end' not in analysis['location']['lines']:
            analysis['location']['lines']['end'] = analysis['location']['lines']['begin']
        print(json.dumps(analysis) + '\0')
