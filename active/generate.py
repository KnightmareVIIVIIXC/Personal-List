import requests

def process_file(url):
    try:
        response = requests.get(url)
        response.raise_for_status()
        domains = set()
        content = response.text
        for line in content.splitlines():
            line = line.strip()
            if line and not line.startswith("#") and not line.startswith("!"):
                parts = line.split()
                domain = parts[0] if len(parts) >= 1 else None
                if len(parts) > 1:
                    domain = parts[1]
                if domain:
                    domains.add(domain)
        return domains
    except requests.exceptions.RequestException as e:
        print(f"Error downloading file: {e}")
        return None
    except Exception as e:
        print(f"An error occurred: {e}")
        return None

def write_domains_to_file(domains, output_filename="activephish.txt"):
    if domains is None:
        return
    try:
        with open(output_filename, "w") as f:
            for domain in sorted(list(domains)):
                f.write(domain + "\n")
        print(f"Domains written to {output_filename}")
    except Exception as e:
        print(f"Error writing to file: {e}")

if __name__ == "__main__":
    urls = [
        "https://zonefiles.io/f/compromised/domains/live/compromised_domains_live.txt",
        "https://hosts.tweedge.net/malicious.txt",
        "https://github.com/xRuffKez/NRD/raw/main/lists/30-day_phishing/domains-only/nrd-phishing-30day.txt",
    ]
    all_domains = set()
    for url in urls:
        domains = process_file(url)
        if domains is None:
            break
        all_domains.update(domains)
    if all_domains:
        write_domains_to_file(all_domains)