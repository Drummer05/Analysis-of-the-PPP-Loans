#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# Download modules
get_ipython().system('pip install azure-storage-blob')
get_ipython().system('pip install boto3')
get_ipython().system('pip install pandas')
get_ipython().system('pip install mysql-connector-python')
get_ipython().system('pip install google-cloud-bigquery')


# In[ ]:


## Importing Libraries
from azure.storage.blob import BlobServiceClient, ContainerClient, BlobClient
import os
import requests
from bs4 import BeautifulSoup
import re
import boto3
import glob
import pandas as pd
import mysql.connector
import os


# In[ ]:


# Import the os module which provides functions for interacting with the operating system
import os

# Set the path of the folder to be used as the new working directory
folder_path = "datappploan20230420"

# Change the current working directory to the one specified in folder_path
os.chdir(folder_path)

# Print the current working directory to verify that it has been changed successfully
print(os.getcwd())


# In[ ]:


url = "https://data.sba.gov/dataset/ppp-foia"

# Download the webpage content
response = requests.get(url)
page_content = response.text

# Parse the HTML content with BeautifulSoup
soup = BeautifulSoup(page_content, "html.parser")

# Find all anchor tags containing CSV file links
csv_links = soup.find_all("a", href=re.compile(".*\.csv"))

# Define the destination folder for the downloaded CSV files
destination_folder = "C:\\Users\\Carlos\\Desktop\\datappploan20230420"

# Download each CSV file to the specified destination folder
for link in csv_links:
    csv_url = link["href"]
    csv_filename = os.path.basename(csv_url)
    destination_file = os.path.join(destination_folder, csv_filename)

    print(f"Downloading {csv_url}...")

    # Download the CSV file
    with requests.get(csv_url, stream=True) as r:
        r.raise_for_status()
        with open(destination_file, "wb") as f:
            for chunk in r.iter_content(chunk_size=8192):
                f.write(chunk)

    print(f"Downloaded {csv_filename} to {destination_file}.")

print("All CSV files have been downloaded.")


# In[ ]:


# List all containers in the blob storage
all_containers = blob_service_client.list_containers()
for container in all_containers:
    print(container.name)
    
    
# Name of the container and blob (file)
container_name = "pppdata"
blob_name = "stcis4400projects"
file_path = r"C:\Users\Carlos\Desktop\datappploan20230420"

# Get the container client
container_client = blob_service_client.get_container_client(container_name)

# Upload the file
with open(file_path, "rb") as data:
    container_client.upload_blob(name=blob_name, data=data)


# In[ ]:


# Your connection string goes here (censored)
CONNECTION_STRING = "Censored"

# Create a BlobServiceClient using the connection string
blob_service_client = BlobServiceClient.from_connection_string(CONNECTION_STRING)

# Now you can use the blob_service_client to interact with your blob storage

# Name of the container
container_name = "pppdata"
container_client = blob_service_client.get_container_client(container_name)

# Directory containing the files you want to upload
directory_path = r"C:\Users\Carlos\Desktop\datappploan20230420"

# Iterate over the files in the directory
for filename in os.listdir(directory_path):
    # Create the full file path
    file_path = os.path.join(directory_path, filename)
    
    # Create the blob name, could be filename or a combination of folder and filename
    blob_name = f"stcis4400projects/{filename}"

    # Upload the file
    try:
        with open(file_path, "rb") as data:
            print(f"Uploading {filename} to blob storage...")
            container_client.upload_blob(name=blob_name, data=data, overwrite=True)
            print(f"Uploaded {filename}")
    except FileNotFoundError:
        print(f"The file at {file_path} was not found.")
    except Exception as e:
        print(f"An error occurred: {e}")


# In[ ]:




