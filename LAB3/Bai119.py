from math import isqrt

REGULAR_PAIRS = [('0', '0'), ('1', '1'), ('6', '9'), ('8', '8'), ('9', '6')]
EXTENDED_PAIRS = REGULAR_PAIRS + [('2', '2'), ('5', '5')]
REGULAR_MID = ['0', '1', '8']
EXTENDED_MID = ['0', '1', '2', '5', '8']


def generate_strobogrammatic(n: int, final_length: int, extended: bool = False) -> list[str]:
    if n == 0:
        return ['']
    if n == 1:
        return EXTENDED_MID[:] if extended else REGULAR_MID[:]

    pairs = EXTENDED_PAIRS if extended else REGULAR_PAIRS
    middles = generate_strobogrammatic(n - 2, final_length, extended)
    result = []
    for middle in middles:
        for left, right in pairs:
            if n == final_length and left == '0':
                continue
            result.append(left + middle + right)
    return result


def strobogrammatic_numbers_under(limit: int, extended: bool = False) -> list[int]:
    result = []
    max_len = len(str(limit - 1))
    for length in range(1, max_len + 1):
        for s in generate_strobogrammatic(length, length, extended):
            value = int(s)
            if value < limit:
                result.append(value)
    return sorted(result)


def is_prime(n: int) -> bool:
    if n < 2:
        return False
    if n in (2, 3):
        return True
    if n % 2 == 0:
        return False
    limit = isqrt(n)
    for i in range(3, limit + 1, 2):
        if n % i == 0:
            return False
    return True


def strobogrammatic_transform(num: int) -> int | None:
    mapping = {'0': '0', '1': '1', '6': '9', '8': '8', '9': '6'}
    s = str(num)
    transformed = []
    for ch in reversed(s):
        if ch not in mapping:
            return None
        transformed.append(mapping[ch])
    return int(''.join(transformed))


def non_strobo_nonprime_but_transformed_prime(limit: int) -> list[int]:
    result = []
    for n in range(1, limit):
        if n < 2:
            continue
        if is_prime(n):
            continue
        transformed = strobogrammatic_transform(n)
        if transformed is None:
            continue
        if transformed != n and is_prime(transformed):
            result.append(n)
    return result


def main() -> None:
    limit = 1_000_000
    regular = strobogrammatic_numbers_under(limit)
    extended = strobogrammatic_numbers_under(limit, extended=True)

    print('a) Các số strobogrammatic nhỏ hơn 1.000.000:')
    print(', '.join(str(n) for n in regular))
    print('\nTổng số:', len(regular))

    regular_primes = [n for n in regular if is_prime(n)]
    print('\nb) Các số nguyên tố strobogrammatic nhỏ hơn 1.000.000:')
    print(', '.join(str(n) for n in regular_primes))
    print('Tổng số:', len(regular_primes))

    print('\nc) Các số strobogrammatic mở rộng nhỏ hơn 1.000.000:')
    print(', '.join(str(n) for n in extended))
    print('Tổng số:', len(extended))

    extended_primes = [n for n in extended if is_prime(n)]
    print('\nd) Các số nguyên tố strobogrammatic mở rộng nhỏ hơn 1.000.000:')
    print(', '.join(str(n) for n in extended_primes))
    print('Tổng số:', len(extended_primes))

    special = non_strobo_nonprime_but_transformed_prime(limit)
    print('\ne) Các số < 1.000.000 không phải strobogrammatic và không phải nguyên tố, nhưng số strobogrammatic của số này là nguyên tố:')
    print(', '.join(str(n) for n in special))
    print('Tổng số:', len(special))


if __name__ == '__main__':
    main()
