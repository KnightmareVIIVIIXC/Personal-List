import requests
import re
from colorama import init, Fore

init()


def check_domain_in_blocklist(source_url, target_domain):
    try:
        response = requests.get(source_url)
        response.raise_for_status()

        lines = [
            line.strip()
            for line in response.text.split("\n")
            if line.strip() and not line.startswith(("#", "!"))
        ]

        pattern = rf"(?:^|\s|\.|\|){re.escape(target_domain)}(?=\^|\#|\!|\s|$)"
        matches = [re.search(pattern, line, flags=re.MULTILINE) for line in lines]
        return any(matches)

    except requests.exceptions.RequestException as e:
        print(f"Error checking {source_url}: {e}")
        return False


def find_blocking_blocklists(target_domain, sources):
    blocking_blocklists = []

    for name, source in sources.items():
        if check_domain_in_blocklist(source, target_domain):
            blocking_blocklists.append(name)

    if blocking_blocklists:
        print(Fore.GREEN + f"Domain '{target_domain}' found in the following sources:\n")
        for blocklist in blocking_blocklists:
            print(Fore.CYAN + f" - {blocklist}\n")
    else:
        print(Fore.RED + f"Domain '{target_domain}' not found in any sources.")

    print(Fore.RESET, end="")


if __name__ == "__main__":
    blocklist_sources = {
        "Cert.pl": "https://github.com/AdguardTeam/HostlistsRegistry/raw/main/filters/regional/filter_41_POL_CERTPolskaListOfMaliciousDomains/filter.txt",
        "MetaMask Phishing": "https://raw.githubusercontent.com/KnightmareVIIVIIXC/Personal-List/main/metamask/phishing.txt",
        "NRD 14 Day": "https://github.com/xRuffKez/NRD/raw/main/lists/14-day_phishing/domains-only/nrd-phishing-14day.txt",
        "NRD 30 Day": "https://github.com/xRuffKez/NRD/raw/main/lists/30-day_phishing/domains-only/nrd-phishing-30day.txt",
        "OpenPhish": "https://github.com/invisiblethreat/openphish-pihole/raw/main/openphish.txt",
        "PhishFort Phishing": "https://raw.githubusercontent.com/KnightmareVIIVIIXC/Personal-List/main/phishfort/phishing_domains.txt",
        "PhishTank": "https://github.com/Zaczero/pihole-phishtank/raw/main/hosts.txt",
        "Phishing Army": "https://github.com/AdguardTeam/HostlistsRegistry/raw/main/filters/security/filter_18_PhishingArmy/filter.txt",
        "Phishing Database Active": "https://github.com/Phishing-Database/Phishing.Database/raw/master/phishing-domains-ACTIVE.txt",
        "Phishing Database New Last Hour": "https://github.com/Phishing-Database/Phishing.Database/raw/master/phishing-domains-NEW-last-hour.txt",
        "Phishing Database New Today": "https://github.com/Phishing-Database/Phishing.Database/raw/master/phishing-domains-NEW-today.txt",
        "Phishing Sinking Yachts": "https://phish.sinking.yachts/v2/text",
        "Phishing URLs": "https://github.com/AdguardTeam/HostlistsRegistry/raw/main/filters/security/filter_30_PhishingURLBlocklist/filter.txt",
        "RPiList Phishing": "https://github.com/RPiList/specials/raw/master/Blocklisten/Phishing-Angriffe",
        "blocklistproject Phishing": "https://github.com/blocklistproject/Lists/raw/master/phishing.txt",
        "chainapsis Phishing Blocklist": "https://github.com/chainapsis/phishing-block-list/raw/main/block-list.txt",
        "validin-phish-feed": "https://github.com/MikhailKasimov/validin-phish-feed/raw/main/validin-phish-feed.txt",
        "validin-phish-feed-1": "https://github.com/MikhailKasimov/validin-phish-feed/raw/main/validin-phish-feed-1.txt",
    }

    while True:
        target_domain = input("Enter a domain to find (or type 'exit' to close): ")

        if target_domain.lower() == "exit":
            print("Exiting the script.")
            break

        if (
            "." not in target_domain
            or target_domain.startswith(".")
            or target_domain.endswith(".")
            or ".." in target_domain
        ):
            print(Fore.YELLOW + "Invalid domain")
            print(Fore.RESET, end="")
            continue

        find_blocking_blocklists(target_domain, blocklist_sources)
