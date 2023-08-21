import configparser
import csv

import requests


parser = configparser.ConfigParser()
parser.read("pipeline.conf")
host = parser.get("api_config", "host")
port = parser.get("api_config", "port")

API_URL = f"http://{host}:{port}"
DATA_FOLDER = "data"

### Events
data = "events"
date = "2021-02-11"
response = requests.get(f"{API_URL}/{data}/?created_at={date}")
json_data = response.json()
with open(f"{DATA_FOLDER}/{data}.csv", "w") as f:
    writer = csv.writer(f)
    header = json_data[0].keys()
    writer.writerow(header)

    for each in json_data:
        writer.writerow(each.values())
print(f" done {data}")

### Orders
data = "orders"
date = "2021-02-11"
response = requests.get(f"{API_URL}/{data}/?created_at={date}")
json_data = response.json()
with open(f"{DATA_FOLDER}/{data}.csv", "w") as f:
    writer = csv.writer(f)
    header = json_data[0].keys()
    writer.writerow(header)

    for each in json_data:
        writer.writerow(each.values())
print(f" done {data}")


### Users
data = "users"
date = "2020-10-23"
response = requests.get(f"{API_URL}/{data}/?created_at={date}")
json_data = response.json()
if not json_data:
    with open(f"{DATA_FOLDER}/users.csv", "w") as f:
        writer = csv.writer(f)
        header = ["user_id", "first_name", "last_name", "email", "phone_number", "created_at", "updated_at", "address"]
        writer.writerow(header)
else:
    with open(f"{DATA_FOLDER}/{data}.csv", "w") as f:
        writer = csv.writer(f)
        header = json_data[0].keys()
        writer.writerow(header)

        for each in json_data:
            writer.writerow(each.values())

print(f" done {data}")