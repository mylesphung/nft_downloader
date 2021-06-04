import os

path = input("Set path for the downloads: \n")
os.chdir(path)

name = input("Name for file: \n")
num = input("Number of NFT's: \n")

file = open(name, "a+")
for i in range(num):
    token = input("Input token id: \n")
    file.write(token)
    print("When you are done, type 'Y'")
file.close()
