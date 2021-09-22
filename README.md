# nft
Program for my friend that allows him to download NFTs using OpenSea's API (downloads the image of the NFT). Inputs the token IDs of the NFTs, and then sends a request to the API. 

nft_downloader.py- program that inputs and downloads the NFTs to a specified path
<br/>id_list.py- extra program that allows user to input token IDs, and appends said IDs to a file (used to keep track of downloaded NFTs)

Modules needed: 
- requests
- PIL
- os

Caveats:
- neither script reads off of an Excel or CSV sheet- all token IDs must be entered one by one into the command prompt
- id_list and nft_downloader are not synced- the token IDs must be entered into both separately (if using id_list, which is not required to use nft_downloader)
