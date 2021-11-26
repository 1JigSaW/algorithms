#include <cassert>
#include <iostream>
#include <cstdint>

template <class Int>
Int gcd(Int a, Int b) {
    assert(a > 0 && b > 0);

    Int current_gcd = 1;
    for (Int d = 1; d * d <= a; d++) {
        if (a % d == 0) {
            if (b % d == 0) {
                current_gcd = d;
            }
            Int big_d = a / d;
            if (b % big_d == 0) {
                return big_d;
            }
        }
    }
    return current_gcd;
}

int main(void) {
    std::int64_t a, b;
    std::cin >> a >> b;
    std::cout << gcd(a, b) << std::endl;
}