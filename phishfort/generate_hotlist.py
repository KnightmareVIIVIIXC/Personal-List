import requests

# URL of the JSON file
url = "https://raw.githubusercontent.com/phishfort/phishfort-lists/master/blacklists/hotlist.json"

# Function to fetch and extract domain entries
def extract_domains(url):
    try:
        # Fetch the JSON data
        response = requests.get(url)
        response.raise_for_status()  # Raise an exception for 4xx/5xx status codes
        data = response.json()

        # Check if the data is a list
        if isinstance(data, list):
            # Extract domain entries
            domains = [entry for entry in data]
            return domains
        else:
            print("Data is not in the expected format.")
            return None
    except Exception as e:
        print("Error:", e)
        return None

# Function to save domains to a file
def save_to_file(domains, filename):
    try:
        with open(filename, "w", encoding="utf-8") as file:  # Specify encoding as UTF-8
            for domain in domains:
                file.write(domain + "\n")
        print("Domains saved to", filename)
    except Exception as e:
        print("Error saving to file:", e)

# Main function
def main():
    domains = extract_domains(url)
    if domains:
        save_to_file(domains, "hotlist_domains.txt")

if __name__ == "__main__":
    main()
