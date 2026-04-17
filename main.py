Chieu_dai = float(input("Nhập Chiều Dài Đấy Hình Chữ Nhật (cm)"))
Chieu_rong = float(input("Nhập Chiều Rộng Đấy Hình Chữ Nhật (cm)"))
Chieu_Cao = float(input("Nhập Chiều Cao Đấy Hình Chữ Nhật (cm)"))

print ("dai = ", Chieu_dai)
print ("rong = ",Chieu_rong)
print ("cao = ",Chieu_Cao)

SoLe = input("Số Lượng Số lẻ cần hiển thị ")
DinhDang = '{:.'+SoLe+'f}'

Chieu_dai = float(DinhDang.format(eval(Chieu_dai)))
Chieu_rong = float(DinhDang.format(eval(Chieu_rong)))
Chieu_Cao = float(DinhDang.format(eval(Chieu_Cao)))

print ("dai = ", Chieu_dai)
print ("rong =", Chieu_rong)
print ("cao = ", Chieu_Cao)

dientich = Chieu_dai * Chieu_rong
dientich = float(DinhDang.format(eval(dientich)))

thetich = Chieu_dai * Chieu_Cao * Chieu_rong
thetich = float(DinhDang.format(eval(thetich)))

print("Dien Tich Day Hình Chu Nhat = ", dientich, "cm\u00b2" )
print("The Tich Hinh Khoi = ", thetich , "cm\u00b3" )