call python spamasnlist.py
call hostlist-compiler -c litedisallowedclients.json -o lite_disallowed_clients.txt
call hostlist-compiler -c disallowedclients.json -o dns_disallowed_clients.txt
call hostlist-compiler -c asnclientmerge.json -o asnclientmerge.txt