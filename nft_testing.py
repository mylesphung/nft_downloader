# token id for testing:
#29147704762150632971195140556730043302924574719714568449575404612846710947841

#import modules
import requests
from PIL import Image
import os

token_list = []
print("Type in the list of token ID's, pressing enter after each ID. When you are done, press Y")
check = False
while check == False:
    token = str(input("Type the token ID here: \n"))
    if token == "Y":
        check = True
    else:
        token_list.append(token)

#get the data from the API and print the data
url = "https://api.opensea.io/api/v1/assets"
querystring = {"token_ids": token_list,
                "order_by":"token_id",
                "order_direction":"desc",
                "offset":"0",
                "limit":"10"}
response = requests.get(url=url, params=querystring)
print(response.text)

# format the data with json and extract the image url
data = response.json()
image = data["assets"][0]["image_url"]
print(image)

name = data["assets"][0]["name"]
response = requests.get(image)
os.chdir("C:\Python/gitHub/nft/datasets/D1")
file = open(name, "a+b")
file.write(response.content)
file.close()
im = Image.open("nft_test")
im.show()


