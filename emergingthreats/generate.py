import requests

def process_hosts_file(url):
    try:
        response = requests.get(url, stream=True)
        response.raise_for_status()

        domains = []
        for line in response.iter_lines(decode_unicode=True):
            line = line.strip()
            if line and not line.startswith("#"):
                parts = line.split()
                if len(parts) > 1:
                    domain = parts[1]
                    domains.append(domain)

        return domains

    except requests.exceptions.RequestException as e:
        print(f"Error downloading file: {e}")
        return None
    except Exception as e:
        print(f"An error occurred: {e}")
        return None

def write_domains_to_file(domains, output_filename="malicious_domains.txt"):
    if domains is None:
      return

    try:
        with open(output_filename, "w") as f:
            for domain in domains:
                f.write(domain + "\n")
        print(f"Domains written to {output_filename}")
    except Exception as e:
        print(f"Error writing to file: {e}")

if __name__ == "__main__":
    url = "https://hosts.tweedge.net/malicious.txt"
    domains = process_hosts_file(url)

    if domains is not None:
        write_domains_to_file(domains)