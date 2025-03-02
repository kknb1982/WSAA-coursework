# Access the file from the repository
with open(filename, 'r') as fp:
    content = fp.read()
    print("File has been read from the repository.")

# Search for "Andrew" and replace with "Kirstin" in the JSON data
updatedtxt = content.replace("Andrew", "Kirstin")
print("Text has been modified.")

with open (filename, "w") as fp:
    fp.write(updatedtxt)
    fp.close()

print("File has been searched and modified where needed.")

# Write the modified file back to the repository
response = requests.put(url,  auth=('token', apikey))
print("File has been modified and written back to the repository.")

