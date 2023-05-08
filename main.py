import subprocess
import re

result = subprocess.run(["netsh", "wlan", "show", "profile"],shell=True, capture_output=True, text=True)
match = re.findall(r":(.*?)\n", result.stdout)
for x in range(len(match)):
    match[x] = match[x].lstrip()
match.pop(0)
with open("Wi-Fi Names.txt", "a") as f:
    for x in match:
        if x != '':
            name = subprocess.run(["netsh", "wlan", "show", "profile", x, 'key="clear"'], capture_output=True, text=True)
            match_two = re.findall(r"Key Content\s*:\s*(.*)", name.stdout)
        if match_two != []:
            string = str(match_two[0])
            f.write(f"{x}   -----   {string}\n")
        else:
            f.write(f"{x}   -----   No Password Available\n")
