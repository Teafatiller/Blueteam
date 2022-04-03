$users = Get-Content -path C:\Users\Administrator\Desktop\users.txt
foreach($user in $users)
{
$Password = ConvertTo—SecureString "Password123!" -AsP1ainText -Force
Set-LocalUser -Name $user -Password $Password
}
