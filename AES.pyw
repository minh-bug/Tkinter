import tkinter as tk
import random


data = "1234567890abcdf"

# Biến toàn cục
Nk = 4  # Độ dài khóa
Nb = 4  # Kích thước khối
Nr = 10  # Số lần lặp
s_box = [
    0x63,
    0x7C,
    0x77,
    0x7B,
    0xF2,
    0x6B,
    0x6F,
    0xC5,
    0x30,
    0x01,
    0x67,
    0x2B,
    0xFE,
    0xD7,
    0xAB,
    0x76,
    0xCA,
    0x82,
    0xC9,
    0x7D,
    0xFA,
    0x59,
    0x47,
    0xF0,
    0xAD,
    0xD4,
    0xA2,
    0xAF,
    0x9C,
    0xA4,
    0x72,
    0xC0,
    0xB7,
    0xFD,
    0x93,
    0x26,
    0x36,
    0x3F,
    0xF7,
    0xCC,
    0x34,
    0xA5,
    0xE5,
    0xF1,
    0x71,
    0xD8,
    0x31,
    0x15,
    0x04,
    0xC7,
    0x23,
    0xC3,
    0x18,
    0x96,
    0x05,
    0x9A,
    0x07,
    0x12,
    0x80,
    0xE2,
    0xEB,
    0x27,
    0xB2,
    0x75,
    0x09,
    0x83,
    0x2C,
    0x1A,
    0x1B,
    0x6E,
    0x5A,
    0xA0,
    0x52,
    0x3B,
    0xD6,
    0xB3,
    0x29,
    0xE3,
    0x2F,
    0x84,
    0x53,
    0xD1,
    0x00,
    0xED,
    0x20,
    0xFC,
    0xB1,
    0x5B,
    0x6A,
    0xCB,
    0xBE,
    0x39,
    0x4A,
    0x4C,
    0x58,
    0xCF,
    0xD0,
    0xEF,
    0xAA,
    0xFB,
    0x43,
    0x4D,
    0x33,
    0x85,
    0x45,
    0xF9,
    0x02,
    0x7F,
    0x50,
    0x3C,
    0x9F,
    0xA8,
    0x51,
    0xA3,
    0x40,
    0x8F,
    0x92,
    0x9D,
    0x38,
    0xF5,
    0xBC,
    0xB6,
    0xDA,
    0x21,
    0x10,
    0xFF,
    0xF3,
    0xD2,
    0xCD,
    0x0C,
    0x13,
    0xEC,
    0x5F,
    0x97,
    0x44,
    0x17,
    0xC4,
    0xA7,
    0x7E,
    0x3D,
    0x64,
    0x5D,
    0x19,
    0x73,
    0x60,
    0x81,
    0x4F,
    0xDC,
    0x22,
    0x2A,
    0x90,
    0x88,
    0x46,
    0xEE,
    0xB8,
    0x14,
    0xDE,
    0x5E,
    0x0B,
    0xDB,
    0xE0,
    0x32,
    0x3A,
    0x0A,
    0x49,
    0x06,
    0x24,
    0x5C,
    0xC2,
    0xD3,
    0xAC,
    0x62,
    0x91,
    0x95,
    0xE4,
    0x79,
    0xE7,
    0xC8,
    0x37,
    0x6D,
    0x8D,
    0xD5,
    0x4E,
    0xA9,
    0x6C,
    0x56,
    0xF4,
    0xEA,
    0x65,
    0x7A,
    0xAE,
    0x08,
    0xBA,
    0x78,
    0x25,
    0x2E,
    0x1C,
    0xA6,
    0xB4,
    0xC6,
    0xE8,
    0xDD,
    0x74,
    0x1F,
    0x4B,
    0xBD,
    0x8B,
    0x8A,
    0x70,
    0x3E,
    0xB5,
    0x66,
    0x48,
    0x03,
    0xF6,
    0x0E,
    0x61,
    0x35,
    0x57,
    0xB9,
    0x86,
    0xC1,
    0x1D,
    0x9E,
    0xE1,
    0xF8,
    0x98,
    0x11,
    0x69,
    0xD9,
    0x8E,
    0x94,
    0x9B,
    0x1E,
    0x87,
    0xE9,
    0xCE,
    0x55,
    0x28,
    0xDF,
    0x8C,
    0xA1,
    0x89,
    0x0D,
    0xBF,
    0xE6,
    0x42,
    0x68,
    0x41,
    0x99,
    0x2D,
    0x0F,
    0xB0,
    0x54,
    0xBB,
    0x16,
]
inverse_sbox = [
    0x52,
    0x09,
    0x6A,
    0xD5,
    0x30,
    0x36,
    0xA5,
    0x38,
    0xBF,
    0x40,
    0xA3,
    0x9E,
    0x81,
    0xF3,
    0xD7,
    0xFB,
    0x7C,
    0xE3,
    0x39,
    0x82,
    0x9B,
    0x2F,
    0xFF,
    0x87,
    0x34,
    0x8E,
    0x43,
    0x44,
    0xC4,
    0xDE,
    0xE9,
    0xCB,
    0x54,
    0x7B,
    0x94,
    0x32,
    0xA6,
    0xC2,
    0x23,
    0x3D,
    0xEE,
    0x4C,
    0x95,
    0x0B,
    0x42,
    0xFA,
    0xC3,
    0x4E,
    0x08,
    0x2E,
    0xA1,
    0x66,
    0x28,
    0xD9,
    0x24,
    0xB2,
    0x76,
    0x5B,
    0xA2,
    0x49,
    0x6D,
    0x8B,
    0xD1,
    0x25,
    0x72,
    0xF8,
    0xF6,
    0x64,
    0x86,
    0x68,
    0x98,
    0x16,
    0xD4,
    0xA4,
    0x5C,
    0xCC,
    0x5D,
    0x65,
    0xB6,
    0x92,
    0x6C,
    0x70,
    0x48,
    0x50,
    0xFD,
    0xED,
    0xB9,
    0xDA,
    0x5E,
    0x15,
    0x46,
    0x57,
    0xA7,
    0x8D,
    0x9D,
    0x84,
    0x90,
    0xD8,
    0xAB,
    0x00,
    0x8C,
    0xBC,
    0xD3,
    0x0A,
    0xF7,
    0xE4,
    0x58,
    0x05,
    0xB8,
    0xB3,
    0x45,
    0x06,
    0xD0,
    0x2C,
    0x1E,
    0x8F,
    0xCA,
    0x3F,
    0x0F,
    0x02,
    0xC1,
    0xAF,
    0xBD,
    0x03,
    0x01,
    0x13,
    0x8A,
    0x6B,
    0x3A,
    0x91,
    0x11,
    0x41,
    0x4F,
    0x67,
    0xDC,
    0xEA,
    0x97,
    0xF2,
    0xCF,
    0xCE,
    0xF0,
    0xB4,
    0xE6,
    0x73,
    0x96,
    0xAC,
    0x74,
    0x22,
    0xE7,
    0xAD,
    0x35,
    0x85,
    0xE2,
    0xF9,
    0x37,
    0xE8,
    0x1C,
    0x75,
    0xDF,
    0x6E,
    0x47,
    0xF1,
    0x1A,
    0x71,
    0x1D,
    0x29,
    0xC5,
    0x89,
    0x6F,
    0xB7,
    0x62,
    0x0E,
    0xAA,
    0x18,
    0xBE,
    0x1B,
    0xFC,
    0x56,
    0x3E,
    0x4B,
    0xC6,
    0xD2,
    0x79,
    0x20,
    0x9A,
    0xDB,
    0xC0,
    0xFE,
    0x78,
    0xCD,
    0x5A,
    0xF4,
    0x1F,
    0xDD,
    0xA8,
    0x33,
    0x88,
    0x07,
    0xC7,
    0x31,
    0xB1,
    0x12,
    0x10,
    0x59,
    0x27,
    0x80,
    0xEC,
    0x5F,
    0x60,
    0x51,
    0x7F,
    0xA9,
    0x19,
    0xB5,
    0x4A,
    0x0D,
    0x2D,
    0xE5,
    0x7A,
    0x9F,
    0x93,
    0xC9,
    0x9C,
    0xEF,
    0xA0,
    0xE0,
    0x3B,
    0x4D,
    0xAE,
    0x2A,
    0xF5,
    0xB0,
    0xC8,
    0xEB,
    0xBB,
    0x3C,
    0x83,
    0x53,
    0x99,
    0x61,
    0x17,
    0x2B,
    0x04,
    0x7E,
    0xBA,
    0x77,
    0xD6,
    0x26,
    0xE1,
    0x69,
    0x14,
    0x63,
    0x55,
    0x21,
    0x0C,
    0x7D,
]


