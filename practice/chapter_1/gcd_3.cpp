#include <cassert>
#include <iostream>
#include <cstdint>

template <class Int>
Int gcd(Int a, Int b) {
    assert(a > 0);

    if (b > 0) {
        return gcd(b, a % b);
    }
    return a;
}

int main(void) {
    std::int64_t a, b;
    std::cin >> a >> b;
    std::cout << gcd(a, b) << std::endl;
}