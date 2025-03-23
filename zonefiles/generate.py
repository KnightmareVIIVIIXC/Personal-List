import requests

def download_rfdfeed_lines(url, filename):
    try:
        response = requests.get(url, stream=True)
        response.raise_for_status()

        with open(filename, 'wb') as f:
            for line in response.iter_lines():
                if line:
                    f.write(line + b'\n')

        print(f"Successfully downloaded {url} and saved as {filename}")

    except requests.exceptions.RequestException as e:
        print(f"Error downloading {url}: {e}")
    except OSError as e:
        print(f"Error saving file {filename}: {e}")


if __name__ == "__main__":
    url = "https://zonefiles.io/f/compromised/domains/live/compromised_domains_live.txt"
    filename = "livefeed.txt"
    download_rfdfeed_lines(url, filename)