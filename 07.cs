using System.Numerics;

var world = Console
    .In.ReadToEnd()
    .ReplaceLineEndings()
    .TrimEnd(Environment.NewLine.ToCharArray())
    .Split(Environment.NewLine)
    .Select(l => l.ToCharArray())
    .ToArray();

Dictionary<(int, int), BigInteger> cache = new();
HashSet<(int, int)> hitSplitters = new();

BigInteger tl(int x, int y)
{
    if (y + 1 < world.Length)
        if (cache.ContainsKey((x, y)))
            return cache[(x, y)];
        else
        {
            BigInteger result = 0;
            switch (world[y + 1][x])
            {
                case '.':
                    result = tl(x, y + 1);
                    cache[(x, y)] = result;
                    return result;
                case '^':
                    hitSplitters.Add((x, y + 1));
                    result = tl(x - 1, y + 1) + tl(x + 1, y + 1) + 1;
                    cache[(x, y)] = result;
                    return result;
            }
        }
    return 0;
}

BigInteger numTimelines = 0;
_ = world
    .Select(
        (r, y) =>
            r.Select(
                    (e, x) =>
                    {
                        if (e == 'S')
                        {
                            numTimelines = tl(x, y) + 1;
                        }
                        return 0;
                    }
                )
                .ToArray()
    )
    .ToList();

Console.WriteLine(hitSplitters.ToArray().Length);
Console.WriteLine(numTimelines);
