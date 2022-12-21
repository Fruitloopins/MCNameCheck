# MCNameCheck
[Demonstration video](https://www.youtube.com/watch?v=f99nugP4pf8)

This script constantly checks a set of provided Minecraft UUIDs for changes to their associated username. This is useful for small scale name sniping if you want to know (close to) the exact time the name was changed as Mojang no longer provides an API route for this information.

Simply run MCNameCheck.py and it will create a config file in the same directory where you can enter as many UUIDs as you want separated by spaces. The more UUIDs you add the longer it takes to cycle through all names meaning that the time logged when the name does change might not be wholly accurate, only providing a few names should keep times relatively accurate.

The script will automatically stop checking a username and log it to the same directory in namechange.log if a name change is detected.

Image of it operating and the log it creates if a name change is detected:

![image](https://user-images.githubusercontent.com/49851457/208677880-212abd11-2117-4521-845d-fc826641ded7.png)
![image](https://user-images.githubusercontent.com/49851457/208857445-952da242-69ec-4fa6-b68e-93721a574570.png)
