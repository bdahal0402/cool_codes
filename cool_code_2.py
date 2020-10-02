#cerner_2^5_2020
#Drops some good puns
#requirement requests>=2.24.0 (pip install requests)
import requests

response = requests.get('https://icanhazdadjoke.com/', headers={"Accept":"application/json"})
print("Here's a pun: \n {pun}".format(pun=response.json()['joke']))
