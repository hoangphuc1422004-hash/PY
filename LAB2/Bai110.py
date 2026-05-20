def decode_cipher_text(cipher_text: str) -> str:
    result = []
    i = 0
    while i < len(cipher_text):
        if cipher_text[i] == '#':
            if i + 2 >= len(cipher_text) or not cipher_text[i + 1].isdigit():
                raise ValueError('Định dạng cipher không hợp lệ')
            count = int(cipher_text[i + 1])
            char = cipher_text[i + 2]
            result.append(char * count)
            i += 3
        else:
            result.append(cipher_text[i])
            i += 1
    return ''.join(result)


def main() -> None:
    cipher_text = input('Nhập chuỗi cipher text: ').strip()
    if not cipher_text:
        print('Chuỗi không được để trống.')
        return
    try:
        plain_text = decode_cipher_text(cipher_text)
        print('Plain text:', plain_text)
    except ValueError as error:
        print('Lỗi:', error)


if __name__ == '__main__':
    main()
