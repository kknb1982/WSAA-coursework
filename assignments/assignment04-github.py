# Read in a file from a repository, replace all instances of the word "Andrew" with "Kirstin", and write the modified file back to the repository.
# Author: Kirstin Barnett

from github import Github
import requests
from config import apikeys as cfg

apikey = cfg["githubkey"]

g = Github(apikey)


# Get the file from the repository
url = "https://raw.githubusercontent.com/AndrewFinnell/IS211_Assignment4/master/README.md"
response = requests.get(url)
response.raise_for_status() # Check for errors

# Replace all instances of "Andrew" with "Kirstin"
modified_text = response.text.replace("Andrew", "Kirstin")  

# Write the modified file back to the repository
url = "https://raw.githubusercontent.com/AndrewFinnell/IS211_Assignment4/master/README.md"
response = requests.put(url, data=modified_text)
response.raise_for_status() # Check for errors
print("File has been modified and written back to the repository.")