# Các hàm def
def SubBytes(state):
    for i in range(4):
        for j in range(4):
            # Get the row and column indices from the current byte value
            row = (int(state[i][j], 16) >> 4) & 0xF
            col = int(state[i][j], 16) & 0xF
            # Replace the byte with the corresponding value from the S-box
            state[i][j] = hex(s_box[row * 16 + col])[2:]
    return state


def Inverse_sub_bytes(state):
    """
    Thực hiện thay thế ngược lại (Inverse SubBytes) trên ma trận trạng thái.
    `state` là ma trận 4x4 của byte.
    """
    for i in range(4):
        for j in range(4):
            # Get the row and column indices from the current byte value
            row = (int(state[i][j], 16) >> 4) & 0xF
            col = int(state[i][j], 16) & 0xF
            # Replace the byte with the corresponding value from the S-box
            state[i][j] = hex(inverse_sbox[row * 16 + col])[2:]

    return state


def ShiftRows(state):
    """
    Thực hiện phép dịch các byte trong mỗi hàng của ma trận 4x4 của trạng thái sang trái.
    `state` là một ma trận 4x4 của các byte.
    """
    for i in range(4):  # Bắt đầu từ hàng thứ hai, vì hàng đầu tiên không dịch
        state[i] = state[i][i:] + state[i][:i]
    return state


def Inverse_shift_rows(state):
    """
    Thực hiện dịch ngược lại trên các hàng của ma trận trạng thái (Inverse ShiftRows).
    `state` là ma trận 4x4 của byte.
    """
    for i in range(1, 4):
        state[i] = state[i][-i:] + state[i][:-i]

    return state


def multiply(a, b):
    result = 0
    while b > 0:
        if b % 2 == 1:
            result ^= a
        a <<= 1
        if a & 0x100:
            a ^= 0x11B
        b >>= 1
    return result


def MixColumns(state):
    """
    Thực hiện phép toán MixColumns trên một ma trận 4x4 của trạng thái.
    `state` là một ma trận 4x4 của các byte.
    """
    for i in range(4):
        s0 = int(state[0][i], 16)
        s1 = int(state[1][i], 16)
        s2 = int(state[2][i], 16)
        s3 = int(state[3][i], 16)

        state[0][i] = hex(multiply(0x02, s0) ^ multiply(0x03, s1) ^ s2 ^ s3)[2:]
        state[1][i] = hex(s0 ^ multiply(0x02, s1) ^ multiply(0x03, s2) ^ s3)[2:]
        state[2][i] = hex(s0 ^ s1 ^ multiply(0x02, s2) ^ multiply(0x03, s3))[2:]
        state[3][i] = hex(multiply(0x03, s0) ^ s1 ^ s2 ^ multiply(0x02, s3))[2:]

    return state


def Inverse_mix_columns(state):
    """
    Thực hiện dịch ngược lại trên các cột của ma trận trạng thái (Inverse MixColumns).
    `state` là ma trận 4x4 của byte.
    """
    for i in range(4):
        s0 = int(state[0][i], 16)
        s1 = int(state[1][i], 16)
        s2 = int(state[2][i], 16)
        s3 = int(state[3][i], 16)

        state[0][i] = hex(
            multiply(0x0E, s0)
            ^ multiply(0x0B, s1)
            ^ multiply(0x0D, s2)
            ^ multiply(0x09, s3)
        )[2:]
        state[1][i] = hex(
            multiply(0x09, s0)
            ^ multiply(0x0E, s1)
            ^ multiply(0x0B, s2)
            ^ multiply(0x0D, s3)
        )[2:]
        state[2][i] = hex(
            multiply(0x0D, s0)
            ^ multiply(0x09, s1)
            ^ multiply(0x0E, s2)
            ^ multiply(0x0B, s3)
        )[2:]
        state[3][i] = hex(
            multiply(0x0B, s0)
            ^ multiply(0x0D, s1)
            ^ multiply(0x09, s2)
            ^ multiply(0x0E, s3)
        )[2:]

    return state


