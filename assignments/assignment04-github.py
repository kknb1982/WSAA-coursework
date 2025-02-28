# Read in a file from a repository, replace all instances of the word "Andrew" with "Kirstin", and write the modified file back to the repository.
# Author: Kirstin Barnett

import requests
from config import apikeys as cfg

apikey = cfg["apikeys"]

url = "https://github.com/kknb1982/WSAA-coursework/mywork"
filename = "classlist.txt"

# Get the file from the repository
response = requests.get(url, auth=('token', apikey))
response.raise_for_status() # Check for errors

# Replace all instances of "Andrew" with "Kirstin"
modified_text = response.text.replace("Andrew", "Kirstin")  

# Write the modified file back to the repository
response = requests.put(url, data=modified_text)
response.raise_for_status() # Check for errors
print("File has been modified and written back to the repository.")

