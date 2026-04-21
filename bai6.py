# Bài 6: Đếm số lần xuất hiện của một từ trong chuỗi
# Viết chương trình cho người dùng nhập 1 chuỗi (S) và 1 từ (word)
# Đếm xem trong S có bao nhiều từ word

s = '''Chiều chiều trước bên Vân Lâu
Ai ngồi, ai cầu, ai sầu, ai thầm
Ai thương, ai cầm, ai nhớ, ai trông
Thuyên ai thắp thoáng ven sông
Dua cầu mãi vây chanh lòng nước non'''

word = 'ai'

# Phương pháp 1: Sử dụng count()
count1 = s.count(word)
print(f"Phương pháp 1 (count): Số từ '{word}' là {count1}")

# Phương pháp 2: Sử dụng split() và đếm
words_list = s.lower().split()
count2 = sum(1 for w in words_list if word.lower() in w)
print(f"Phương pháp 2 (split): Số từ '{word}' là {count2}")

# Phương pháp 3: Đếm bằng vòng lặp
count3 = 0
i = 0
while i < len(s):
    if s[i:i+len(word)].lower() == word.lower():
        count3 += 1
        i += len(word)
    else:
        i += 1
print(f"Phương pháp 3 (vòng lặp): Số từ '{word}' là {count3}")