def AddRoundKey(state, round_key):
    """
    Thực hiện phép toán XOR giữa ma trận trạng thái và khóa con của vòng mã hóa hiện tại.
    `state` là một ma trận 4x4 của các byte.
    `round_key` là một ma trận 4x4 của các byte, tương ứng với khóa con của vòng mã hóa.
    Do hàm add round key dựa vào phép toán XOR lên việc giải mã cũng có thể sử dụng hàm AddRoundKey
    """
    for i in range(4):
        for j in range(4):
            state[i][j] = hex(int(state[i][j], 16) ^ int(round_key[i][j], 16))[
                2:
            ]  # Thực hiện phép toán XOR
    return state


def state_to_strings(state):
    """Đưa một state/block thành một chuỗi"""
    result = []
    for i in state:
        result.append("".join(i))
    result = "".join(result)
    return result


def dec(state):
    """Hàm đưa một state về dạng bản rõ"""
    for i in range(4):
        for j in range(4):
            state[i][j] = chr(int(state[i][j], 16))
    return state


def state_to_strings(state):
    """Đưa một state/block thành một chuỗi"""
    result = []
    for i in state:
        result.append("".join(i))
    result = "".join(result)
    return result


def dec(state):
    """Hàm đưa một state về dạng bản rõ"""
    for i in range(4):
        for j in range(4):
            state[i][j] = chr(int(state[i][j], 16))
    return state


def string_to_blocks(input_string):
    """Đầu vào là một list ký tự trong mảng 1 gồm các ký tự thuộc chuỗi"""
    # Chia chuỗi thành các đoạn có độ dài là 16 (4x4)
    chunks = [input_string[i : i + 16] for i in range(0, len(input_string), 16)]

    # Bổ sung ký tự filler để đảm bảo mỗi đoạn có độ dài là 16
    for i, chunk in enumerate(chunks):
        filler_length = 16 - len(chunk)
        chunks[i] += ["0"] * filler_length

    # Chuyển đổi mỗi đoạn thành ma trận 4x4
    blocks = []
    for chunk in chunks:
        block = [[chunk[i + j] for j in range(4)] for i in range(0, len(chunk), 4)]
        blocks.append(block)

    return blocks


def Aes(state, key):
    """Thực hiện mã hóa một khối
    state là các khối cần được mã hóa
    key là list các key được mở rộng

    """
    # Thêm khóa vòng đầu
    state = AddRoundKey(state, key[0])
    # Bắt đầu 9 vòng đầu :
    for i in range(1, 10):
        state = SubBytes(state)
        state = ShiftRows(state)
        state = MixColumns(state)
        state = AddRoundKey(state, key[i])
    # Vòng thứ 10:
    state = SubBytes(state)
    state = ShiftRows(state)
    state = AddRoundKey(state, key[10])
    return state


def Inv_aes(state, key):
    """Thực hiện giải mã một khối
    state là các khối cần được giải mã
    key là các khóa được mở rộng
    """
    # Dịch mã vòng cuối
    state = AddRoundKey(state, key[10])
    state = Inverse_shift_rows(state)
    state = Inverse_sub_bytes(state)
    # Dịch ngược lại 9 vòng đầu từ 9 --> 1
    for i in range(9, 0, -1):
        state = AddRoundKey(state, key[i])
        state = Inverse_mix_columns(state)
        state = Inverse_shift_rows(state)
        state = Inverse_sub_bytes(state)
    state = AddRoundKey(state, key[0])
    return state


def Ma_Hoa_AES(input, key):
    """Hàm Mã hóa một chuỗi ký tự
    Nhận đầu vào là một list
    Đầu ra là một chuỗi ký tự đã được mã hóa
    """
    input = [hex(ord(x))[2:] for x in input]
    input = string_to_blocks(input)
    ban_ma = ""
    for i in range(len(input)):
        ban_ma = ban_ma + state_to_strings(Aes(input[i], key))
    print("*" * 50)
    print("Kết quả mã hóa : " + ban_ma)
    return ban_ma


def Giai_Ma_AES(input, key):
    """Hàm Giai Mã một chuỗi ký tự
    Nhận đầu vào và một chuỗi ký tự
    """
    input = [hex(ord(x))[2:] for x in input]
    input = string_to_blocks(input)
    ban_ro = ""
    for i in range(len(input)):
        ban_ro = ban_ro + state_to_strings(dec(Inv_aes(input[i], key)))
    print("*" * 50)
    print("Kết quả giải mã : " + ban_ro)
    return ban_ro


def main_aes(input, key):
    """Yêu cầu đầu vào là một chuỗi ký tự và list 11 khóa đa được mở rộng"""
    output_string_mh = Ma_Hoa_AES(input, key)
    output_string_gm = Giai_Ma_AES(output_string_mh, key)
    return [output_string_mh, output_string_gm]


def key_to_state(state):
    new_state = [
        ["00", "00", "00", "00"],
        ["00", "00", "00", "00"],
        ["00", "00", "00", "00"],
        ["00", "00", "00", "00"],
    ]
    for i in range(4):
        for j in range(4):
            new_state[i][j] = state[j][i]
    return new_state


def string_to_state(input_string):
    """Hàm nhận đầu vào là một chuỗi hex gồm 32 ký tự và chia chuỗi thành mảng 4x4"""
    # Đảm bảo chiều dài của chuỗi đầu vào là đúng (32 ký tự)
    if len(input_string) != 32:
        raise ValueError("Độ dài của chuỗi đầu vào phải là 32 ký tự.")

    # Khởi tạo state 4x4 với giá trị mặc định là 0
    state = [
        ["00", "00", "00", "00"],
        ["00", "00", "00", "00"],
        ["00", "00", "00", "00"],
        ["00", "00", "00", "00"],
    ]

    # Điền giá trị từ chuỗi vào state theo hàng ngang từ trái sang phải
    for i in range(4):
        for j in range(4):
            # Lấy 2 ký tự từ chuỗi
            byte_str = input_string[i * 8 + j * 2 : i * 8 + (j + 1) * 2]
            # Đặt giá trị byte vào state
            state[j][i] = byte_str

    return state


