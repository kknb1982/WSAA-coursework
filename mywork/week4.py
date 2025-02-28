import requests
import json

url = "http://andrewbeatty1.pythonanywhere.com/books"

def readbooks():
    response = requests.get(url)
    # we could do checking for correct response code here
    response.json()
    response["id"] = id
if __name__ == "__main__":
    print(readbooks(id))