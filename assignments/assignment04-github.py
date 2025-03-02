# Read in a file from a repository, replace all instances of the word "Andrew" with "Kirstin", and write the modified file back to the repository.
# Author: Kirstin Barnett

from github import Github
from config import apikeys as cfg
import requests


filename = "classlist.txt"
apikey = cfg["apikeys"]
g = Github(apikey)
repository = "kknb1982/WSAA-coursework"

# Access the repository
repo = g.get_repo(repository)

# Get the download URL for the file
file_info = repo.get_contents("classlist.txt")
fileurl = file_info.download_url

# Output the content of the file
response = requests.get(fileurl)
filecontent = response.text

# Update the content of the file
newcontent = filecontent.replace("Andrew", "Kirstin")

# Write the updated content back to the file
githubresponse = repo.update_file(file_info.path, "Replaced Andrew with Kirstin", newcontent, file_info.sha)
print(githubresponse)