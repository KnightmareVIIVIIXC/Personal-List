import requests
import json

# URL to download the JSON file
url = "https://raw.githubusercontent.com/MetaMask/eth-phishing-detect/main/src/config.json"

# Output file
output_file = "phishing.txt"

try:
    # Download the JSON file
    response = requests.get(url)
    response.raise_for_status()  # Raise an HTTPError for bad responses (4xx and 5xx)

    # Parse the JSON content
    data = response.json()

    # Extract domains from the blacklist section
    blacklist = data.get("blacklist", [])

    # Write the domains to the output file
    with open(output_file, "w") as file:
        for domain in blacklist:
            file.write(f"{domain}\n")

    print(f"Domains extracted and saved to {output_file}")

except requests.RequestException as e:
    print(f"Error downloading the JSON file: {e}")
except (json.JSONDecodeError, KeyError) as e:
    print(f"Error parsing the JSON file: {e}")
