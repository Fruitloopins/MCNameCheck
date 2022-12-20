import configparser
import os
import requests
import time
import datetime
import logging

#Creating log file and config if necessary
logging.basicConfig(filename="namechange.log", encoding="utf-8", level=logging.INFO)

config = configparser.ConfigParser()
def write_file():
    config.write(open("config.ini", "w"))

if not os.path.exists("config.ini"):
    config.add_section("Accounts")
    config.set("Accounts", "accounts", "UUIDs Go Here")

    with open("config.ini", "w") as configfile:
        config.write(configfile)

config.read("config.ini")

#If user has not filled any UUIDs into config.ini this error will appear
if config["Accounts"]["accounts"] == "UUIDs Go Here":
    print("Please fill your selected UUIDs into the created config.ini file before running the script again")
    quit()

uuidlist = config["Accounts"]["accounts"].split()
print(uuidlist)

#Adding all current names of provided UUIDs to a list
namelist = []
for i in uuidlist:
    request = requests.get(f"https://api.mojang.com/user/profile/{i}").json()
    name = request["name"]
    namelist.append(name)
    print("Added", name, "to namelist")

print(namelist)

#Checking all provided UUIDs for changes to their name in the API
while True:
    for i in uuidlist:
        print("Checking account", i)
        request = requests.get(f"https://api.mojang.com/user/profile/{i}").json()
        namecheck = request["name"]

        #If a change is detected print this to log and remove UUID from list then continue checking
        if namecheck not in namelist:
            ts = time.time()
            timestamp = datetime.datetime.fromtimestamp(ts).strftime('%d-%m-%Y %H:%M:%S.%f')
            print("Account", namecheck, i, "changed at", timestamp)
            logging.info("Account %s %s changed at %s", namecheck, i, timestamp)
            uuidlist.remove(i)
