import configparser
import csv

import requests


parser = configparser.ConfigParser()
parser.read("pipeline.conf")
host = parser.get("api_config", "host")
port = parser.get("api_config", "port")

API_URL = f"http://{host}:{port}"
DATA_FOLDER = "data_api"

### Events
data = "events"
date = "2021-02-10"
response = requests.get(f"{API_URL}/{data}/?created_at={date}")
data = response.json()
with open(f"{DATA_FOLDER}/events.csv", "w") as f:
    writer = csv.writer(f)
    header = data[0].keys()
    writer.writerow(header)

    for each in data:
        writer.writerow(each.values())

### Users
data = "users"
date = "2020-10-23"
# ลองดึงข้อมูลจาก API เส้น users และเขียนลงไฟล์ CSV
# YOUR CODE HERE
response = requests.get(f"{API_URL}/{data}/?created_at={date}")
data = response.json()
with open(f"{DATA_FOLDER}/users.csv", "w") as f:
    writer = csv.writer(f)
    header = data[0].keys()
    writer.writerow(header)

    for each in data:
        writer.writerow(each.values())

### Orders
data = "orders"
date = "2021-02-10"
# ลองดึงข้อมูลจาก API เส้น orders และเขียนลงไฟล์ CSV
# YOUR CODE HERE
response = requests.get(f"{API_URL}/{data}/?created_at={date}")
data = response.json()
with open(f"{DATA_FOLDER}/orders.csv", "w") as f:
    writer = csv.writer(f)
    header = data[0].keys()
    writer.writerow(header)

    for each in data:
        writer.writerow(each.values())

## order_items
data = "order-items"
date = "2021-02-10"
# ลองดึงข้อมูลจาก API เส้น orders และเขียนลงไฟล์ CSV
# YOUR CODE HERE
response = requests.get(f"{API_URL}/{data}/?created_at={date}")
data = response.json()
with open(f"{DATA_FOLDER}/order-items.csv", "w") as f:
    writer = csv.writer(f)
    header = data[0].keys()
    writer.writerow(header)

    for each in data:
        writer.writerow(each.values())

## promos
data = "promos"
date = "2021-02-10"
# ลองดึงข้อมูลจาก API เส้น orders และเขียนลงไฟล์ CSV
# YOUR CODE HERE
response = requests.get(f"{API_URL}/{data}/?created_at={date}")
data = response.json()
with open(f"{DATA_FOLDER}/promos.csv", "w") as f:
    writer = csv.writer(f)
    header = data[0].keys()
    writer.writerow(header)

    for each in data:
        writer.writerow(each.values())

## addresses
data = "addresses"
date = "2021-02-10"
# ลองดึงข้อมูลจาก API เส้น orders และเขียนลงไฟล์ CSV
# YOUR CODE HERE
response = requests.get(f"{API_URL}/{data}/?created_at={date}")
data = response.json()
with open(f"{DATA_FOLDER}/addresses.csv", "w") as f:
    writer = csv.writer(f)
    header = data[0].keys()
    writer.writerow(header)

    for each in data:
        writer.writerow(each.values())

# ## users
# data = "users"
# date = "2022-02-10"
# # ลองดึงข้อมูลจาก API เส้น orders และเขียนลงไฟล์ CSV
# # YOUR CODE HERE
# response = requests.get(f"{API_URL}/{data}/?created_at={date}")
# data = response.json()
# print(data)

# with open(f"{DATA_FOLDER}/users.csv", "w") as f:
#     writer = csv.writer(f)
#     header = data[0].keys()
#     writer.writerow(header)

#     for each in data:
#         writer.writerow(each.values())

# ## users
# data = "users"
# date = "2022-02-10"
# response = requests.get(f"{API_URL}/{data}/?created_at={date}")
# data = response.json()

# # Check if data is not empty before processing it
# if data:
#     with open(f"{DATA_FOLDER}/users.csv", "w") as f:
#         writer = csv.writer(f)
#         header = data[0].keys()
#         writer.writerow(header)

#         for each in data:
#             writer.writerow(each.values())
# else:
#     print("No users data found for the specified date.")

## users
data = "users"
date = "2022-02-10"
# ลองดึงข้อมูลจาก API เส้น orders และเขียนลงไฟล์ CSV
# YOUR CODE HERE
response = requests.get(f"{API_URL}/{data}/?created_at={date}")
data = response.json()
if not data:
    data = [{}] 

with open(f"{DATA_FOLDER}/users.csv", "w", newline="") as f:
    writer = csv.writer(f)
    header = data[0].keys()
    writer.writerow(header)

    for each in data:
        writer.writerow(each.values())

## products
data = "products"
date = "2021-02-10"
# ลองดึงข้อมูลจาก API เส้น orders และเขียนลงไฟล์ CSV
# YOUR CODE HERE
response = requests.get(f"{API_URL}/{data}/?created_at={date}")
data = response.json()
with open(f"{DATA_FOLDER}/products.csv", "w") as f:
    writer = csv.writer(f)
    header = data[0].keys()
    writer.writerow(header)

    for each in data:
        writer.writerow(each.values())


# "addresses": "http://34.87.139.82:8000/addresses/",
# "events": "http://34.87.139.82:8000/events/",
# "order-items": "http://34.87.139.82:8000/order-items/",
# "orders": "http://34.87.139.82:8000/orders/",
# "products": "http://34.87.139.82:8000/products/",
# "promos": "http://34.87.139.82:8000/promos/",
# "users": "http://34.87.139.82:8000/users/"