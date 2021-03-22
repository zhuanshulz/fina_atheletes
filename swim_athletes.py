import requests
import json
import time
target = 'https://api.fina.org/fina/athletes?gender=M&discipline=SW&nationality=&name=&'
page = 'page='
pagenum = 333
pagesize = '&pageSize=50'
# req = requests.get(url=(target + page + "0" + pagesize))
req_json_all = {"pageInfo": {},"content": []}
for i in range(pagenum):
    url=target + page + str(i) + pagesize
    req_temp = requests.get(url)
    req_json = req_temp.json()
    req_json_all["pageInfo"].update(req_json["pageInfo"])
    req_json_all["content"] = req_json_all["content"] + req_json["content"]
    time.sleep(0.1)
    print(i)
json_file_name = 'swim_athletes.json'
with open(json_file_name, "w", encoding='utf8') as fp:
    fp.write(json.dumps(req_json_all,indent=4, ensure_ascii=False))
    fp.close() 
    # req_json_all.update(req_json)
# print(req_json_all)
# print(req_json)

# for i in range(pagenum):
#     req = requests.get(url=(target + page + i + pagesize))
#     req_json = req.json
#     # print(req.json)