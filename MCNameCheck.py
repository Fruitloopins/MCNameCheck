import requests
import time
import datetime

#List all UUIDs of accounts you want to check for name changes, the more you add the more inaccurate the time will be
uuidlist = ["fed0ec4af1ad4b979443876391668b34", "069a79f444e94726a5befca90e38aaf5", "f17d77abaed444e796efec9cd473eda3"]

#Creating an empty list to add names to
namelist = []

#Adding all current names of provided UUIDs to a list
for i in uuidlist:
    request = requests.get(f"https://api.mojang.com/user/profile/{i}").json()
    name = request["name"]
    namelist.append(name)
    print("Added", name, "to namelist")

print(namelist)

#Checking all provided UUIDs for changes to their name in the API
while True:
    for i in uuidlist:
        request = requests.get(f"https://api.mojang.com/user/profile/{i}").json()
        namecheck = request["name"]

        if namecheck not in namelist:
            ts = time.time()
            timestamp = datetime.datetime.fromtimestamp(ts).strftime('%d-%m-%Y %H:%M:%S.%f')
            print("Account", namecheck, i, "changed at", timestamp)
            uuidlist.remove(i)