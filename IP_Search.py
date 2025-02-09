import requests
import re
import ipaddress
from colorama import init, Fore

init()


def check_ip_in_blocklist(source_url, target_ip):
    try:
        response = requests.get(source_url)
        response.raise_for_status()

        lines = [
            line.strip()
            for line in response.text.split("\n")
            if line.strip() and not line.startswith(("#", "!"))
        ]

        pattern = rf"(?:^|\s|\|){re.escape(target_ip)}(?:\s|/|#|$)"
        matches = [re.search(pattern, line, flags=re.MULTILINE) for line in lines]
        return any(matches)

    except requests.exceptions.RequestException as e:
        print(f"Error checking {source_url}: {e}")
        return False


def find_blocking_blocklists(target_ip, sources):
    blocking_blocklists = []

    for name, source in sources.items():
        if check_ip_in_blocklist(source, target_ip):
            blocking_blocklists.append(name)

    if blocking_blocklists:
        print(Fore.GREEN + f"IP '{target_ip}' found in the following sources:\n")
        for blocklist in blocking_blocklists:
            print(Fore.CYAN + f" - {blocklist}\n")
    else:
        print(Fore.RED + f"IP '{target_ip}' not found in any sources.")

    print(Fore.RESET, end="")


if __name__ == "__main__":
    blocklist_sources = {
        "Blocklist.de IP List": "https://lists.blocklist.de/lists/all.txt",
        "BlocklistProject Malware IP List": "https://raw.githubusercontent.com/blocklistproject/Lists/master/malware.ip",
        "C2-Tracker IP List": "https://raw.githubusercontent.com/montysecurity/C2-Tracker/main/data/all.txt",
        "CI-BadGuys IP List": "https://cinsscore.com/list/ci-badguys.txt",
        "DandelionSprout IP List": "https://raw.githubusercontent.com/DandelionSprout/adfilt/master/Alternate%20versions%20Anti-Malware%20List/Dandelion%20Sprout's%20and%20other%20adblocker%20lists'%20IPs.ipset",
        "Emerging Threats Compromised IP List": "https://rules.emergingthreats.net/blockrules/compromised-ips.txt",
        "GlobalAntiScamOrg IP List": "https://github.com/elliotwutingfeng/GlobalAntiScamOrg-blocklist/raw/main/global-anti-scam-org-scam-ips.txt",
        "Green Snow IP List": "https://blocklist.greensnow.co/greensnow.txt",
        "Hagezi TIF IP List": "https://raw.githubusercontent.com/hagezi/dns-blocklists/main/ips/tif.txt",
        "Phishing IP List": "https://malware-filter.gitlab.io/malware-filter/phishing-filter-dnscrypt-blocked-ips.txt",
        "RomainMarcoux Malware IP List 40K": "https://github.com/romainmarcoux/malicious-ip/raw/main/full-40k.txt",
        "RomainMarcoux Malware Outgoing-IP List 40K": "https://raw.githubusercontent.com/romainmarcoux/malicious-outgoing-ip/main/full-outgoing-ip-40k.txt",
        "ShadowWhisperer Hackers": "https://raw.githubusercontent.com/ShadowWhisperer/IPs/master/Malware/Hackers",
        "ShadowWhisperer Hackers_Old": "https://raw.githubusercontent.com/ShadowWhisperer/IPs/master/Malware/Hackers_Old",
        "ShadowWhisperer Hosting": "https://raw.githubusercontent.com/ShadowWhisperer/IPs/master/Malware/Hosting",
        "ShadowWhisperer Scanners": "https://raw.githubusercontent.com/ShadowWhisperer/IPs/master/Other/Scanners",
        "URLHaus IP List": "https://malware-filter.gitlab.io/malware-filter/urlhaus-filter-dnscrypt-blocked-ips.txt",
        "UT1 Malware IP List": "https://raw.githubusercontent.com/cbuijs/ut1/master/malware/ips.original",
        "UT1 Phishing IP List": "https://raw.githubusercontent.com/cbuijs/ut1/master/phishing/ips.original",
        "VN BadSites IP List": "https://malware-filter.gitlab.io/malware-filter/vn-badsite-filter-dnscrypt-blocked-ips.txt",
        "stamparm ipsum level 8": "https://raw.githubusercontent.com/stamparm/ipsum/master/levels/8.txt",
        "threatview.io IP Feed": "https://threatview.io/Downloads/IP-High-Confidence-Feed.txt",
    }

    while True:
        target_ip = input("Enter an IP address to find (or type 'exit' to close): ")

        if target_ip.lower() == "exit":
            print("Exiting the script.")
            break

        try:
            ipaddress.ip_address(target_ip)
        except ValueError:
            print(Fore.YELLOW + "Invalid IP address format.")
            print(Fore.RESET, end="")
            continue

        find_blocking_blocklists(target_ip, blocklist_sources)