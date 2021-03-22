import requests
import json
import time
# https://api.fina.org/fina/athletes/1166191/results
target = 'https://api.fina.org/fina/athletes/'
results_end = '/results'

with open("swim_athletes.json","r",encoding="utf-8") as f:
    swim_athletes_string = f.read()
    swim_athletes_json = json.loads(swim_athletes_string)
    f.close()

req_json_all = {}
time_counter = 0
for i in swim_athletes_json["content"]:
    id_athletes = i["id"]
    url = target + str(id_athletes) + results_end
    req_temp = requests.get(url)
    req_json = req_temp.json()
    # req_json_all.update({str(id_athletes):req_json})
    time.sleep(0.1)
    print("%d   //  %d" ,time_counter, swim_athletes_json["pageInfo"]["numEntries"])
    json_file_name = ".//data//" + str(time_counter) + '_swim_data.json'
    
    time_counter = time_counter + 1
    with open(json_file_name, "w", encoding='utf8') as fp:
        fp.write(json.dumps(req_json,indent=4, ensure_ascii=False))
        fp.close()
    # if time_counter==2 :
    #     break

json_file_name = 'swim_data.json'
with open(json_file_name, "w", encoding='utf8') as fp:
    fp.write(json.dumps(req_json_all,indent=4, ensure_ascii=False))
    fp.close()
