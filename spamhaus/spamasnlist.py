import requests
import json
import os

def is_valid_asn(asn):
    return asn.isdigit()

def extract_asn_from_json(json_data):
    asns = set()
    for entry in json_data:  # Directly iterate over the parsed JSON
        try:
            asn = entry.get("asn")
            if asn and is_valid_asn(str(asn)):
                asns.add(str(asn))
        except (json.JSONDecodeError, TypeError): # Catch TypeError if entry is not a dict
            pass
    return asns

def save_asns_to_file(asns, output_file):
    sorted_asns = sorted(asns, key=lambda x: int(x.lstrip("AS")))
    with open(output_file, "w") as file:
        for asn in sorted_asns:
            file.write(f"AS{asn}\n")

if __name__ == "__main__":
    file_url = "https://www.spamhaus.org/drop/asndrop.json"
    output_directory = ""
    output_file = "asnspam.txt"

    try:
        response = requests.get(file_url)
        response.raise_for_status()  # Raise an exception for bad status codes (4xx or 5xx)

        try:
            json_data = response.json()  # Parse the JSON directly from the response
            new_asns = extract_asn_from_json(json_data)

            output_path = os.path.join(output_directory, output_file)
            save_asns_to_file(new_asns, output_path)

            print(f"ASNs extracted, sorted, and saved to {output_path}")

        except json.JSONDecodeError:
            print("Error: Invalid JSON received from URL.")

    except requests.exceptions.RequestException as e:
        print(f"Error downloading file: {e}")
