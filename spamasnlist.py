import os
import requests
import json

def download_file(url, save_path):
    response = requests.get(url)
    with open(save_path, 'wb') as file:
        file.write(response.content)

def is_valid_asn(asn):
    # Add your own criteria for validating ASNs, e.g., check for numeric values
    return asn.isdigit()

def extract_asn_from_json(json_data):
    asns = set()
    for line in json_data:
        try:
            entry = json.loads(line)
            asn = entry.get('asn')
            if asn and is_valid_asn(str(asn)):
                asns.add(str(asn))
        except json.JSONDecodeError:
            # Ignore invalid JSON lines
            pass
    return asns

def save_asns_to_file(asns, output_file):
    sorted_asns = sorted(asns, key=lambda x: int(x.lstrip('AS')))
    with open(output_file, 'w') as file:  # Open the file in write mode to overwrite existing content
        for asn in sorted_asns:
            file.write(f'AS{asn}\n')

def delete_file(file_path):
    if os.path.exists(file_path):
        os.remove(file_path)

if __name__ == "__main__":
    file_url = "https://www.spamhaus.org/drop/asndrop.json"
    output_directory = r"C:\Users\Logan\Documents\GitHub\AdGuard-Home-Allowlist\configpersonal"
    output_file = "asnspam.txt"
    json_file_path = 'asndrop.json'

    # Download JSON file
    download_file(file_url, json_file_path)

    # Load JSON data line by line
    with open(json_file_path, 'r') as json_file:
        # Extract valid ASNs from JSON data
        new_asns = extract_asn_from_json(json_file)

    # Save sorted and valid ASNs to a text file in the specified directory (overwriting existing content)
    output_path = os.path.join(output_directory, output_file)
    save_asns_to_file(new_asns, output_path)

    # Delete the JSON file
    delete_file(json_file_path)

    print(f'ASNs extracted, sorted, and saved to {output_path}')
