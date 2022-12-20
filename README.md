# MCNameCheck
**I AM NOT CERTAIN THIS WORKS, YOU ARE FREE TO VERIFY IT.**

Constantly checks a set of provided Minecraft UUIDs for changes to their associated username.

Useful for name sniping on a small scale if you want to know (close to) the exact time the name was changed as Mojang no longer provides an API route for this information.

Simply run MCNameCheck.py and it will create a config file in the same directory where you can enter as many UUIDs as you want separated by spaces. The more UUIDs you add the longer it takes to cycle through all names meaning that the time logged when the name does change might not be wholly accurate, only providing a few names should keep times relatively accurate.

The script will automatically stop checking a username and log it to the same directory in namechange.log if a name change is detected.
