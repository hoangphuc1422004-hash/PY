def giai_quyet_doi_tien(so_tien):
    denominations = [500, 200, 100, 50, 20, 10, 5, 2, 1]
    total_notes = 0
    count_types = 0

    print(f"\nSo tien {so_tien} duoc doi thanh:")

    for coin in denominations:
        count = so_tien // coin
        if count > 0:
            print(f"Loai {coin} gom {count} to")
            total_notes += count
            count_types += 1
        so_tien %= coin

    print(f"TỔNG CỘNG CÓ {total_notes} TỜ")
    print(f"Tong so loai = {count_types}")


def main():
    try:

        a = int(input("Nhap so tien hang can tra (a): "))
        b = int(input("Nhap so tien khach thuc te tra (b): "))

        if a > b:
            print(f"So tien khach hang con thieu la: {a - b}")
        elif a == b:
            print("Cám ơn khách hàng. Hẹn gặp lại")
        else:
            # Truong hop a < b: can thoi tien
            tien_thua = b - a
            print(f"So tien thua can thoi lai: {tien_thua}")

            # Goi ham doi tien cho so tien thua
            giai_quyet_doi_tien(tien_thua)

            input("\nNhan Enter de ket thuc...")
            print("Cám ơn khách hàng. Hẹn gặp lại")

    except ValueError:
        print("Lỗi: Vui lòng nhập số nguyên hợp lệ!")


if __name__ == "__main__":
    main()