def key_expansion(key):
    r_con = [0x01, 0x02, 0x04, 0x08, 0x10, 0x20, 0x40, 0x80, 0x1B, 0x36]

    def sub_word(word):
        for i in range(4):
            # Get the row and column indices from the current byte value
            row = (word[i] >> 4) & 0xF
            col = word[i] & 0xF
            # Replace the byte with the corresponding value from the S-box
            word[i] = s_box[row * 16 + col]
        return word

    def rot_word(word):
        return word[1:] + [word[0]]

    def xor_words(word1, word2):
        """Hàm thực hiện phép toán XOR giữa hai word"""
        return [(b1 ^ b2) for b1, b2 in zip(word1, word2)]

    def split_into_matrices(expanded_key):
        """Hàm chuyển một chuỗi 16 phần tử thành một ma trận 4x4"""
        return [expanded_key[i : i + 4] for i in range(0, len(expanded_key), 4)]

    # Bước 1: Khởi tạo khóa mở rộng với khóa ban đầu
    expanded_key = [int(key[i : i + 2], 16) for i in range(0, len(key), 2)]
    # Bước 2: Lặp lại quy trình mở rộng khóa cho đến khi có đủ khóa con cho tất cả các vòng
    for i in range(4, 4 * 11):  # 4 * số vòng (10 vòng cho AES-128)
        temp = expanded_key[(i - 1) * 4 : i * 4]
        # Lấy temp
        # Bước 3: Thực hiện các phép biến đổi (g)
        if i % 4 == 0:
            # Dữ liệu label frame 1
            temp = rot_word(temp)
            # print([hex(x)[2:] for x in temp])
            temp = sub_word(temp)
            # print([hex(x)[2:] for x in temp])
            temp = xor_words(temp, [r_con[i // 4 - 1], 0, 0, 0])
            # print([hex(x)[2:] for x in temp])
        # Dữ liệu label frame 2
        temp = xor_words(expanded_key[(i - 4) * 4 : (i - 3) * 4], temp)
        expanded_key.extend(temp)

    # Bước 4: Chia danh sách khóa mở rộng thành các ma trận 4x4

    return split_into_matrices_four(hexxx(split_into_matrices(expanded_key)))


def split_into_matrices_four(data):
    matrices = [data[i : i + 4] for i in range(0, len(data), 4)]
    return matrices


def modify_value(value):
    # Thực hiện thay đổi giá trị theo logic của bạn
    return hex(value)[2:]


def hexxx(lst):
    # Duyệt qua từng cấp và thực hiện thay đổi giá trị
    for i in range(len(lst)):
        for j in range(len(lst[i])):
            lst[i][j] = modify_value(lst[i][j])
    return lst


def nghich_dao_ma_tran(state):
    # Tạo một ma trận mới có kích thước ngược với ma trận đầu vào
    transposed_state = [[0] * len(state) for _ in range(len(state[0]))]

    # Thực hiện chuyển vị
    for i in range(len(state)):
        for j in range(len(state[0])):
            transposed_state[j][i] = state[i][j]

    return transposed_state


def center_window(window, width, height):
    # Lấy thông tin về kích thước màn hình
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()

    # Tính toán vị trí của cửa sổ để nó được ở giữa màn hình
    x = (screen_width - width) // 2
    y = (screen_height - height) // 2

    # Đặt vị trí mới cho cửa sổ
    window.geometry(f"{width}x{height}+{x}+{y}")


def tinhieu_mahoa():
    def create_rounded_label(canvas, widget, text, x, y):
        # Tạo canvas để vẽ hình tròn
        # canvas = tk.Canvas(widget, width=x, height=y, bd=0, highlightthickness=0)
        # canvas.pack()
        # Vẽ hình tròn trên canvas
        canvas.create_oval(0, 0, x, y, outline="black", width=2)
        # Tạo label và đặt nó lên canvas
        label = tk.Label(widget, text=text, font=("", 8))
        canvas.create_window(x // 2, y // 2, window=label)

    def draw_arrow(canvas, length, width, x, y, direction="right"):
        # Tọa độ của đỉnh mũi tên
        arrow_head = []
        if direction == "right":
            arrow_head = [
                x - length,
                y,
                x - length + width,
                y - width,
                x - length + width,
                y + width,
            ]
        elif direction == "left":
            arrow_head = [
                x + length,
                y,
                x + length - width,
                y - width,
                x + length - width,
                y + width,
            ]
        elif direction == "up":
            arrow_head = [
                x,
                y + length,
                x - width,
                y + length - width,
                x + width,
                y + length - width,
            ]
        elif direction == "down":
            arrow_head = [
                x,
                y - length,
                x - width,
                y - length + width,
                x + width,
                y - length + width,
            ]

        # Vẽ thân mũi tên
        if direction in ["left", "right"]:
            canvas.create_line(
                x,
                y,
                x - length if direction == "right" else x + length,
                y,
                width=width,
                arrow=tk.LAST,
                fill="black",
            )
        else:
            canvas.create_line(
                x,
                y,
                x,
                y - length if direction == "up" else y + length,
                width=width,
                arrow=tk.LAST,
                fill="black",
            )

        # Vẽ đầu mũi tên
        canvas.create_polygon(arrow_head, fill="black")

    def hidden(widget):
        manager = widget.winfo_manager()
        if manager == "place":
            widget.place_forget()
        if manager == "grid":
            widget.grid_forget()
        if manager == "pack":
            widget.pack_forget()

    def create_table_4_4(frame):
        labels = [
            [
                tk.Label(
                    frame, text="", borderwidth=1, relief="solid", width=4, height=1
                )
                for _ in range(4)
            ]
            for _ in range(4)
        ]

        # Đặt các nhãn vào bảng
        for i in range(4):
            for j in range(4):
                labels[i][j].grid(row=i, column=j, padx=1, pady=1)
        return labels

    def add_data(list_4_4, tabels):
        for i in range(4):
            for j in range(4):
                tabels[i][j].config(text=list_4_4[i][j])

    def get_data(tables):
        result = []
        for i in range(4):
            row = []
            for j in range(4):
                row.append(tables[i][j].cget("text"))
            result.append(row)
        return result

    def clean_data(tables):
        for i in range(4):
            for j in range(4):
                tables[i][j].config(text="")

    ###########banro
    def sinh_ban_ro():
        ban_ro = "".join([random.choice(data) for _ in range(0, 32)])
        # ban_ro = "a3c5080878a4ffd300ff3636285f0102"
        ban_ro = string_to_state(ban_ro)
        add_data(ban_ro, tables1)

    def move_to_2():
        # Làm biến mất cảnh 1 , giữ lại khối bảng frame1
        hidden(button_ban_ro)
        hidden(button_ma_hoa)
        hidden(button_sinh_khoa)
        hidden(text_key)
        frame1.config(text="Bản rõ")
        center_window(child_window, 550, 330)
        # Tạo các nút bấm mới
        global Start_the_loop
        global Add_Round_Key_c2_btn
        Start_the_loop = tk.Button(
            child_window, text="Bắt đầu thực hiện vòng lặp", command=move_to_3
        )
        Start_the_loop.place(x=170, y=300)

        def add_round_key_c2():
            bab_ro = get_data(tables1)
            khoa = khoa_mo_rong[0]
            reuslt = AddRoundKey(bab_ro, khoa)
            add_data(reuslt, tablesS1)

        Add_Round_Key_c2_btn = tk.Button(
            child_window, text="AddRoundKey", command=add_round_key_c2
        )
        Add_Round_Key_c2_btn.place(x=10, y=300)
        # Khai bảo những bảng mới
        # Tạo bảng Cipher Key
        global tables_cipher_key
        global tablesS1
        global frame2
        global frame3
        global mui1
        global mui2
        global mui3

        frame2 = tk.LabelFrame(child_window, width=50, height=50, text="Cipherkey")
        frame2.place(x=200, y=190)
        tables_cipher_key = create_table_4_4(frame2)
        add_data(khoa_mo_rong[0], tables_cipher_key)
        # Tạo bảng S1
        frame3 = tk.LabelFrame(child_window, width=50, height=50, text="S1")
        frame3.place(x=400, y=40)
        tablesS1 = create_table_4_4(frame3)
        # Tạo hình tròn AddRoundKey
        global hinhAddRoundKey
        hinhAddRoundKey = tk.Canvas(
            child_window, width=100, height=60, bd=0, highlightthickness=0
        )
        hinhAddRoundKey.place(x=220, y=60)
        create_rounded_label(hinhAddRoundKey, child_window, "AddRoundKey", 100, 50)
        # Tất cả mũi tên cảnh 1
        mui1 = tk.Canvas(child_window, width=50, height=50, highlightthickness=0)
        mui2 = tk.Canvas(child_window, width=50, height=50, highlightthickness=0)
        mui3 = tk.Canvas(child_window, width=50, height=50, highlightthickness=0)
        mui1.place(x=165, y=60)
        draw_arrow(mui1, 50, 10, 0, 25, direction="left")
        mui2.place(x=220 + 110, y=60)
        draw_arrow(mui2, 50, 10, 0, 25, direction="left")
        mui3.place(x=245, y=130)
        draw_arrow(mui3, 50, 5, 25, 50, direction="up")

    def move_to_3():
        # Xóa một số widget cũ
        hidden(mui1)
        hidden(mui2)
        hidden(mui3)
        hidden(frame1)
        center_window(child_window, 1500, 500)
        hidden(Add_Round_Key_c2_btn)
        hidden(Start_the_loop)
        hidden(hinhAddRoundKey)
        # Sử dụng lại S1, ô khóa
        x = int(300)
        frame3.place_configure(x=20, y=40)

        add_data(khoa_mo_rong[1], tables_cipher_key)

        frame4 = tk.LabelFrame(child_window, width=50, height=50, text="S_box")
        frame4.place(x=20 + x, y=40)
        tables_s_box = create_table_4_4(frame4)

        frame5 = tk.LabelFrame(child_window, width=50, height=50, text="ShiftRow")
        frame5.place(x=20 + x * 2, y=40)
        tables_shiftrow = create_table_4_4(frame5)

        frame6 = tk.LabelFrame(child_window, width=50, height=50, text="MixColumn")
        frame6.place(x=20 + x * 3, y=40)
        tables_mixcolumn = create_table_4_4(frame6)

        frame7 = tk.LabelFrame(child_window, width=50, height=50, text="S2")
        frame7.place(x=20 + x * 4, y=40)
        tables_s_i_cong_1 = create_table_4_4(frame7)

        frame2.place_configure(x=20 + x * 4 - 150)
        frame2.config(text="Key [1]")

        ###################################################
        # Tạo các label ở trên mũi tên
        label_s_box = tk.Label(child_window, text="S_box")
        label_s_box.place(x=20 + 150 + 50, y=50)
        label_s_box = tk.Label(child_window, text="ShiftRow")
        label_s_box.place(x=20 + x + 150 + 45, y=50)
        label_mix_column = tk.Label(child_window, text="MixCoulmn")
        label_mix_column.place(x=20 + x * 2 + 150 + 45, y=50)
        label_s_box = tk.Label(child_window, text="⊕", font=("Arial", 20))
        label_s_box.place(x=20 + x * 3 + 150 + 55, y=75)

        ##################################################
        # Các nút bấm

        def btn_s_box():
            state_before = get_data(tablesS1)
            result = SubBytes(state_before)
            add_data(result, tables_s_box)
            button_shiftrow.config(state="active")
            button_s_box.config(state="disabled")

        def btn_shiftrow():
            state_before = get_data(tables_s_box)
            result = ShiftRows(state_before)
            add_data(result, tables_shiftrow)
            button_mix_column.config(state="active")
            button_shiftrow.config(state="disabled")

        def btn_mix_column():
            state_before = get_data(tables_shiftrow)
            result = MixColumns(state_before)
            add_data(result, tables_mixcolumn)
            button_add_roundkey.config(state="active")
            button_mix_column.config(state="disabled")

        def btn_add_roundkey():
            state_before = get_data(tables_mixcolumn)
            key_round = get_data(tables_cipher_key)
            result = AddRoundKey(state_before, key_round)
            add_data(result, tables_s_i_cong_1)
            button_next_round.config(state="active")
            button_add_roundkey.config(state="disabled")

        def btn_shiftrow_end():
            state_before = get_data(tables_s_box)
            result = ShiftRows(state_before)
            add_data(result, tables_shiftrow)
            button_add_roundkey.config(state="active")
            button_shiftrow.config(state="disabled")

        def btn_add_round_key_end():
            state_before = get_data(tables_shiftrow)
            key_round = get_data(tables_cipher_key)
            result = AddRoundKey(state_before, key_round)
            add_data(result, tables_s_i_cong_1)
            button_add_roundkey.config(state="disabled")

        key_count = 2
        state_count = 1

        def btn_next_round():
            nonlocal key_count
            nonlocal state_count
            state_before = get_data(tables_s_i_cong_1)
            frame7.config(text=f"S{key_count+1}")
            frame3.config(text=f"S{key_count}")
            frame2.config(text=f"Key [{key_count}]")
            result = state_before
            add_data(result, tablesS1)
            round_key = khoa_mo_rong[key_count]
            add_data(round_key, tables_cipher_key)
            clean_data(tables_s_box)
            clean_data(tables_mixcolumn)
            clean_data(tables_s_i_cong_1)
            clean_data(tables_shiftrow)
            key_count += 1
            state_count += 1
            button_s_box.config(state="active")
            button_next_round.config(state="disabled")
            if state_count == 10:
                hidden(frame6)
                hidden(label_mix_column)
                hidden(button_mix_column)
                hidden(button_next_round)
                hidden(mui7)
                frame7.config(text=f"Bản mã")
                mui5.place_forget()
                mui10 = tk.Canvas(
                    child_window, width=350, height=50, highlightthickness=0
                )
                mui10.place(x=20 + x * 2 + 150, y=70)
                draw_arrow(mui10, 350, 10, 0, 25, direction="left")
                button_end = tk.Button(
                    child_window,
                    text="Kết thúc",
                    command=btn_end,
                    state="active",
                )
                button_end.place(x=10 + 50 + 70 + 500, y=400)
                button_add_roundkey.place_configure(x=10 + 50 + 80, y=400)
                button_add_roundkey.config(command=btn_add_round_key_end)
                button_shiftrow.config(command=btn_shiftrow_end)

        def btn_end():
            child_window.destroy()
            pass

        button_s_box = tk.Button(
            child_window, text="S_box", command=btn_s_box, state="active"
        )
        button_shiftrow = tk.Button(
            child_window, text="ShiftRow", command=btn_shiftrow, state="disabled"
        )
        button_mix_column = tk.Button(
            child_window, text="Mixcolumn", command=btn_mix_column, state="disabled"
        )
        button_add_roundkey = tk.Button(
            child_window,
            text="Add Round Key",
            command=btn_add_roundkey,
            state="disabled",
        )
        button_next_round = tk.Button(
            child_window,
            text="Vòng tiếp theo",
            command=btn_next_round,
            state="disabled",
        )
        button_s_box.place(x=10, y=400)
        button_shiftrow.place(x=10 + 50, y=400)
        button_mix_column.place(x=10 + 50 + 70, y=400)
        button_add_roundkey.place(x=10 + 50 + 70 + 80, y=400)
        button_next_round.place(x=10 + 50 + 70 + 80 + 100, y=400)
        ##########################################################
        # Tạo các mũi tên
        length_arr = 140
        mui4 = tk.Canvas(
            child_window, width=length_arr, height=50, highlightthickness=0
        )
        mui5 = tk.Canvas(
            child_window, width=length_arr, height=50, highlightthickness=0
        )
        mui6 = tk.Canvas(
            child_window, width=length_arr, height=50, highlightthickness=0
        )
        mui7 = tk.Canvas(child_window, width=50, height=50, highlightthickness=0)
        mui8 = tk.Canvas(child_window, width=50, height=50, highlightthickness=0)
        mui9 = tk.Canvas(child_window, width=50, height=50, highlightthickness=0)

        mui4.place(x=20 + x + 150, y=70)
        draw_arrow(mui4, length_arr, 10, 0, 25, direction="left")

        mui5.place(x=20 + x * 2 + 150, y=70)
        draw_arrow(mui5, length_arr, 10, 0, 25, direction="left")

        mui6.place(x=20 + 150, y=70)
        draw_arrow(mui6, length_arr, 10, 0, 25, direction="left")

        mui7.place(x=20 + x * 3 + 150, y=70)
        draw_arrow(mui7, 50, 10, 0, 25, direction="left")

        mui8.place(x=20 + x * 4 - 60, y=70)
        draw_arrow(mui8, 50, 10, 0, 25, direction="left")

        mui9.place(x=20 + x * 4 - 110, y=130)
        draw_arrow(mui9, 50, 5, 25, 50, direction="up")

    def sinh_khoa():
        global khoa_mo_rong
        cipher_key = "".join([random.choice(data) for _ in range(0, 32)])
        # cipher_key = "368ac0f4edcf76a608a3b6783131276e"
        text = ""
        khoa = key_expansion(cipher_key)
        khoa_mo_rong = [nghich_dao_ma_tran(i) for i in khoa]
        for i in range(len(khoa)):
            for j in range(len(khoa[i])):
                for z in range(len(khoa[i][j])):
                    if len(khoa[i][j][z]) == 1:
                        khoa[i][j][z] = f"0{z}"
        khoa = "".join(["".join(y) for x in khoa for y in x])
        text = f"Khóa ban đầu : {khoa[0:32]}\n"
        for i in range(32, len(khoa), 32):
            text += f"Khóa mở rộng [{i //32 }] : {khoa[i:i+32]}\n"

        text_key.config(text=text, anchor="nw", justify="left", font=(14))

    child_window = tk.Toplevel(root)
    child_window.title("Tìm hiểu về quá trình mã hóa")

    center_window(child_window, 900, 450)
    # Cảnh 1
    button_ban_ro = tk.Button(
        child_window, text="Sinh khối dữ liệu bản rõ", command=sinh_ban_ro
    )
    button_ban_ro.place(x=20, y=12)

    button_ma_hoa = tk.Button(
        child_window, text="Thực hiện mã hóa", font=("Arial", 20), command=move_to_2
    )
    button_ma_hoa.place(x=20, y=150, height=200)

    button_sinh_khoa = tk.Button(child_window, text="Sinh khóa", command=sinh_khoa)
    button_sinh_khoa.place(x=300, y=120, width=200)
    # Tạo bảng sinh khóa
    frame1 = tk.LabelFrame(child_window, width=50, height=50)
    frame1.place(x=20, y=40)
    tables1 = create_table_4_4(frame1)
    # Tạo ô chứa khóa mở rộng và khóa ban đầu
    text_key = tk.Label(
        child_window,
        text="",
        borderwidth=1,
        relief="solid",
        width=50,
        height=15,
    )
    text_key.place(x=300, y=150)


def timhieu_sinhkhoa():
    def create_table_4_44(frame):
        # Tạo danh sách 2 chiều chứa các nhãn
        labels = [
            [
                tk.Label(
                    frame, text="", borderwidth=1, relief="solid", width=4, height=1
                )
                for _ in range(44)
            ]
            for _ in range(4)
        ]

        # Đặt các nhãn vào bảng
        for i in range(4):
            for j in range(44):
                labels[i][j].grid(row=i, column=j, padx=1, pady=1)
        return labels

    def create_heading(frame):
        headings = [
            tk.Label(frame, text=f"W{i}", borderwidth=1, width=4, height=1)
            for i in range(44)
        ]
        for i in range(44):
            headings[i].grid(row=0, column=i, padx=1, pady=1)
            if i % 4 == 0 and i != 0:
                headings[i].config(fg="red")

    def add_data(labels_empty, data, word):
        # Đặt dữ liệu vào các nhãn theo số cột
        """labels_empty là chỉ bảng 43 các word hàm sẽ nhập dữ liệu vào word được chỉ đinh vd : w1 , w2"""
        for i in range(4):
            labels_empty[i][word].config(text=data[i])

    def get_data(labels_empty, word):
        """Lấy dữ liệu trong bảng 4x44 với word được chọn mục đích là w i-1 và w i-4"""
        labels_data = []
        for i in range(4):
            labels_data.append(labels_empty[i][word].cget("text"))
        return labels_data

    def create_table_1_4(frame, j):
        labels = [
            tk.Label(frame, text="", borderwidth=1, relief="solid", width=4, height=1)
            for _ in range(4)
        ]
        for i in range(4):
            labels[i].grid(row=j, column=i + 1, padx=1, pady=1)
        return labels

    def add_data_1_4(tables, data):
        for i in range(4):
            tables[i].config(text=data[i])

    def sub_word(word):
        for i in range(4):
            # Get the row and column indices from the current byte value
            row = (word[i] >> 4) & 0xF
            col = word[i] & 0xF
            # Replace the byte with the corresponding value from the S-box
            word[i] = s_box[row * 16 + col]
        return word

    def rot_word(word):
        return word[1:] + [word[0]]

    def xor_words(word1, word2):
        """Hàm thực hiện phép toán XOR giữa hai word"""
        return [(b1 ^ b2) for b1, b2 in zip(word1, word2)]

    def sinhkhoa():
        cipherkey = "".join([random.choice(data) for x in range(0, 32)])
        # cipherkey = "368ac0f4edcf76a608a3b6783131276e"
        cipherkey_show = nghich_dao_ma_tran(string_to_state(cipherkey))
        for i in range(4):
            add_data(labels_empty, cipherkey_show[i], i)

    def close_window():
        child_window.destroy()

    word_count = 4

    def next_word():
        nonlocal word_count
        r_con = [0x01, 0x02, 0x04, 0x08, 0x10, 0x20, 0x40, 0x80, 0x1B, 0x36]
        i = word_count
        # Thêm dữ liệu vào dòng wi
        wi_1 = get_data(labels_empty, i - 1)
        wi_4 = get_data(labels_empty, i - 4)
        temp = [int(x, 16) for x in wi_1]
        if i % 4 == 0:
            add_data_1_4(tables_n_1, wi_1)
            add_data_1_4(tables_n_4, wi_4)
            # Tính g
            temp = rot_word(temp)
            add_data_1_4(tables_rotword, [hex(x)[2:] for x in temp])
            #
            temp = sub_word(temp)
            add_data_1_4(tables_subword, [hex(x)[2:] for x in temp])
            #
            temp = xor_words(temp, [r_con[i // 4 - 1], 0, 0, 0])
            rconi = [hex(r_con[i // 4 - 1])[2:], 0, 0, 0]
            add_data_1_4(tables_rcon, rconi)
            add_data_1_4(tables_rcon_result, [hex(x)[2:] for x in temp])
            temp = xor_words(temp, [int(x, 16) for x in wi_4])
            add_data_1_4(tables_n, [hex(x)[2:] for x in temp])
            label_word_n_1.config(text=f"w{i-1}")
            label_word_n_4.config(text=f"⊕w{i-4}")
            label_word_n.config(text=f"w{i}")
        elif i % 4 != 0:
            add_data_4_1(table2_1, wi_1)
            add_data_4_1(table2_2, wi_4)
            temp = xor_words(temp, [int(x, 16) for x in wi_4])
            add_data_4_1(table2_3, temp)
            label_word_i_1.config(text=f"w{i-1}")
            label_word_i_4.config(text=f"w{i-4}")
            label_word_i.config(text=f"w{i}")

        add_data(labels_empty, [hex(x)[2:] for x in temp], i)

        # Tắt nút sinh khóa:
        btn_sinhkhoa.config(state="disabled")
        if word_count == 43:
            btn_next.config(state="disabled")
            btn_end.config(state="active")
        word_count += 1

    # Tạo cửa sổ phụ
    child_window = tk.Toplevel(root)
    child_window.title("Tìm hiểu trực quan hóa mở rộng khóa AES")

    # Kích thước cửa sổ phụ
    child_window.geometry(f"{screen_width}x{screen_height-350}")

    # Khu vực một: Nút sinh khóa và nút thực hiện mở rộng khóa
    frame1 = tk.Frame(child_window)
    frame1.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")

    btn_sinhkhoa = tk.Button(frame1, text="Sinh khóa", command=sinhkhoa)
    btn_sinhkhoa.grid(row=0, column=0, padx=5, pady=5)

    btn_next = tk.Button(frame1, text="Word tiếp theo", command=next_word)
    btn_next.grid(row=0, column=2, padx=5, pady=5)

    btn_end = tk.Button(
        frame1, text="Kết thúc trực quan hóa", command=close_window, state="disabled"
    )
    btn_end.grid(row=0, column=3, padx=5, pady=5)
    # Khu vực hai: Bảng (ô ma trận 4x4)
    frame2 = tk.Frame(child_window)
    frame2.grid(row=1, column=0, padx=10, pady=10, sticky="nsew")

    # Thiết lập tỷ lệ của frame2
    frame2.grid_rowconfigure(0, weight=1)
    frame2.grid_columnconfigure(0, weight=1)

    # Chia frame 2 làm hai phần
    frame2_1 = tk.Frame(frame2)
    frame2_1.grid(row=0, column=0, padx=10, pady=1, sticky="nsew")
    frame2_2 = tk.Frame(frame2)
    frame2_2.grid(row=1, column=0, padx=10, pady=10, sticky="nsew")

    create_heading(frame2_1)
    labels_empty = create_table_4_44(frame2_2)
    # add_data(labels_empty, ["a", "b", "c", "d"], 1)

    # Khu vực ba: Hai FrameLabel (tính g và tính wi)
    frame3 = tk.Frame(
        child_window,
    )
    frame3.grid(row=2, column=0, padx=10, pady=10, sticky="nsew")
    # Cột 1
    label_frame1 = tk.LabelFrame(
        frame3,
        text="Trường hợp (i-1) % Nk == 0",
    )
    label_word_n_1 = tk.Label(label_frame1, text="word")
    label_word_n_1.grid(row=0, column=0, sticky="w", padx=5, pady=5)

    labelRotword = tk.Label(label_frame1, text="Rotword")
    labelRotword.grid(row=1, column=0, sticky="w", padx=5, pady=5)

    labelSubword = tk.Label(label_frame1, text="Subword")
    labelSubword.grid(row=2, column=0, sticky="w", padx=5, pady=5)

    labelRcon = tk.Label(label_frame1, text="⊕Rcon")
    labelRcon.grid(row=3, column=0, sticky="w", padx=5, pady=5)

    labelg = tk.Label(label_frame1, text="g")
    labelg.grid(row=4, column=0, sticky="w", padx=5, pady=5)

    label_word_n_4 = tk.Label(label_frame1, text="⊕wi-4")
    label_word_n_4.grid(row=5, column=0, sticky="w", padx=5, pady=5)

    label_word_n = tk.Label(label_frame1, text="wi")
    label_word_n.grid(row=7, column=0, sticky="w", padx=5, pady=5)

    tables_n_1 = create_table_1_4(label_frame1, 0)
    tables_rotword = create_table_1_4(label_frame1, 1)
    tables_subword = create_table_1_4(label_frame1, 2)
    tables_rcon = create_table_1_4(label_frame1, 3)
    tables_n_4 = create_table_1_4(label_frame1, 5)
    tables_n = create_table_1_4(label_frame1, 7)
    tables_rcon_result = create_table_1_4(label_frame1, 4)

    label_frame1.grid(row=0, column=0, padx=25, pady=5)
    # add_data_1_4(tables1, [0, 1, 2, 3])
    label_bang = tk.Label(
        label_frame1,
        text="=",
    )
    label_bang.grid(row=6, column=0, padx=25, pady=5, sticky="n")
    # Cột 2
    label_frame2 = tk.LabelFrame(frame3, text="Trường hợp :(i-1) % Nk != 0")

    label_word_i_4 = tk.Label(label_frame2, text="wi-4")
    label_word_i_4.grid(row=0, column=0, padx=5, pady=5)

    label_word_i_1 = tk.Label(label_frame2, text="wi-1")
    label_word_i_1.grid(row=0, column=2, padx=5, pady=5)

    label_word_i = tk.Label(label_frame2, text="wi")
    label_word_i.grid(row=0, column=4, padx=5, pady=5)

    def create_table_4_1(frame, j):
        labels = [
            tk.Label(frame, text="", borderwidth=1, relief="solid", width=4, height=1)
            for _ in range(4)
        ]
        for i in range(4):
            labels[i].grid(row=i + 1, column=j, padx=1, pady=1)
        return labels

    def add_data_4_1(tables, data):
        for i in range(4):
            tables[i].config(text=data[i])

    table2_1 = create_table_4_1(label_frame2, 0)
    table2_2 = create_table_4_1(label_frame2, 2)
    table2_3 = create_table_4_1(label_frame2, 4)
    # add_data_4_1(table2_1, [1, 2, 3, 4])

    kytuxor = tk.Label(label_frame2, text="⊕")
    kytuxor.grid(row=2, column=1, padx=5, pady=5)
    kytubang2 = tk.Label(label_frame2, text="=")
    kytubang2.grid(row=2, column=3, padx=5, pady=5)

    label_frame2.grid(row=0, column=1, padx=5, pady=5)


# Tạo cửa sổ chính
root = tk.Tk()
root.title("Trực quan hóa quy trình mã hóa AES")

# Kích thước cửa sổ chính
root.geometry("400x200")


# Lấy kích thước màn hình
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

# Tính toán vị trí của cửa sổ chính để đặt ở giữa màn hình
x_position = (screen_width - 400) // 2
y_position = (screen_height - 200) // 2

# Đặt vị trí cửa sổ chính
root.geometry(f"400x200+{x_position}+{y_position}")

# Tạo nút "Tìm hiểu về quá trình mã hóa"
btn_mahoa = tk.Button(
    root,
    text="Tìm hiểu về quá trình mã hóa AES",
    command=tinhieu_mahoa,
    font=("Arial", 14),
)
btn_mahoa.pack(side="top", expand=True)

# Tạo nút "Tìm hiểu về quá trình sinh khóa trong AES"
btn_sinhrhoa = tk.Button(
    root,
    text="Tìm hiểu về quá trình sinh khóa trong AES",
    command=timhieu_sinhkhoa,
    font=("Arial", 14),
)
btn_sinhrhoa.pack(side="top", expand=True)

# Chạy vòng lặp chính của cửa sổ
root.mainloop()
