

so_dong_nhat_all = lambda k: k > 0 and all(chu_so == str(k)[0] for chu_so in str(k)) # all(...) sẽ trả về True nếu TẤT CẢ các ký tự chữ số đều giống chữ số đầu tiên



so_dong_nhat_any = lambda k: k > 0 and not any(chu_so != str(k)[0] for chu_so in str(k)) # any(...) sẽ trả về True nếu có BẤT KỲ chữ số nào KHÁC chữ số đầu tiên, nên ta dùng 'not any' để suy ra TẤT CẢ đều giống nhau

so_hoan_thien = lambda n: n > 0 and sum(i for i in range(1, n) if n % i == 0) == n# Tổng tất cả các ước số (từ 1 đến n-1) phải bằng chính n


print(" CÁC SỐ ĐỒNG NHẤT TỪ 1 ĐẾN 10000 ")
ds_dong_nhat = []
for i in range(1, 10001): # lặp từ 1 đến 10000 để kiểm tra từng số có phải là số đồng nhất hay không
    
    if so_dong_nhat_all(i): 
        ds_dong_nhat.append(i)


print(", ".join(map(str, ds_dong_nhat)))
print(f"(Có tất cả {len(ds_dong_nhat)} số)\n")


print(" CÁC SỐ HOÀN THIỆN TỪ 1 ĐẾN 10000 ")
ds_hoan_thien = []
for i in range(1, 10001):
    if so_hoan_thien(i):
        ds_hoan_thien.append(i)

print(", ".join(map(str, ds_hoan_thien)))
print(f"(Có tất cả {len(ds_hoan_thien)} số)")
