import requests
import re
from urllib.parse import urlparse

def extract_domain(url):
    try:
        parsed_url = urlparse(url)
        if parsed_url.netloc:
            return parsed_url.netloc
        elif "." in url:
            return url
        else:
            return None
    except Exception as e:
        print(f"Error parsing URL {url}: {e}")
        return None

def process_openphish_feed(input_file, output_file):
    try:
        response = requests.get(input_file, stream=True)
        response.raise_for_status()

        domains = set()

        for line in response.iter_lines(decode_unicode=True):
            if line:
                url = line.strip()
                domain = extract_domain(url)
                if domain:
                    domains.add(domain)

        with open(output_file, "w") as outfile:
            for domain in sorted(list(domains)):
                outfile.write(domain + "\n")

        print(f"Successfully processed {input_file} and saved to {output_file}")

    except requests.exceptions.RequestException as e:
        print(f"Error downloading {input_file}: {e}")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    input_file = "https://github.com/openphish/public_feed/raw/main/feed.txt"
    output_file = "opfeed.txt"
    process_openphish_feed(input_file, output_file)
