import json
import os
from os import listdir
from os.path import isfile,join

dirname = "."
json_files = sorted([f for f in listdir(dirname) if isfile(join(dirname,f)) and ("." not in f and "_" not in f and f != 'combined' and f != 'combined2')])
print(json_files)

data = json.load(open(json_files[0]))

for f in json_files[1:]:
    data.extend(json.load(open(f)))

with open('combined2','w') as f:
    json.dump(data,f)

data = json.load(open('combined2'))
# s = set()
for i in data:

    for p in i['Pollutants']:
        name = p[0]
        i[name+'_avg'] = p[1]
        i[name+'_max'] = p[2]
        i[name+'_min'] = p[3]

# print(s)
with open('changed_pollutants2','w') as f:
    json.dump(data,f)



