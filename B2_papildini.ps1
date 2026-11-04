Write-Host "Sākam eksportu"
Get-PSDrive -PSProvider FileSystem | Select-Object Name, Used, Free | Export-Csv -Path diski.csv -NoTypeInformation -Delimiter ";" -Encoding UTF8
 
