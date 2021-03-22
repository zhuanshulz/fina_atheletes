import os
import json

dir = './data_multithread/'
dict_var = {}
for home, dirs, files in os.walk(dir):
    for filename in files:
        json_file = './data_multithread/' + filename
        with open(json_file, encoding="utf-8") as f_demo:
            data = json.loads(f_demo.read())
            f_demo.close()
        dict_var[data['FullName']] = data
with open("./swim_data.json", "w", encoding='utf-8') as f:
    f.write(json.dumps(dict_var,indent=4, ensure_ascii=False))
