@echo off

REM Compiling blocklists using hostlist-compiler:
call hostlist-compiler -c createpersonal.json -o personal_disallowed_domains.txt

REM Remove dead entries from personal list: call dead-domains-linter -i personal_disallowed_domains.txt --import=personaldead.txt --auto

REM Sort entries in personal_disallowed_domains:
python sortlist.py