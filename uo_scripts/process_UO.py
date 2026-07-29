import json
from datetime import datetime

file_name = 'bremerton_661_434.json' 
file_name_rev = 'bremerton_661_434_v2.json' 
timesteps = 4
cutoff = 4

with open(file_name, 'r') as file:
    data = json.load(file)
    
breakpoint()
    
# prepend_text = {"id": 0, "name": "First Item"}
# data.insert(0, prepend_text)
data['project']['climate_zone'] = "5C"
data['project']['begin_date'] = "2025-01-01T07:00:00.000Z"
data['project']['end_date'] = "2025-12-31T07:00:00.000Z"
data['project']["default_template"] = "DOE Ref Pre-1980"
data['project']["weather_filename"] = "USA_WA_Bremerton.National.AP.727928_TMY3.epw"
data['project']["timesteps_per_hour"] = timesteps 

for feat in data['features']: 
    if feat['properties']['type']=='Building':
        clean_str = feat['properties']['year_built'][:cutoff]
        feat['properties']['year_built'] = int(clean_str)
        if feat['properties']['name'] == 'B434': 
            feat['properties']['mixed_type_1']  = 'Office' 
            feat['properties']['mixed_type_1_percentage']  = 50
            feat['properties']['mixed_type_2']  = 'Retail other than mall' 
            feat['properties']['mixed_type_2_percentage']  = 50


breakpoint()


with open(file_name_rev, 'w') as file:
    json.dump(data, file, indent=4, sort_keys=True)