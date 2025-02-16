import requests

def download_feed(url, filename):
    try:
        response = requests.get(url, stream=True)
        response.raise_for_status()

        with open(filename, 'wb') as f:
            for chunk in response.iter_content(chunk_size=8192):
                f.write(chunk)

        print(f"Successfully downloaded {url} and saved as {filename}")

    except requests.exceptions.RequestException as e:
        print(f"Error downloading {url}: {e}")
    except OSError as e:
        print(f"Error saving file {filename}: {e}")


if __name__ == "__main__":
    url = "https://dl.red.flag.domains/red.flag.domains.txt"
    filename = "rfdfeed.txt"
    download_feed(url, filename)