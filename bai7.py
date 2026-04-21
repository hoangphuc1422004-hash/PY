# Bài 7: Thay thế chuỗi "not...poor" bằng "good"
# Viết chương trình cho người dùng nhập 1 chuỗi (S)
# Nếu từ 'poor' đi sau từ 'not' thì thay đoạn từ 'not' đến 'poor' thành 'good'
# Các trường hợp khác sẽ giữ nguyên chuỗi

import re

def replace_not_poor(s):
    """
    Thay thế 'not ... poor' bằng 'good'
    """
    # Sử dụng regex để tìm và thay thế 'not ... poor' bằng 'good'
    # .*? nghĩa là bất kỳ ký tự nào (không tham lam)
    result = re.sub(r'not\s+.*?\s+poor', 'good', s, flags=re.IGNORECASE)
    return result

# Test case 1
s1 = 'The lyrics is not that poor!'
print(f"Chuỗi 1: {s1}")
print(f"Kết quả: {replace_not_poor(s1)}")
print()

# Test case 2
s2 = 'The lyrics is poor!'
print(f"Chuỗi 2: {s2}")
print(f"Kết quả: {replace_not_poor(s2)}")
print()

# Test case 3 - người dùng nhập
print("--- Nhập chuỗi của bạn ---")
s = input("Nhập chuỗi S: ")
print(f"Kết quả: {replace_not_poor(s)}")
