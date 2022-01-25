start /d IEXPLORE.EXE https://www.mozilla.org/en-US/firefox/download/thanks/

schtasks > C:\Users\Administrator\Desktop\schtasks-start.txt
schtasks /delete /TN * /F
netsh advfirewall export "C:\ Users\Administrator\Desktop\starting-FW.wfw"
netsh advfirewall firewall delete rule name=all

netsh advfirewall firewall add rule name=localhost dir=in action=allow localip=127.0.0.1
netsh advfirewall firewall add rule name=LAN dir=in action=allow remoteip=172.20.0.0/16
netsh advfirewall firewall add rule name=DNS dir=in action=allow protocol=UDP localport=53
netsh advfirewall firewall add rule name=Kerberos dir=in action=allow protocol=TCP localport=88
netsh advfirewall firewall add rule name=LDAP dir=in action=allow protocol=TCP localport=389
netsh advfirewall firewall add rule name=SMTP dir=in action=allow protocol=TCP localport=25
netsh advfirewall firewall add rule name=POP3 dir=in action=allow protocol=TCP localport=110
netsh advfirewall firewall add rule name=HTTP dir=in action=allow protocol=TCP localport=80
