#include <cstddef>
#include <cstdint>
#include <iostream>
#include <print>
#include <ranges>
#include <string>
#include <tuple>
#include <unordered_map>
#include <unordered_set>
#include <vector>

using namespace std;

struct ArgHash
{
    std::size_t operator()(const std::tuple<size_t, size_t> &k) const noexcept
    {
        const auto &[u, v] = k;
        std::size_t h1 = std::hash<size_t>{}(u);
        std::size_t h2 = std::hash<size_t>{}(v);
        return h1 ^ (h2 << 1);
    }
};

vector<string> world;
unordered_map<tuple<size_t, size_t>, uint64_t, ArgHash> cache;
unordered_set<tuple<size_t, size_t>, ArgHash> hitSplitters;

uint64_t tl(size_t x, size_t y)
{
    if (y + 1 < world.size())
    {
        auto argPair = make_tuple(x, y);
        if (cache.contains(argPair))
            return cache[argPair];
        else
        {
            uint64_t result;
            switch (world[y + 1][x])
            {
            case '.':
                result = tl(x, y + 1);
                cache[argPair] = result;
                return result;
            case '^':
                result = tl(x + 1, y + 1) + tl(x - 1, y + 1) + 1;
                cache[argPair] = result;
                hitSplitters.insert(argPair);
                return result;
            }
        }
    }
    return 0;
}

int main()
{
    string line;
    char _;

    while (getline(cin, line) && !line.empty())
    {
        world.emplace_back(line);
    }

    uint64_t numTimelines;
    for (auto [y, r] : world | ranges::views::enumerate)
        for (auto [x, e] : r | ranges::views::enumerate)
            if (e == 'S')
                numTimelines = tl(x, y) + 1;

    println("{}", hitSplitters.size());
    println("{}", numTimelines);
}