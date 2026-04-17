# Nhập thông tin hai vòng tròn C1 và C2.
# Mỗi vòng tròn xác định bởi tâm (x, y) và bán kính R.
# Dữ liệu có thể nhập trên một dòng hoặc nhiều dòng, cách nhau bởi khoảng trắng.

try:
    values = []
    while len(values) < 6:
        values.extend(input().strip().split())
    x1, y1, r1, x2, y2, r2 = map(int, values[:6])
except Exception as e:
    print("Dữ liệu không hợp lệ")
    raise SystemExit(1)

from math import sqrt

d = sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)

if d == 0 and r1 == r2:
    print("C1 và C2 trùng nhau")
elif d + r1 <= r2:
    print("C1 nằm trong C2")
elif d + r2 <= r1:
    print("C2 nằm trong C1")
elif abs(r1 - r2) <= d <= r1 + r2:
    print("C1 và C2 cắt nhau")
else:
    print("C1 và C2 không cắt nhau")
