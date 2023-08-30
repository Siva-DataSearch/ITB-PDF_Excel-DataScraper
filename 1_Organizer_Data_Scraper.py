import requests
import xml.etree.ElementTree as ET
import csv
import time

url = "https://live.messebackend.aws.corussoft.de/webservice/search"
start_result_row = 0
end_result_row = 5575
organizations = []

# Create a session
session = requests.Session()

headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/603.3.8 (KHTML, like Gecko) Version/10.1.2 Safari/603.3.8"
}

while start_result_row <= end_result_row:
    payload = {
        "topic": "2023_itb",
        "os": "web",
        "appUrl": "https://www.itb.com/en/itb-berlin-for-visitors/exhibitor-list/#/",
        "lang": "en",
        "apiVersion": "39",
        "timezoneOffset": "-450",
        "userLang": "en-IN",
        "filterlist": "entity_orga",
        "startresultrow": str(start_result_row),
        "numresultrows": "25"
    }

    # Add a 60-second delay if start_result_row is 2000 or 4000
    if start_result_row in [2000, 4000]:
        time.sleep(60)
    
    # Add a 2-second delay before each request
    time.sleep(2)

    response = session.post(url, data=payload, headers=headers)

    if response.status_code == 200:
        # Parse the XML response
        root = ET.fromstring(response.text)

        # Extract and store the organization data in the list of dictionaries
        for organization in root.findall(".//organization"):
            organization_id = organization.get("id")
            organization_name = organization.get("name")

            # Create a dictionary for the organization data and append it to the list
            organization_data = {'organization_id': organization_id, 'organization_name': organization_name}
            organizations.append(organization_data)

        # Increment the start_result_row by 25 for the next request
        start_result_row += 25

    else:
        print(f"Failed to fetch data. Status Code: {response.status_code}")
        break

# Write the data to a CSV file
filename = "organizations_data.csv"
with open(filename, mode="w", newline="", encoding="utf-8") as csvfile:
    fieldnames = ['organization_id', 'organization_name']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

    # Write the header
    writer.writeheader()

    # Write the data for each organization
    for organization in organizations:
        writer.writerow(organization)

print(f"Data has been written to {filename}.")
