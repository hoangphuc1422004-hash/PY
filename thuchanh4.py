# Nhập hai số nguyên a và b trên cùng một dòng, cách nhau bởi khoảng trắng
# Giải phương trình bậc 1: ax + b = 0

try:
    values = input().strip().split()
    if len(values) < 2:
        raise ValueError("Cần nhập ít nhất hai số nguyên a và b.")
    a, b = int(values[0]), int(values[1])
except Exception as e:
    print(e)
    raise SystemExit(1)

if a == 0:
    if b == 0:
        print("Phương trình có vô số nghiệm")
    else:
        print("Phương trình vô nghiệm")
else:
    x = -b / a
    if x.is_integer():
        x = int(x)
    print(x)
