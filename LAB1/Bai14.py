denominations = [500, 200, 100, 50, 20, 10, 5, 2, 1]


def doi_tien():
    try:
        # Nhập số tiền X
        x = int(input("Nhập số tiền X: "))
        original_x = x

        results = []
        total_notes = 0

        # Thuật toán tham lam để tìm số tờ ít nhất
        for coin in denominations:
            count = x // coin  # Chia lấy nguyên để tìm số tờ
            results.append((coin, count))
            x %= coin  # Chia lấy dư để tính tiếp cho mệnh giá sau
            total_notes += count

        # In kết quả
        print(f"\nSo tien {original_x} duoc doi thanh:")
        for coin, count in results:
            print(f"Loai {coin} gom {count} to")

        print(f"TỔNG CỘNG CÓ {total_notes} TỜ")

    except ValueError:
        print("Vui lòng nhập một số nguyên hợp lệ!")


if __name__ == "__main__":
    doi_tien()