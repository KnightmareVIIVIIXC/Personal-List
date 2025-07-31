import requests
import json

def is_valid_asn(asn):
    return asn.isdigit()

def extract_asn_from_json_lines(json_lines):
    asns = set()
    for line in json_lines:
        try:
            entry = json.loads(line)
            asn = entry.get("asn")
            if asn and is_valid_asn(str(asn)):
                asns.add(str(asn))
        except (json.JSONDecodeError, TypeError):
            pass
    return asns

def save_asns_to_file(asns, output_file):
    sorted_asns = sorted(asns, key=lambda x: int(x.lstrip("AS")))
    with open(output_file, "w") as file:
        for asn in sorted_asns:
            file.write(f"AS{asn}\n")

if __name__ == "__main__":
    file_url = "https://www.spamhaus.org/drop/asndrop.json"
    output_file = "asndrop.list"

    try:
        response = requests.get(file_url, stream=True)
        response.raise_for_status()

        asns = set()
        for line in response.iter_lines():
            if line:
                decoded_line = line.decode('utf-8')
                try:
                    entry = json.loads(decoded_line)
                    asn = entry.get("asn")
                    if asn and is_valid_asn(str(asn)):
                        asns.add(str(asn))
                except (json.JSONDecodeError, TypeError):
                    pass

        save_asns_to_file(asns, output_file)

        print(f"ASNs extracted, sorted, and saved to {output_file}")

    except requests.exceptions.RequestException as e:
        print(f"Error downloading file: {e}")
