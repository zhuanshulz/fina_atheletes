import requests
import json
import time
import os
from multiprocessing import Process

# https://api.fina.org/fina/athletes/1166191/results
target = 'https://api.fina.org/fina/athletes/'
results_end = '/results'

with open("swim_athletes.json","r",encoding="utf-8") as f:
    swim_athletes_string = f.read()
    swim_athletes_json = json.loads(swim_athletes_string)
    f.close()

length = len(swim_athletes_json["content"])
mini_length = 2080
def single_thread(start_num):
    time_counter = 0
    for i in swim_athletes_json["content"][start_num*mini_length:((start_num+1)*mini_length):1]:
        try:
            json_file_name = ".//data_multithread//" + str(start_num) + '_'+ str(time_counter) + '_swim_data.json'
            if (os.path.exists(json_file_name)):
                time_counter = time_counter + 1
                continue
            else:
                if (i==length):
                    break
                id_athletes = i["id"]
                url = target + str(id_athletes) + results_end
                req_temp = requests.get(url)
                req_json = req_temp.json()
                
                # req_json_all.update({str(id_athletes):req_json})
                time.sleep(0.1)
                print(time_counter, swim_athletes_json["pageInfo"]["numEntries"])
                
                time_counter = time_counter + 1
                with open(json_file_name, "w", encoding='utf8') as fp:
                    fp.write(json.dumps(req_json,indent=4, ensure_ascii=False))
                    fp.close()
        except:
            continue

ps = []
p1 = Process(target=single_thread, name="single_thread" + str(0),args=(0,))
p2 = Process(target=single_thread, name="single_thread" + str(1),args=(1,))
p3 = Process(target=single_thread, name="single_thread" + str(2),args=(2,))
p4 = Process(target=single_thread, name="single_thread" + str(3),args=(3,))
p5 = Process(target=single_thread, name="single_thread" + str(4),args=(4,))
p6 = Process(target=single_thread, name="single_thread" + str(5),args=(5,))
p7 = Process(target=single_thread, name="single_thread" + str(6),args=(6,))
p8 = Process(target=single_thread, name="single_thread" + str(7),args=(7,))
p9 = Process(target=single_thread, name="single_thread" + str(7),args=(8,))
ps.append(p1)
ps.append(p2)
ps.append(p3)
ps.append(p4)
ps.append(p5)
ps.append(p6)
ps.append(p7)
ps.append(p8)
ps.append(p9)

for i in range(9):
    ps[i].start()
for i in range(9):
    ps[i].join()
print("all done!")
