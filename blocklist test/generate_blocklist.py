import os
import colorama
from colorama import Fore, Style

colorama.init(autoreset=True)

def update_hostlist():
    while True:
        replacements = []
        i = 10  # Start with 10 entries

        while i > 0:
            if i == 10:
                color = Fore.GREEN  # Green for 10 entries remaining
            elif i == 1:
                color = Fore.YELLOW  # Yellow for 1 entry remaining
            else:
                color = Fore.CYAN  # Cyan for entries 2 to 9

            print(f"{color}{i} entries remaining{Style.RESET_ALL}")

            replacement = input("Enter blocklist URL or local path: ")
            if replacement.lower() == 'r':
                i = 10
                replacements = []
                continue

            replacements.append(replacement)
            i -= 1

            if i == 0:
                break  # Stop after 1 entry

            more_replacements = input("Do you want to add more entries? (y)es / (n)o / (r)eset: ").lower()
            while more_replacements not in ('y', 'n', 'r', 'yes', 'no', 'reset'):
                print(Fore.RED + "Invalid input. Please enter 'y', 'n', or 'r'." + Style.RESET_ALL)
                more_replacements = input("Do you want to add more entries? (y)es / (n)o / (r)eset: ").lower()

            if more_replacements.startswith('r'):
                i = 10
                replacements = []
            elif more_replacements.startswith('n'):
                break

        command = "hostlist-compiler -i {} -o blocklist.txt".format(" -i ".join(replacements))
        os.system(command)

        repeat = input("Do you want to update the blocklist again? (y)es / (n)o: ").lower()
        while repeat not in ('y', 'n', 'yes', 'no'):
            print(Fore.RED + "Invalid input. Please enter 'y' or 'n'." + Style.RESET_ALL)
            repeat = input("Do you want to update the blocklist again? (y)es / (n)o: ").lower()
        if repeat.startswith('n'):
            break

if __name__ == "__main__":
    update_hostlist()
