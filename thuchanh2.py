# Chương trình tìm n nhỏ nhất bằng cách trừ n cho tổng các chữ số của nó

n = int(input("Nhập số dương n: "))

while True:
    # Tính tổng các chữ số của n
    digit_sum = sum(int(digit) for digit in str(n))
    
    # Tính n mới bằng cách trừ n cho tổng chữ số
    new_n = n - digit_sum
    
    # Nếu kết quả <= 0, dừng lại
    if new_n <= 0:
        break
    
    # Cập nhật n
    n = new_n

print(f"Kết quả: n = {n}")
