#include <cassert>
#include <iostream>
#include <cstdint>

template <class Int>
Int gcd(Int a, Int b) {
    assert(a > 0 && b > 0);

    while (a > 0 && b > 0) {
        if (a > b) {
            a %= b;
        } else {
            b %= a;
        }
    }
    return a == 0 ? b : a;
}

int main(void) {
    std::int64_t a, b;
    std::cin >> a >> b;
    std::cout << gcd(a, b) << std::endl;
}