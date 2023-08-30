import pandas as pd
import re
import requests
import time
import urllib3

# Create a session
session = requests.Session()

headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/603.3.8 (KHTML, like Gecko) Version/10.1.2 Safari/603.3.8"
}

# Read the CSV file
filename = "organizations_data.csv"
data = pd.read_csv(filename)

# Access the organization_id and organization_name columns
org_data = data[['organization_id', 'organization_name']]

# Base URL
base_url = "https://www.itb.com/en/itb-berlin-for-visitors/exhibitor-list/#/detail/"

# Create a list to store the complete URLs
complete_urls = []

# Apply regular expressions to transform the organization names
for index, row in org_data.iterrows():
    org_id = row['organization_id']
    org_name = row['organization_name']

    # Convert uppercase letters to lowercase
    org_name = org_name.lower()

    # Remove all alphanumeric characters and spaces with hyphens
    org_name = re.sub(r'[^a-z0-9]+', '-', org_name)

    # Concatenate org_name with the base_url and organization_id to form the complete URL
    complete_url = base_url + org_name + '--' + str(org_id)

    complete_urls.append(complete_url)

    # Print the first 10 complete URLs as an example
    if index < 10:
        print(f"{index + 1}. {complete_url}, {row['organization_name']}")

print(len(complete_urls))

# Check the validity of each URL
valid_urls = []
invalid_urls = []
for index, url in enumerate(complete_urls, start=1):
    success = False
    retry_count = 0
    while not success and retry_count < 3:  # Retry up to 3 times
        try:
            response = session.get(url, headers=headers)
            if response.status_code // 100 == 2:
                valid_urls.append(url)
                success = True
            else:
                invalid_urls.append(url)
                print(f"URL {url} is invalid (Status Code: {response.status_code})")
        except (requests.exceptions.ConnectionError, urllib3.exceptions.MaxRetryError):
            retry_count += 1
            print(f"Retrying {url} (Retry {retry_count}/3)")

# Write valid URLs to a text file
with open("PDF_URLs_5567.txt", "w") as file:
    for url in valid_urls:
        file.write(url + "\n")

print(f"{len(valid_urls)} valid URLs have been written to PDF_URLs_5567.txt")

# Print invalid URLs
if(len(invalid_urls)) > 0:
    print("Invalid URLs:")
    for url in invalid_urls:
        print(url)

print("script completed")
