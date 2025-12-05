List<List<int>> l = new();
while (Console.ReadLine()?.Select(c=>c-'0').ToList() is List<int> b) l.Add(b);
double f(List<int> b, int n)
{
    if(n < 0) return 0;
    var m = b[..^n].Max();
    return m*Math.Pow(10,n)+f(b[(b.IndexOf(m)+1)..],n-1);
} 
foreach(var p in new[]{1,11}) Console.WriteLine(l.Select(l=>f(l,p)).Sum());