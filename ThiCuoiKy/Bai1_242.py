

dai   = float(input("Nhập chiều dài đáy hình khối chữ nhật (cm)>? ")) # float để chuyển chuỗi đầu vào thành số thực, gán cho biến dài là kiểu float
rong  = float(input("Nhập chiều rộng đáy hình khối chữ nhật (cm)>? ")) # float để chuyển chuỗi đầu vào thành số thực, gán cho biến rong là kiểu float
cao   = float(input("Nhập chiều cao hình khối chữ nhật (cm)>? ")) # float để chuyển chuỗi đầu vào thành số thực, gán cho biến cao là kiểu float
n     = int(input("Số lượng số lẻ cần hiển thị>? ")) # int để chuyển chuỗi đầu vào thành số nguyên

dien_tich_day = dai * rong
the_tich      = dai * rong * cao

print(f"Diện tích đáy hình khối chữ nhật= {dien_tich_day:.{n}f} cm\u00b2") #  .{n}f để hiển thị số thực với n chữ số thập phân, \u00b2 để hiển thị ký tự mũ 2 (²)
print(f"Thể tích hình khối= {the_tich:.{n}f} cm\u00b3") #  .{n}f để hiển thị số thực với n chữ số thập phân, \u00b3 để hiển thị ký tự mũ 3 (³)
