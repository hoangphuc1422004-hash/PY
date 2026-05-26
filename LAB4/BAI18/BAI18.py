python BAI18.py --start 1 --end 100000 --type so_phong_phuimport argparse
import math

# Bài 18: Các hàm ẩn danh kiểm tra các loại số
# Mỗi predicate dưới đây là một lambda trả về True/False.
# Sau đó dùng các hàm này để lập danh sách số thỏa điều kiện trong một khoảng.

PREDICATES = {
    'so_than_thien': lambda n: math.gcd(n, int(str(n)[::-1])) == 1,
    'so_chinh_phuong': lambda n: math.isqrt(n) ** 2 == n,
    'so_dong_nhat': lambda n: len({*str(n)}) == 1,
    'so_hoan_thien': lambda n: (
        sum(
            d + (n // d if d != n // d else 0)
            for d in range(1, math.isqrt(n) + 1)
            if n % d == 0
        ) - n
    ) == n,
    'so_phong_phu': lambda n: (
        sum(
            d + (n // d if d != n // d else 0)
            for d in range(1, math.isqrt(n) + 1)
            if n % d == 0
        ) - n
    ) > n,
    'so_tang_dan': lambda n: all(a <= b for a, b in zip(str(n), str(n)[1:])),
    'so_armstrong': lambda n: sum(int(d) ** len(str(n)) for d in str(n)) == n,
    'so_nguyen_to': lambda n: n > 1 and all(n % d for d in range(2, math.isqrt(n) + 1)),
    'so_palindrome': lambda n: (s := str(n)) == s[::-1],
    'so_nguyen_to_palindrome': lambda n: (
        n > 1
        and (s := str(n)) == s[::-1]
        and all(n % d for d in range(2, math.isqrt(n) + 1))
    ),
    'so_loc_phat': lambda n: set(str(n)) <= {'6', '8'},
    'so_loc_phat_palindrome': lambda n: set(str(n)) <= {'6', '8'} and (s := str(n)) == s[::-1],
}

LABELS = {
    'so_than_thien': 'Số thân thiện',
    'so_chinh_phuong': 'Số chính phương',
    'so_dong_nhat': 'Số đồng nhất',
    'so_hoan_thien': 'Số hoàn thiện',
    'so_phong_phu': 'Số phong phú',
    'so_tang_dan': 'Số tăng dần',
    'so_armstrong': 'Số Armstrong',
    'so_nguyen_to': 'Số nguyên tố',
    'so_palindrome': 'Số palindrome',
    'so_nguyen_to_palindrome': 'Số nguyên tố palindrome',
    'so_loc_phat': 'Số lộc phát',
    'so_loc_phat_palindrome': 'Số lộc phát palindrome',
}


def find_numbers(predicate, start, end):
    return [n for n in range(start, end + 1) if predicate(n)]


def print_results(name, predicate, start, end, max_display=100, print_all=False):
    matches = find_numbers(predicate, start, end)
    print('=' * 60)
    print(f"{LABELS.get(name, name)}: {len(matches)} số trong khoảng [{start}, {end}]")
    if not matches:
        print('Không có số thỏa điều kiện.')
        return
    if print_all:
        print('Danh sách đầy đủ:')
        print(', '.join(str(n) for n in matches))
    else:
        print(f"{min(len(matches), max_display)} số đầu tiên:")
        print(', '.join(str(n) for n in matches[:max_display]))
        if len(matches) > max_display:
            print(f"... (còn {len(matches) - max_display} số khác)")


def parse_arguments():
    parser = argparse.ArgumentParser(
        description='BAI18: Kiểm tra và in các loại số theo predicate lambda.'
    )
    parser.add_argument(
        '--start', type=int, default=1,
        help='Giá trị bắt đầu của khoảng (mặc định 1).'
    )
    parser.add_argument(
        '--end', type=int, default=100000,
        help='Giá trị kết thúc của khoảng (mặc định 100000).'
    )
    parser.add_argument(
        '--type', choices=list(PREDICATES), default=None,
        help='Loại số cần in. Nếu không chỉ định thì in tất cả.'
    )
    parser.add_argument(
        '--print-all', action='store_true',
        help='In toàn bộ các số thỏa điều kiện thay vì chỉ in vài số đầu.'
    )
    parser.add_argument(
        '--max-display', type=int, default=50,
        help='Số lượng số đầu tiên hiển thị khi không dùng --print-all.'
    )
    return parser.parse_args()


def main():
    args = parse_arguments()
    if args.start < 1 or args.end < args.start:
        raise ValueError('Khoảng phải thỏa 1 <= start <= end.')

    selected = [args.type] if args.type else list(PREDICATES.keys())
    for name in selected:
        print_results(
            name,
            PREDICATES[name],
            args.start,
            args.end,
            max_display=args.max_display,
            print_all=args.print_all,
        )
    print('=' * 60)


if __name__ == '__main__':
    main()
