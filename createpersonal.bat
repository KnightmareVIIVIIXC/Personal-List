@echo off

set GIT_PATH="%programfiles%\git\bin\bash.exe"
set CONFIG_PATH=C:\Users\Logan\Documents\GitHub\Personal-List

REM Push PhishFort repository: 
%GIT_PATH% %CONFIG_PATH%\pullphishfort.bat

REM Python script to download list from Phish Fort: 
python domain-only\generatephishfortlist.py

REM Python script to download hotlist from Phish Fort: 
python domain-only\generatephishforthotlist.py

REM Python script to download whitelist from Phish Fort: 
python domain-only\generatephishfortwhitelist.py

REM Push PhishFort repository:
%GIT_PATH% %CONFIG_PATH%\pushphishfort.bat

REM Update disconnectme lists: python disconnectme-pihole\update.py

REM Pull repository:
%GIT_PATH% %CONFIG_PATH%\pullrepo.bat

REM Update disallowed_clients:
call update_disallowed_clients.bat

REM Compiling blocklists using hostlist-compiler: 
call hostlist-compiler -c createpersonal.json -o personal_disallowed_domains.txt

REM Remove dead entries from personal list: call dead-domains-linter -i personal_disallowed_domains.txt --import=personaldead.txt --auto

REM Sort entries in personal_disallowed_domains:
python sortlist.py

REM Push repository:
%GIT_PATH% %CONFIG_PATH%\pushrepo.bat
