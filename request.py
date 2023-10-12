import requests as req

data = {"content": "Iyad Koteich"}

response = req.post("http://localhost:5000/api/data", json=data)

if response.status_code == 201:
    print("Data added successfully.")
else:
    print("Failed to add data.")


# import requests
#
# data_id_to_delete = 3  # Replace with the ID of the data you want to delete
#
# response = requests.delete(f"http://localhost:5000/api/data/{data_id_to_delete}")
#
# if response.status_code == 200:
#     print("Data deleted successfully.")
# elif response.status_code == 404:
#     print("Data not found.")
# else:
#     print("Failed to delete data.")

