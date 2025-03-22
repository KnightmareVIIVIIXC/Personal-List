import requests
from urllib.parse import urlparse

def extract_domain(url):
    try:
        parsed_url = urlparse(url)
        if parsed_url.netloc:
            return parsed_url.netloc
        else:
            return None
    except ValueError:
        return None
    except TypeError:
        return None

def process_urlabuse_feed(input_file, output_file):
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

        with open(output_file, "w", encoding="utf-8") as outfile:
            for domain in sorted(list(domains)):
                outfile.write(domain + "\n")

        print(f"Successfully processed {input_file} and saved to {output_file}")

    except requests.exceptions.RequestException as e:
        print(f"Error downloading {input_file}: {e}")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    input_file = "https://urlabuse.com/public/data/phishing_url.txt"
    output_file = "uaphishing.txt"
    process_urlabuse_feed(input_file, output_file)