# using requests module we can access the data of a url. the information is in mostly json or html format
import requests

r = requests.get("https://api.github.com/users/PAVANSRIVATSA-97")
with open("External_modules\Pavansrivaatsa.txt", "w") as f:
    f.write(r.text)