from pymongo import MongoClient

# Connect to the MongoDB server
client = MongoClient()

# Connect to the logs database
db = client.logs

# Connect to the nginx collection
collection = db.nginx

# Get the number of documents in the collection
num_documents = collection.count_documents({})

# Print the number of documents in the collection
print(f"{num_documents} logs")

# Get the number of documents with each method
methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
for method in methods:
    count = collection.count_documents({"method": method})
    print(f"    method {method}: {count}")

# Get the number of documents with method=GET and path=/status
status_check_count = collection.count_documents({"method": "GET", "path": "/status"})
print(f"{status_check_count} status check")
