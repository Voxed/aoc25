time to burn some lifetime

### Python
python + powershell
```powershell
Get-Content <day>.<in|ex> | python <day>.py
```

### C#
dotnet + powershell
```powershell
Get-Content <day>.<in|ex> | dotnet run <day>.cs
```

### C++
clang + powershell
```powershell
clang <day>.<in|ex> -std=c++23; Get-Content input.txt | ./a.exe
```

cl + powershell
```powershell
cl <day>.<in|ex> /std:c++latest /Fe:a.exe /EHsc; Get-Content input.txt | ./a.exe
```