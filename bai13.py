
def is_normalized_string(s):
    """
    Kiểm tra xem chuỗi có hoàn chỉnh không
    """
    # Kiểm tra đầu và cuối không có khoảng trắng
    if s != s.strip():
        return False
    
    # Kiểm tra giữa các từ chỉ có 1 khoảng trắng
    if '  ' in s:  # Có 2 khoảng trắng liên tiếp
        return False
    
    # Kiểm tra dấu chấm và phẩy không có space trước nó
    if ' .' in s or ' ,' in s:
        return False
    
    return True

def normalize_string(s):
    """
    Hoàn chỉnh chuỗi
    """
    # Bước 1: Loại bỏ khoảng trắng ở đầu và cuối
    s = s.strip()
    
    # Bước 2: Thay thế nhiều khoảng trắng thành 1 khoảng trắng
    while '  ' in s:
        s = s.replace('  ', ' ')
    
    # Bước 3: Loại bỏ khoảng trắng trước dấu chấm và phẩy
    s = s.replace(' .', '.')
    s = s.replace(' ,', ',')
    
    # Bước 4: Nếu là bài thơ (nhiều dòng), canh thẳng hàng các dòng
    if '\n' in s:
        lines = s.split('\n')
        normalized_lines = [line.strip() for line in lines]
        s = '\n'.join(normalized_lines)
    
    return s

# Test với các ví dụ từ bài
test_cases = [
    "Quê  hương\nQuê_hương_là____chỗ_khé___ngót.\n____Cho_con_trèo_hái____mẩu___ngày___.\nQuê__hương_là___đường_đi_học.\n__Con_về_rơi_buốm_vàng_bay..\n__Đõ______Trung_Quân____",
    "Quê hương\nQuê hương là chỗ khé ngót.\nCho con trèo hái mẩu ngày.\nQuê hương là đường đi học.\nCon về rơi buốm vàng bay.\nĐõ Trung Quân"
]

print("=" * 60)
print("KIỂM TRA VÀ HOÀN CHỈNH CHUỖI")
print("=" * 60)

# Test case 1: Chuỗi chưa hoàn chỉnh
s1 = "Quê  hương  là   chỗ  khé   ngót ."
print(f"\nChuỗi nhập vào: '{s1}'")
print(f"Đã hoàn chỉnh? {is_normalized_string(s1)}")
print(f"Chuỗi hoàn chỉnh: '{normalize_string(s1)}'")

# Test case 2: Chuỗi chưa hoàn chỉnh (đầu cuối có space)
s2 = "  Cho con trèo hái  mẩu  ngày  "
print(f"\nChuỗi nhập vào: '{s2}'")
print(f"Đã hoàn chỉnh? {is_normalized_string(s2)}")
print(f"Chuỗi hoàn chỉnh: '{normalize_string(s2)}'")

# Test case 3: Chuỗi chưa hoàn chỉnh (space trước dấu phẩy)
s3 = "Con về rơi buốm vàng bay ."
print(f"\nChuỗi nhập vào: '{s3}'")
print(f"Đã hoàn chỉnh? {is_normalized_string(s3)}")
print(f"Chuỗi hoàn chỉnh: '{normalize_string(s3)}'")

# Test case 4: Chuỗi đã hoàn chỉnh
s4 = "Đõ Trung Quân."
print(f"\nChuỗi nhập vào: '{s4}'")
print(f"Đã hoàn chỉnh? {is_normalized_string(s4)}")
print(f"Chuỗi hoàn chỉnh: '{normalize_string(s4)}'")

# Nhập từ người dùng
print("\n" + "=" * 60)
print("NHẬP CHUỖI CỦA BẠN")
print("=" * 60)
user_input = input("Nhập chuỗi: ")
print(f"\nChuỗi gốc: '{user_input}'")
print(f"Đã hoàn chỉnh? {is_normalized_string(user_input)}")
print(f"Chuỗi hoàn chỉnh: '{normalize_string(user_input)}'")
