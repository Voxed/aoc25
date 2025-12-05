#include <algorithm>
#include <cstdint>
#include <functional>
#include <iostream>
#include <print>
#include <ranges>
#include <span>
#include <string>
#include <vector>

using namespace std;
namespace views = std::ranges::views;

int main()
{
    string line;
    uint64_t p1 = 0, p2 = 0;
    while (getline(cin, line))
    {
        vector<char> bank;
        for (char c : line)
            bank.emplace_back(c - '0');

        function<uint64_t(span<char>, char)> jolt = [&](auto b, auto n) -> uint64_t {
            if (n < 0)
                return 0;
            auto m = ranges::max_element(b | views::take(b.size() - n));
            return *m * pow(10, n) + jolt(b | views::drop(distance(b.begin(), m) + 1), n - 1);
        };

        p1 += jolt(bank, 1);
        p2 += jolt(bank, 11);
    }
    std::println("{}\n{}", p1, p2);
}