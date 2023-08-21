import json

import requests


if __name__ == "__main__":
    url = "https://dog.ceo/api/breeds/image/random" # api
    response = requests.get(url)
    data = response.json() # schema
    print(data)

    # Your code here
    with open("dogs.json", "w") as f:
        json.dump(data,f)