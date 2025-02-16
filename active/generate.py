import requests

def download_and_merge(urls, output_file):
    try:
        all_domains = set()

        for url in urls:
            try:
                response = requests.get(url, stream=True)
                response.raise_for_status()

                for line in response.iter_lines():
                    if line:
                        domain = line.decode('utf-8').strip()
                        if not domain.startswith("#") and not domain.startswith("!"):
                            all_domains.add(domain)

            except requests.exceptions.RequestException as e:
                print(f"Error downloading {url}: {e}")
                continue

        with open(output_file, 'w') as f:
            for domain in sorted(list(all_domains)):
                f.write(domain + '\n')

        print(f"Successfully downloaded and merged into {output_file}")

    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    urls = [
        "https://github.com/xRuffKez/NRD/raw/main/lists/30-day_phishing/domains-only/nrd-phishing-30day.txt",
        "https://github.com/Phishing-Database/Phishing.Database/raw/master/phishing-domains-ACTIVE.txt",
        "https://github.com/Phishing-Database/Phishing.Database/raw/master/phishing-domains-NEW-last-hour.txt",
        "https://github.com/Phishing-Database/Phishing.Database/raw/master/phishing-domains-NEW-today.txt",
    ]
    output_file = "activephish.txt"
    download_and_merge(urls, output_file)