import requests

url = "https://raw.githubusercontent.com/MetaMask/eth-phishing-detect/main/src/config.json"

def extract_domains(output_file, key):
    try:
        response = requests.get(url)
        response.raise_for_status()

        data = response.json()

        domains = data.get(key, [])

        with open(output_file, "w") as file:
            for domain in domains:
                file.write(f"{domain}\n")

        print(f"Domains extracted and saved to {output_file}")

    except requests.RequestException as e:
        print(f"Error downloading the JSON file: {e}")
    except (KeyError, ValueError) as e:
        print(f"Error parsing the JSON file: {e}")

if __name__ == "__main__":
    extract_domains("allow.txt", "whitelist")
    extract_domains("phish.txt", "blacklist")