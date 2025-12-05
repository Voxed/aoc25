#include <algorithm>
#include <cstdint>
#include <iostream>
#include <print>
#include <sstream>
#include <string>
#include <vector>

using namespace std;

int main()
{
    string line;
    char _;
    
    vector<pair<uint64_t, uint64_t>> ranges;
    while (getline(cin, line))
    {
        if (line.empty())
            break;
        uint64_t start, end;
        stringstream(line) >> start >> _ >> end;
        end++;
        ranges.emplace_back(start, end);
    }
    sort(ranges.begin(), ranges.end());

    vector<uint64_t> ingredients;
    while (getline(cin, line))
        ingredients.emplace_back(stoll(line));

    println("{}", count_if(ingredients.begin(), ingredients.end(), [ranges](auto i) {
                return any_of(ranges.begin(), ranges.end(),
                              [i](auto range) { return range.first < i && i <= range.second; });
            }));

    uint64_t sum = 0;
    uint64_t cursor = 0;
    for (auto [start, end] : ranges)
    {
        if (cursor >= end)
            continue;
        sum += end - max(cursor, start);
        cursor = end;
    }
    println("{}", sum);
}