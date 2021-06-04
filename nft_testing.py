#import modules
import requests
from PIL import Image
import os

# get list of token id's
token_list = []
print("Type in the list of token ID's, pressing enter after each ID. When you are done, press Y")
check = False
while check == False:
    token = str(input("Type the token ID here: \n"))
    if token == "Y":
        check = True
    else:
        token_list.append(token)
limit = len(token_list)

#get and print the data from the API
url = "https://api.opensea.io/api/v1/assets"
querystring = {"token_ids": token_list,
                "order_by": "token_id",
                "order_direction": "desc",
                "offset": "0",
                "limit": limit}
response = requests.get(url=url, params=querystring)
print(response.text)

# format the data with json, and count the number of NFT's
data = response.json()
count = len(data["assets"])
print("NFT Count: " + str(count))

# get the names into a list
names = []
for i in range(count):
    name = data["assets"][(i-1)]["name"]
    names.append(name)
print("NFT Names:" + str(names))

# get the images into a list
images = []
for i in range(count):
    image = data["assets"][(i-1)]["image_url"]
    images.append(image)
print("NFT Image Links: " + str(images))

# set path to download images to
path = input("Path for files to be downloaded to (with capitals): \n")
os.chdir(path)
print("Path set")

# download the images
num = 0
for i in range(count):
    response = requests.get(images[(i-1)])
    name = names[(i-1)]
    file = open(name, "a+b")
    file.write(response.content)
    file.close()
    num+=1
print("Downloads successful. \n Number of downloads: " + str(num))
