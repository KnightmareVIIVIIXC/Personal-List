import json
import requests
from urllib.parse import urlparse

def extract_domains(url, output_file):
    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()

        domains = set()

        for item in data:
            url_str = item.get('url', '')
            if url_str:
                parsed_url = urlparse(url_str)
                if parsed_url.netloc:
                    domains.add(parsed_url.netloc)

        with open(output_file, 'w', encoding='utf-8') as f: # added encoding='utf-8'
            for domain in sorted(domains):
                f.write(domain + '\n')

        print(f"Domains extracted and saved to {output_file}")

    except requests.exceptions.RequestException as e:
        print(f"Error fetching data: {e}")
    except json.JSONDecodeError as e:
        print(f"Error decoding JSON: {e}")
    except IOError as e:
        print(f"Error writing to file: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    url = "https://github.com/ProKn1fe/phishtank-database/raw/master/online-valid.json"
    output_file = "ptfeed.txt"
    extract_domains(url, output_file)