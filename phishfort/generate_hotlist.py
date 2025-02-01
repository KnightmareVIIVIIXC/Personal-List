import requests

url = "https://raw.githubusercontent.com/phishfort/phishfort-lists/master/blacklists/hotlist.json"

def extract_domains(url):
    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()

        if isinstance(data, list):
            domains = [entry for entry in data]
            return domains
        else:
            print("Data is not in the expected format.")
            return None
    except Exception as e:
        print("Error:", e)
        return None

def save_to_file(domains, filename):
    try:
        with open(filename, "w", encoding="utf-8") as file:
            for domain in domains:
                file.write(domain + "\n")
        print("Domains saved to", filename)
    except Exception as e:
        print("Error saving to file:", e)

def main():
    domains = extract_domains(url)
    if domains:
        save_to_file(domains, "hotlist_domains.txt")

if __name__ == "__main__":
    main()