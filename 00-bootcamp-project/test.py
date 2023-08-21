import configparser
import csv
import requests

parser = configparser.ConfigParser()
parser.read("pipeline.conf")
host = parser.get("api_config", "host")
port = parser.get("api_config", "port")

API_URL = f"http://{host}:{port}"
DATA_FOLDER = "data"

date = "2021-02-11"

# Define a helper function to write data to a CSV file
def write_data_to_csv(data_type, json_data):
    filename = f"{DATA_FOLDER}/{data_type}.csv"
    with open(filename, "w", newline="") as f:
        writer = csv.writer(f)
        if json_data:
            header = json_data[0].keys()
            writer.writerow(header)

            for each in json_data:
                writer.writerow(each.values())
            print(f"done {data_type}")
        else:
            print(f"No {data_type} data available. Created an empty CSV file.")
            writer.writerow([])  # Write an empty row as the header

# Events
data_type = "events"
response = requests.get(f"{API_URL}/{data_type}/?created_at={date}")
json_data = response.json()
write_data_to_csv(data_type, json_data)

# Users
data_type = "users"
response = requests.get(f"{API_URL}/{data_type}/?created_at={date}")
json_data = response.json()
write_data_to_csv(data_type, json_data)

# Orders
data_type = "orders"
response = requests.get(f"{API_URL}/{data_type}/?created_at={date}")
json_data = response.json()
write_data_to_csv(data_type, json_data)
