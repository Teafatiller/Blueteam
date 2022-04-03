$InputFile = 'C:\Users\Administrator\Desktop\users.txt'
write—host "removing traillng space.. of f11e $InputFi1e"
$content = Get-Content $InputFile
$content I Foreach {$_.TrimEnd()} | Set-Content users.txt
write-host ""
(gc users.txt) | ? {$_.trim() -ne "" } | set-content users.txt
write-host "Remove Admin and backup admins from file manually!"
