import requests
import json
url = "https://api.orhanaydogdu.com.tr/deprem/kandilli/live"

payload = {}
headers = {}

response = requests.request("GET", url)

result = json.loads(response.text)


#print(result)
count = 0
print("{:<24} {:<39}  {:<12}"
      .format("Tarih","Bölge","Büyüklük","Derinlik"))
for i in result["result"]:
    if(count>10):
        break
        if(i["mag"]>3):
            print("{:<24} {:<39} {:<12} {:<12}"
                  .format(i["date"],i["title"], i["mag"], i["depth"]))
            count += 1
