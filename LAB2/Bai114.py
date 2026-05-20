from math import gcd


def reverse_number(n: int) -> int:
    return int(str(n)[::-1])


def is_friendly_number(n: int) -> bool:
    reversed_n = reverse_number(n)
    return gcd(n, reversed_n) == 1


def main() -> None:
    try:
        a = int(input('Nhập a (10 ≤ a ≤ 30000): ').strip())
        b = int(input('Nhập b (a ≤ b ≤ 30000): ').strip())
    except ValueError:
        print('Vui lòng nhập số nguyên hợp lệ.')
        return

    if a < 10 or b > 30000 or a > b:
        print('Giá trị không hợp lệ. Đảm bảo 10 ≤ a ≤ b ≤ 30000.')
        return

    friendly_numbers = [n for n in range(a, b + 1) if is_friendly_number(n)]

    if friendly_numbers:
        print('Các số thân thiện trong khoảng từ', a, 'đến', b, 'là:')
        print(' '.join(str(n) for n in friendly_numbers))
    else:
        print('Không có số thân thiện trong khoảng này.')

    print('Số lượng:', len(friendly_numbers))


if __name__ == '__main__':
    main()
