from azure.storage.blob import BlobServiceClient
import os

# Azure Storage account connection string
connection_string = "<YOUR_AZURE_STORAGE_CONNECTION_STRING>"
container_name = "my-container"
blob_name = "sample.txt"
local_file_path = "sample.txt"

def upload_to_blob():
    blob_service_client = BlobServiceClient.from_connection_string(connection_string)
    container_client = blob_service_client.get_container_client(container_name)
    
    with open(local_file_path, "rb") as file:
        container_client.upload_blob(blob_name, file, overwrite=True)
    print("✅ File uploaded successfully.")

def download_from_blob():
    blob_service_client = BlobServiceClient.from_connection_string(connection_string)
    container_client = blob_service_client.get_container_client(container_name)
    
    with open("downloaded_sample.txt", "wb") as file:
        file.write(container_client.download_blob(blob_name).readall())
    print("✅ File downloaded successfully.")

# Run functions
upload_to_blob()
download_from_blob()