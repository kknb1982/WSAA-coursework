# This retrieves the dataset for the "exchequer account" from the CSO and stores it into a file called "cso.json"

# Author: Kirstin Barnett

import requests
import json

url = "https://ws.cso.ie/public/api.restful/PxStat.Data.Cube_API.ReadDataset/FIQ02/JSON-stat/2.0/en"

def getAll():
    response = requests.get(url)
    return response.json()

if __name__ == "__main__":
    with open("cso.json", "wt") as fp:
        print(json.dumps(getAll()), file=fp)




