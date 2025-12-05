using System.Numerics;

var chunks = Console
    .In.ReadToEnd()
    .ReplaceLineEndings()
    .TrimEnd(Environment.NewLine.ToCharArray())
    .Split(Environment.NewLine + Environment.NewLine);

var ranges = (
    from line in chunks[0].Split(Environment.NewLine)
    let range = line.Split("-").Select(BigInteger.Parse)
    orderby range.First()
    select (Start: range.First(), End: range.Last() + 1)
).ToList();

// Part 1
Console.WriteLine(
    chunks[1]
        .Split(Environment.NewLine)
        .Select(BigInteger.Parse)
        .Count(i => ranges.Any(r => r.Start < i && i <= r.End))
);

// Part 2
BigInteger sum = 0;
BigInteger cursor = 0;
foreach (var (start, end) in ranges)
{
    if (cursor >= end)
        continue;
    sum += end - BigInteger.Max(cursor, start);
    cursor = end;
}
Console.WriteLine(sum);
