

kiem_tra_boi_so = lambda n: (n % 13 == 0) or (n % 19 == 0) # Hàm lambda nhận 1 đối số n, chia lấy dư (%) cho 13 và 19
# Nếu bằng 0 thì nó là bội số.

n = int(input("Nhập số nguyên n: "))

if kiem_tra_boi_so(n):
    print(f"=> {n} LÀ bội số của 13 hoặc 19.")
else:
    print(f"=> {n} KHÔNG PHẢI là bội số của 13 hoặc 19.")

print("\n" + "="*60 + "\n") 



kiem_tra_tam_giac = lambda a, b, c: (
    "KHÔNG phải là 3 cạnh của một tam giác hợp lệ" 
    if not (a + b > c and a + c > b and b + c > a) else #Kiểm tra tổng 2 cạnh có lớn hơn cạnh còn lại không.
    (
        "Tam giác đều" if a == b == c else 
        "Tam giác vuông cân" if (a*a + b*b == c*c or a*a + c*c == b*b or b*b + c*c == a*a) and (a == b or b == c or a == c) else
        "Tam giác vuông" if (a*a + b*b == c*c or a*a + c*c == b*b or b*b + c*c == a*a) else
        "Tam giác cân" if (a == b or b == c or a == c) else
        "Tam giác thường"
    ) #Nếu hợp lệ thì mới kiểm tra đều, vuông cân, vuông, cân, thường
)

print("--- KIỂM TRA VÀ PHÂN LOẠI TAM GIÁC ---")
a, b, c = map(int, input("Nhập 3 số nguyên a, b, c (cách nhau bởi dấu phẩy): ").split(","))

ket_qua = kiem_tra_tam_giac(a, b, c)
print(f"=> Kết quả: 3 cạnh ({a}, {b}, {c}) là {ket_qua}")
