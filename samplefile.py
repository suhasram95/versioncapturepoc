# import os 
# import logging
# # documents = os.path.abspath('Documents')
# # os.chdir(documents)
# f = open("Documents/myfile.txt", "w")
# for root, dirs, files in os.walk("."):
#     for name in dirs:
#         print(os.path.join(root, name))
#         logging.info("The directory is ")
#         f.write(os.path.join(root, name)+"\n")

#     for name in files:
#         print(os.path.join(root, name))
#         f.write(os.path.join(root, name)+"\n")
# f.close()

# my_dict = {1: "Cisco", 2: "HP", 3: "Juniper", 4: "Arista", 5: "Avaya"}
# print(my_dict.values())

# import json
# import requests
# from pprint import pprint
# import yaml
# response = requests.get("https://jsonplaceholder.typicode.com/todos")
# todos = json.loads(response.text)
# todos_by_user = dict()
# for todo in todos:
#     if todo["completed"]:
#         try:
#             todos_by_user[todo["userId"]] += 1
#         except KeyError:
#             # this user has not been seen. Set their count to 1.
#             todos_by_user[todo["userId"]] = 1

# for todo in todos:
#     print ("The title is {} and the id is {}".format(todo["title"], todo["id"]))
import requests
import json
import sys
from pprint import pprint
import os
import subprocess
import pandas as pd
# os.chdir('repos_temp')
print(os.getcwd())
# username = sys.argv[1]
response = requests.get("https://api.github.com/users/suhasram95/repos")
print(type(response.status_code))
print(response.status_code)
print(response.status_code != 200)
if (response.status_code != 200):
    print("Invalid GitHub Username. Please try again with a valid username")
    sys.exit()
# print(response)
repos_json = json.loads(response.text)
# pprint(repos_json[0])
repos = list()
url = list()
private = list()
data = pd.DataFrame()
for element in repos_json:
    repos.append(element["name"])
    url.append(element["clone_url"])
    private.append(element['private'])

    # url = "git clone "+element["clone_url"]
    # os.system(url)
# subprocess.call("./delete.sh")
list1 = list(zip(repos, url, private))
data = pd.DataFrame(list1, columns=['name', 'url', 'private'])
print(data)
data.to_csv("output.csv")

# for key, value in repos_dict.items():
#     print("The name of the repo is {} and the clone url is {}".format(key, value))

# pprint(repos_json[0])
# pprint(repos_dict)

# for key, value in repos_dict.items():
#     repo = key
#     url = value[0]['url']
#     private = value[0]['private']
#     print("The repo name is {} and the link to the repo is {}, private = {}".format(repo, url, private))