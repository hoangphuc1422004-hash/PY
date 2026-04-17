# Nhập ba số nguyên a, b, c trên cùng một dòng, cách nhau bởi khoảng trắng
# Giải phương trình bậc 2: ax^2 + bx + c = 0

try:
    values = input().strip().split()
    if len(values) < 3:
        raise ValueError("Cần nhập ba số nguyên a, b, c.")
    a, b, c = int(values[0]), int(values[1]), int(values[2])
except Exception as e:
    print(e)
    raise SystemExit(1)

if a == 0:
    # Trở về phương trình bậc 1 bx + c = 0
    if b == 0:
        if c == 0:
            print("Phương trình có vô số nghiệm")
        else:
            print("Phương trình vô nghiệm")
    else:
        x = -c / b
        if x.is_integer():
            x = int(x)
        print(x)
else:
    delta = b * b - 4 * a * c
    if delta < 0:
        print("Phương trình vô nghiệm")
    elif delta == 0:
        x = -b / (2 * a)
        if x.is_integer():
            x = int(x)
        print(x)
    else:
        sqrt_delta = delta ** 0.5
        x1 = (-b + sqrt_delta) / (2 * a)
        x2 = (-b - sqrt_delta) / (2 * a)
        if x1.is_integer():
            x1 = int(x1)
        if x2.is_integer():
            x2 = int(x2)
        print(x1, x2)
