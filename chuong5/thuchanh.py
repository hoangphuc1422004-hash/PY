# Thực hành 6: Anonymous Function (Lambda)

# a) Hàm nhận 1 đối số là số nguyên n và trả về trị tuyệt đối của n
absolute_value = lambda n: abs(n)

# b) Hàm nhận 1 đối số là số nguyên n và trả về giá trị của n+15
add_fifteen = lambda n: n + 15

# c) Hàm nhận 2 đối số là số nguyên (x, y), trả về tích của x và y
multiply = lambda x, y: x * y

# d) Hàm nhận 1 đối số là số nguyên n. Cho biết n có là bội số của 13 hoặc 19 hay không?
is_multiple = lambda n: "Có" if n % 13 == 0 or n % 19 == 0 else "Không"

# e) Hàm nhận 1 đối số là số thực r là bán kính của hình tròn. Cho biết diện tích hình tròn
import math
circle_area = lambda r: math.pi * r ** 2

# f) Hàm nhận 2 đối số là số thực d, r là chiều dài và chiều rộng của hình chữ nhật. Cho biết chu vi hình chữ nhật
rectangle_perimeter = lambda d, r: 2 * (d + r)

# g) Hàm nhận 1 đối số là số nguyên n. Cho biết n có là số chính phương hay không?
is_perfect_square = lambda n: "Có" if int(math.sqrt(n)) ** 2 == n and n >= 0 else "Không"

# h) Hàm nhận 1 đối số là số nguyên n. Cho biết n có là số nguyên tố hay không?
def is_prime(n):
    if n < 2:
        return "Không"
    if n == 2:
        return "Có"
    if n % 2 == 0:
        return "Không"
    for i in range(3, int(math.sqrt(n)) + 1, 2):
        if n % i == 0:
            return "Không"
    return "Có"

is_prime_lambda = lambda n: is_prime(n)

# i) Hàm nhận 3 tham số là số nguyên (a, b, c). Cho biết a, b, c có là 3 cạnh hợp lệ của 1 tam giác hay không?
# Nếu là 3 cạnh hợp lệ, cho biết đó là tam giác gì?
def classify_triangle(a, b, c):
    # Kiểm tra điều kiện tam giác: tổng hai cạnh > cạnh còn lại
    if a + b > c and b + c > a and a + c > b and a > 0 and b > 0 and c > 0:
        if a == b == c:
            return "Tam giác đều"
        elif a == b or b == c or a == c:
            # Kiểm tra nếu vừa cân vừa vuông
            sides = sorted([a, b, c])
            if sides[0]**2 + sides[1]**2 == sides[2]**2:
                return "Tam giác vuông cân"
            else:
                return "Tam giác cân"
        elif a**2 + b**2 == c**2 or b**2 + c**2 == a**2 or a**2 + c**2 == b**2:
            return "Tam giác vuông"
        else:
            return "Tam giác thường"
    else:
        return "Không hợp lệ"

triangle_type = lambda a, b, c: classify_triangle(a, b, c)


# TEST CÁC HÀM
print("="*50)
print("a) Trị tuyệt đối:")
print(f"   absolute_value(-5) = {absolute_value(-5)}")
print(f"   absolute_value(-15) = {absolute_value(-15)}")

print("\nb) Cộng 15:")
print(f"   add_fifteen(5) = {add_fifteen(5)}")
print(f"   add_fifteen(-10) = {add_fifteen(-10)}")

print("\nc) Tích của 2 số:")
print(f"   multiply(3, 4) = {multiply(3, 4)}")
print(f"   multiply(7, 8) = {multiply(7, 8)}")

print("\nd) Bội số của 13 hoặc 19:")
print(f"   is_multiple(26) = {is_multiple(26)}")  # Bội của 13
print(f"   is_multiple(38) = {is_multiple(38)}")  # Bội của 19
print(f"   is_multiple(10) = {is_multiple(10)}")  # Không

print("\ne) Diện tích hình tròn (r=5):")
print(f"   circle_area(5) = {circle_area(5):.2f}")

print("\nf) Chu vi hình chữ nhật (d=5, r=3):")
print(f"   rectangle_perimeter(5, 3) = {rectangle_perimeter(5, 3)}")

print("\ng) Số chính phương:")
print(f"   is_perfect_square(16) = {is_perfect_square(16)}")
print(f"   is_perfect_square(25) = {is_perfect_square(25)}")
print(f"   is_perfect_square(10) = {is_perfect_square(10)}")

print("\nh) Số nguyên tố:")
print(f"   is_prime_lambda(17) = {is_prime_lambda(17)}")
print(f"   is_prime_lambda(4) = {is_prime_lambda(4)}")
print(f"   is_prime_lambda(2) = {is_prime_lambda(2)}")

print("\ni) Phân loại tam giác:")
print(f"   triangle_type(3, 3, 3) = {triangle_type(3, 3, 3)}")
print(f"   triangle_type(5, 5, 6) = {triangle_type(5, 5, 6)}")
print(f"   triangle_type(3, 4, 5) = {triangle_type(3, 4, 5)}")
print(f"   triangle_type(5, 12, 13) = {triangle_type(5, 12, 13)}")
print(f"   triangle_type(2, 3, 5) = {triangle_type(2, 3, 5)}")
print("="*50)
