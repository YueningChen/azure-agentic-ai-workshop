from azure.identity import DefaultAzureCredential
from azure.storage.blob import BlobServiceClient

account_url = "https://<your-storage-account-name>.blob.core.windows.net/"

try:
    credential = DefaultAzureCredential()
    blob_service_client = BlobServiceClient(account_url=account_url, credential=credential)

    containers = blob_service_client.list_containers()
    print("Containers in the storage account:")
    for container in containers:
        print(f"- {container['name']}")
except Exception as e:
    print(f"An error occurred: {e}")
