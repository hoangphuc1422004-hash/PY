# Bài tập 1.16: Quản lý danh sách số
# Nhập nhiều số từ người dùng, sau mỗi lần nhập hỏi có tiếp tục không

numbers = []

# Nhập dữ liệu từ người dùng
while True:
    try:
        num = float(input("Nhập một số: "))
        numbers.append(num)
        
        # Hỏi có tiếp tục không
        while True:
            choice = input("Có muốn nhập tiếp không? (Yes/No): ").strip().upper()
            if choice in ['YES', 'Y']:
                break
            elif choice in ['NO', 'N']:
                break
            else:
                print("Vui lòng nhập Yes hoặc No!")
        
        if choice in ['NO', 'N']:
            break
    except ValueError:
        print("Lỗi! Vui lòng nhập một số hợp lệ.")

# Kiểm tra có số trong danh sách không
if len(numbers) == 0:
    print("Danh sách rỗng!")
else:
    # a) In ra các số nguyên tố có trong list
    print("\n" + "="*50)
    print("a) Các số trong danh sách:")
    print(numbers)
    
    # b) Tính trung bình cộng các số âm, trung bình cộng các số dương
    print("\nb) Thống kê số âm và số dương:")
    
    positive_nums = [n for n in numbers if n > 0]
    negative_nums = [n for n in numbers if n < 0]
    zero_count = numbers.count(0)
    
    if positive_nums:
        avg_positive = sum(positive_nums) / len(positive_nums)
        print(f"   - Số dương: {positive_nums}")
        print(f"   - Trung bình cộng các số dương: {avg_positive:.2f}")
    else:
        print("   - Không có số dương")
    
    if negative_nums:
        avg_negative = sum(negative_nums) / len(negative_nums)
        print(f"   - Số âm: {negative_nums}")
        print(f"   - Trung bình cộng các số âm: {avg_negative:.2f}")
    else:
        print("   - Không có số âm")
    
    if zero_count > 0:
        print(f"   - Số 0: {zero_count} lần")
    
    # c) Số lớn nhất, số nhỏ nhất
    print("\nc) Số lớn nhất và số nhỏ nhất:")
    max_num = max(numbers)
    min_num = min(numbers)
    print(f"   - Số lớn nhất: {max_num}")
    print(f"   - Số nhỏ nhất: {min_num}")
    print(f"   - Khoảng cách: {max_num - min_num}")
    
    # d) Kiểm tra xem các số trong list có được sắp xếp tăng dần hay giảm dần không
    print("\nd) Kiểm tra thứ tự sắp xếp:")
    
    # Kiểm tra tăng dần
    is_ascending = all(numbers[i] <= numbers[i+1] for i in range(len(numbers)-1))
    # Kiểm tra giảm dần
    is_descending = all(numbers[i] >= numbers[i+1] for i in range(len(numbers)-1))
    
    if is_ascending:
        print("   - Dãy số được sắp xếp theo thứ tự TĂNG DẦN")
    elif is_descending:
        print("   - Dãy số được sắp xếp theo thứ tự GIẢM DẦN")
    else:
        print("   - Dãy số KHÔNG được sắp xếp theo thứ tự tăng hay giảm")
    
    # Hiển thị dãy số sau khi sắp xếp
    print(f"\n   - Dãy sắp xếp tăng dần: {sorted(numbers)}")
    print(f"   - Dãy sắp xếp giảm dần: {sorted(numbers, reverse=True)}")

print("\n" + "="*50)
print("Cảm ơn bạn đã sử dụng chương trình!")
