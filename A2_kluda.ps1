Get-Process | Sort-Object CPU -Descending | Select-Object -First 5 Id, ProcessName, CPU
