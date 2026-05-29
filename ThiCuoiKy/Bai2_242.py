
#Nhập 2 số nguyên a và b, in bảng cửu chương từ a đến b
def bang_cuu_chuong(a, b):
    # Đảm bảo start luôn nhỏ hơn end
    if a > b:
        a, b = b, a  # hoán đổi cho tiện

    for i in range(a, b + 1): # lặp từ a đến b (bao gồm b) thì in ra bảng cửu chương của i 
      
        dong = ""
        for j in range(1, 11):
            dong += f"{i} x {j} = {i*j}"
            if j < 10:
                dong += ", "
        print(dong)


# Liệt kê các ước số nguyên tố <= n

def uoc_so_nguyen_to(n):
    ds = []  # danh sách lưu kết quả

    for so in range(2, n + 1): # lặp từ 2 đến n để kiểm tra từng số có phải là nguyên tố hay không
        la_nguyen_to = True  
       
        for uoc in range(2, so): # kiểm tra nếu so chia hết cho bất kỳ số nào từ 2 đến so-1 thì nó không phải là nguyên tố
            if so % uoc == 0:
                la_nguyen_to = False
                break  

        if la_nguyen_to:
            ds.append(so)

    return ds



print("=" * 60)
print(" Bảng cửu chương")
a, b = map(int, input("Nhập 2 số nguyên a và b (cách nhau bởi dấu phẩy ): ").split(",")) # split để tách chuỗi đầu vào thành 2 phần, map để chuyển từng phần thành int, rồi gán lần lượt cho a và b
bang_cuu_chuong(a, b)

print("=" * 60)
print(" Liệt kê các ước số nguyên tố <= n")
n = int(input("Nhập n: "))
ds = uoc_so_nguyen_to(n)
print(f"Các ước số của {n} gồm {len(ds)} số nguyên tố:", ", ".join(map(str, ds))) # join để nối các phần tử trong ds thành một chuỗi, map để chuyển từng phần tử thành str trước khi nối câu
