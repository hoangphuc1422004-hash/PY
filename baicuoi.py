# Bài 1: In ra các thông tin ngày giờ hiện tại
from datetime import datetime
import calendar

now = datetime.now()

print("=" * 50)
print("THÔNG TIN NGÀY GIỜ HIỆN TẠI")
print("=" * 50)

# Năm hiện tại
year = now.year
print(f"Năm hiện tại: {year}")

# Tháng hiện tại bằng chữ
month_name = calendar.month_name[now.month]
print(f"Tháng hiện tại: {month_name}")

# Tuần thứ mấy trong năm (week number)
week_of_year = now.isocalendar()[1]
print(f"Tuần hiện tại là tuần thứ mấy trong năm: {week_of_year}")

# Tuần thứ mấy trong tháng
# Công thức: (day + first_weekday - 1) // 7 + 1
first_day_of_month = datetime(now.year, now.month, 1)
week_of_month = (now.day + first_day_of_month.weekday() - 1) // 7 + 1
print(f"Tuần hiện tại là tuần thứ mấy trong tháng: {week_of_month}")

# Ngày thứ mấy trong năm (day of year)
day_of_year = now.timetuple().tm_yday
print(f"Ngày hiện tại là ngày thứ mấy trong năm: {day_of_year}")

# Ngày dương lịch (ngày trong tháng)
day = now.day
print(f"Ngày dương lịch hiện tại là ngày: {day}")

# Thứ của ngày hiện tại
weekday_name = calendar.day_name[now.weekday()]
print(f"Thứ của ngày hiện tại: {weekday_name}")

# Giờ phút giây
time_str = now.strftime("%H:%M:%S")
print(f"Giờ phút giây hiện tại: {time_str}")

# Bài 2: Tính số ngày cách nhau giữa 2 ngày
print("\n" + "=" * 50)
print("TÍNH KHOẢNG CÁCH GIỮA 2 NGÀY")
print("=" * 50)

try:
    print("\nNhập ngày thứ nhất (định dạng: ngày tháng năm, cách nhau bởi /):")
    input1 = input("Nhập: ")
    date1_parts = input1.split('/')
    day1, month1, year1 = int(date1_parts[0]), int(date1_parts[1]), int(date1_parts[2])
    date1 = datetime(year1, month1, day1)
    
    print("Nhập ngày thứ hai (định dạng: ngày tháng năm, cách nhau bởi /):")
    input2 = input("Nhập: ")
    date2_parts = input2.split('/')
    day2, month2, year2 = int(date2_parts[0]), int(date2_parts[1]), int(date2_parts[2])
    date2 = datetime(year2, month2, day2)
    
    days_diff = abs((date2 - date1).days)
    print(f"Số ngày cách nhau: {days_diff} ngày")
    
except Exception as e:
    print(f"Lỗi: Định dạng không hợp lệ. {e}")

# Bài 3: Chuyển chuỗi ngày sang kiểu datetime
print("\n" + "=" * 50)
print("CHUYỂN CHUỖI SANG KIỂU DATETIME")
print("=" * 50)

try:
    print("Nhập chuỗi ngày (định dạng: 'Sep 18 2019 2:43PM'):")
    date_string = input("Nhập: ")
    
    # Parse chuỗi ngày
    date_obj = datetime.strptime(date_string, '%b %d %Y %I:%M%p')
    print(f"Kết quả: {date_obj}")
    print(f"Định dạng khác: {date_obj.strftime('%Y-%m-%d %H:%M:%S')}")
    
except Exception as e:
    print(f"Lỗi: {e}")

# Bài 4: Sử dụng timedelta để thêm 5 giây
print("\n" + "=" * 50)
print("THÊM 5 GIÂY VÀO THỜI GIAN HIỆN TẠI")
print("=" * 50)

from datetime import timedelta

current_time = datetime.now()
new_time = current_time + timedelta(seconds=5)

print(f"Thời gian hiện tại: {current_time.strftime('%H:%M:%S')}")
print(f"Sau khi thêm 5 giây: {new_time.strftime('%H:%M:%S')}")

# Ví dụ thêm các thời gian khác
print("\n--- Ví dụ thêm các khoảng thời gian khác ---")
print(f"Thêm 1 giờ: {(current_time + timedelta(hours=1)).strftime('%H:%M:%S')}")
print(f"Thêm 1 ngày: {(current_time + timedelta(days=1)).strftime('%Y-%m-%d')}")
print(f"Thêm 1 tuần: {(current_time + timedelta(weeks=1)).strftime('%Y-%m-%d')}")
print(f"Trừ 30 phút: {(current_time - timedelta(minutes=30)).strftime('%H:%M:%S')}")
