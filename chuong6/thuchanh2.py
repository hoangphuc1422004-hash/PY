# Bài tập 3.12: Thao tác với Dictionary
# Cho nhập 2 chuỗi (S1 và S2)
from collections import Counter

print("="*60)
print("BÀI TẬP 3.12: THAO TÁC VỚI DICTIONARY")
print("="*60)

# Nhập 2 dictionary từ người dùng
print("\nNhập từ điển S1 (ví dụ: {'a': 1, 'b': 2, 'c': 3})")
while True:
    try:
        s1_input = input("Nhập S1: ")
        S1 = eval(s1_input)
        if isinstance(S1, dict):
            break
        else:
            print("Lỗi! Vui lòng nhập một dictionary hợp lệ.")
    except:
        print("Lỗi! Vui lòng nhập một dictionary hợp lệ.")

print("\nNhập từ điển S2 (ví dụ: {'b': 2, 'c': 3, 'd': 4})")
while True:
    try:
        s2_input = input("Nhập S2: ")
        S2 = eval(s2_input)
        if isinstance(S2, dict):
            break
        else:
            print("Lỗi! Vui lòng nhập một dictionary hợp lệ.")
    except:
        print("Lỗi! Vui lòng nhập một dictionary hợp lệ.")

print("\n" + "="*60)

# a) In ra những kỳ tự xuất hiện trong cả 2 chuỗi
print("\na) Những kỳ tự xuất hiện trong cả 2 từ điển:")
print(f"   S1 = {S1}")
print(f"   S2 = {S2}")

# Sử dụng phương pháp giao của 2 dict (intersection)
keys_s1 = set(S1.keys())
keys_s2 = set(S2.keys())

common_keys = keys_s1 & keys_s2  # giao tuyến
print(f"   Những kỳ chung: {common_keys if common_keys else 'Không có'}")

# b) Đếm xem có bao nhiều kỳ tự có trong S1 nhưng không có trong S2 
# và có trong S2 nhưng không có trong S1
print("\nb) Số lượng kỳ tự khác nhau:")
only_in_s1 = keys_s1 - keys_s2  # trong S1 nhưng không trong S2
only_in_s2 = keys_s2 - keys_s1  # trong S2 nhưng không trong S1

print(f"   - Kỳ tự chỉ có trong S1: {len(only_in_s1)}")
print(f"   - Kỳ tự chỉ có trong S2: {len(only_in_s2)}")

# c) In ra những kỳ tự có trong S1 nhưng không có trong S2 
# và những kỳ tự có trong S2 nhưng không có trong S1
print("\nc) Chi tiết kỳ tự khác nhau:")
print(f"   - Trong S1 nhưng không có trong S2: {only_in_s1 if only_in_s1 else 'Không có'}")
print(f"   - Trong S2 nhưng không có trong S1: {only_in_s2 if only_in_s2 else 'Không có'}")

# Phương pháp sử dụng Counter (như gợi ý)
print("\n" + "="*60)
print("PHƯƠNG PHÁP DÙNG COUNTER VÀ TOÁN TỬ &:")
print("="*60)

# Chuyển 2 dictionary thành Counter
counter_s1 = Counter(S1)
counter_s2 = Counter(S2)

# Sử dụng phép giao (&) trên 2 Counter
intersection_result = counter_s1 & counter_s2
print(f"\nKỳ tự chung (dùng Counter & toán tử &): {dict(intersection_result)}")

print("\n" + "="*60)
print("TÓMA TẮT KẾT QUẢ:")
print("="*60)
print(f"S1 = {S1}")
print(f"S2 = {S2}")
print(f"Kỳ tự chung: {common_keys if common_keys else 'Không có'}")
print(f"Số kỳ tự chỉ trong S1: {len(only_in_s1)}")
print(f"Số kỳ tự chỉ trong S2: {len(only_in_s2)}")
print("="*60)
