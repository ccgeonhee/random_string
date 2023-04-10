# 샘플 Python 스크립트입니다.
import os
import random
import string

import bcrypt

# Shift+F10을(를) 눌러 실행하거나 내 코드로 바꿉니다.
# 클래스, 파일, 도구 창, 액션 및 설정을 어디서나 검색하려면 Shift 두 번을(를) 누릅니다.


# 0: 소문자만, 1: 대문자만, 2: 대,소문자 모두
ascii_case_map = {
    0: string.ascii_lowercase,
    1: string.ascii_uppercase,
    2: string.ascii_letters,
}
def random_string(string_length, count, ascii_case):
    if ascii_case not in ascii_case_map:
        raise Exception(f"Ascii case not in {list(ascii_case_map.keys())}")

    for _ in range(count):
        rand_str = ''.join(random.choice(ascii_case_map.get(ascii_case) + string.digits) for _ in range(string_length))
        encoded = rand_str.encode('utf-8')
        salt = bcrypt.gensalt(10)
        hashed = bcrypt.hashpw(encoded, salt)
        hashed = str(hashed)[2:-1]
        print(f"랜덤스트링: {rand_str}, 비밀번호: {hashed}")


# 스크립트를 실행하려면 여백의 녹색 버튼을 누릅니다.
if __name__ == '__main__':
    string_length = int(input("랜덤 문자열 길이를 입력해주세요: "))
    count = int(input("생성할 문자열 개수를 입력해주세요: "))
    print("\n0: 소문자만, 1: 대문자만, 2: 대, 소문자 모두")
    ascii_case = int(input("대, 소문자 여부를 입력해주세요: "))
    random_string(string_length, count, ascii_case)

    os.system('pause')

# https://www.jetbrains.com/help/pycharm/에서 PyCharm 도움말 참조
