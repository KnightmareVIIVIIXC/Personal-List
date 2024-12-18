import os
import json
import requests
import msvcrt


def get_api_key():
    with open("config.json") as f:
        config = json.load(f)
    return config.get("virustotal_api_key")


def get_subdomains(domain, api_key):
    url = f"https://www.virustotal.com/vtapi/v2/domain/report"
    params = {"apikey": api_key, "domain": domain}
    response = requests.get(url, params=params)
    data = response.json()

    subdomains = data.get("subdomains", [])
    return subdomains


def save_subdomains_to_file(domain, subdomains):
    if not os.path.exists("Results"):
        os.makedirs("Results")
    filename = os.path.join("Results", f"{domain}_subdomains.txt")
    with open(filename, "w") as f:
        for subdomain in subdomains:
            f.write(subdomain + "\n")
    print(f"Subdomains saved to {filename}")


if __name__ == "__main__":
    while True:
        domain = input("Enter the domain: ")
        api_key = get_api_key()

        if api_key:
            subdomains = get_subdomains(domain, api_key)

            if subdomains:
                save_subdomains_to_file(domain, subdomains)
            else:
                print(f"No subdomains found for {domain} or API limit reached.")
        else:
            print("API key not found. Please check your configuration.")

        print("\nPress 'Enter' to enter another domain or any other key to exit...")
        char = msvcrt.getch()
        if char != b"\r":  # If the pressed key is not 'Enter'
            break  # Exit the loop
