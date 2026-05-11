# Thực hành I/O - File Reading and Writing

# 1. Viết file - Write to file
file_name = "test.txt"

# Write content to file
with open(file_name, 'w', encoding='utf-8') as f:
    f.write("Thuyện và biến\n")
    f.write("Chi có thuyện mới hiểu\n")
    f.write("Biến mệnh mông nhường nào\n")
    f.write("Chi có biến mới biết\n")
    f.write("Thuyện đi đâu về đâu\n")
    f.write("...\n")

print("File đã được viết thành công!")
print()

# 2. Đọc file - Read file
print("Nội dung file:")
print("-" * 40)

with open(file_name, 'r', encoding='utf-8') as f:
    content = f.read()
    print(content)

print("-" * 40)
print()

# 3. Đọc file theo từng dòng - Read file line by line
print("Đọc từng dòng:")
print("-" * 40)

with open(file_name, 'r', encoding='utf-8') as f:
    for line_num, line in enumerate(f, 1):
        print(f"Dòng {line_num}: {line.strip()}")

print("-" * 40)
