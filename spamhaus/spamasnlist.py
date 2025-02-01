import requests
import json
import os

def is_valid_asn(asn):
    return asn.isdigit()

def extract_asn_from_json_lines(json_lines): # Changed function name
    asns = set()
    for line in json_lines:
        try:
            entry = json.loads(line)  # Load each line separately
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
        response = requests.get(file_url, stream=True) # Stream the response
        response.raise_for_status()

        asns = set() # Initialize an empty set outside of the loop
        for line in response.iter_lines(): # Iterate line by line
            if line: # Check if the line is not empty
                decoded_line = line.decode('utf-8') # decode the line
                try:
                    entry = json.loads(decoded_line)
                    asn = entry.get("asn")
                    if asn and is_valid_asn(str(asn)):
                        asns.add(str(asn))
                except (json.JSONDecodeError, TypeError):
                    pass

        output_path = os.path.join(output_directory, output_file)
        save_asns_to_file(asns, output_path)

        print(f"ASNs extracted, sorted, and saved to {output_path}")


    except requests.exceptions.RequestException as e:
        print(f"Error downloading file: {e}")