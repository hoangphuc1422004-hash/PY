from typing import Iterable

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


def strobogrammatic_n_digits(n: int, extended: bool = False) -> list[int]:
    return [int(s) for s in generate_strobogrammatic(n, n, extended)]


def print_numbers(label: str, numbers: Iterable[int]) -> None:
    print(label)
    print(', '.join(str(x) for x in numbers))
    print('Tổng số:', len(numbers))
    print()


def main() -> None:
    try:
        n = int(input('Nhập số nguyên n (2 ≤ n ≤ 10): ').strip())
    except ValueError:
        print('Giá trị không hợp lệ. Vui lòng nhập một số nguyên.')
        return

    if n < 2 or n > 10:
        print('Giá trị không hợp lệ. n phải nằm trong khoảng 2 đến 10.')
        return

    regular = strobogrammatic_n_digits(n)
    extended = strobogrammatic_n_digits(n, extended=True)

    print_numbers(f'a) Các số strobogrammatic gồm {n} chữ số:', regular)
    print_numbers(f'b) Các số strobogrammatic mở rộng gồm {n} chữ số:', extended)


if __name__ == '__main__':
    main()
