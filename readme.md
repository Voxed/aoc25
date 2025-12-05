time to burn some lifetime

### Python
python + powershell
```powershell
Get-Content input.txt | python <day>.py
```

### C#
dotnet + powershell
```powershell
Get-Content input.txt | dotnet run <day>.cs
```

### C++
clang + powershell
```powershell
clang <day>.cc -std=c++23; Get-Content input.txt | ./a.exe
```

cl + powershell
```powershell
cl <day>.cc /std:c++latest /Fe:a.exe /EHsc; Get-Content input.txt | ./a.exe
```