"""
    Copyright (C) 2012 Bo Zhu http://about.bozhu.me
    Permission is hereby granted, free of charge, to any person obtaining a
    copy of this software and associated documentation files (the "Software"),
    to deal in the Software without restriction, including without limitation
    the rights to use, copy, modify, merge, publish, distribute, sublicense,
    and/or sell copies of the Software, and to permit persons to whom the
    Software is furnished to do so, subject to the following conditions:
    The above copyright notice and this permission notice shall be included in
    all copies or substantial portions of the Software.
    THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
    IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
    FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL
    THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
    LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING
    FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER
    DEALINGS IN THE SOFTWARE.
"""

Sbox = (
    0x63, 0x7C, 0x77, 0x7B, 0xF2, 0x6B, 0x6F, 0xC5, 0x30, 0x01, 0x67, 0x2B, 0xFE, 0xD7, 0xAB, 0x76,
    0xCA, 0x82, 0xC9, 0x7D, 0xFA, 0x59, 0x47, 0xF0, 0xAD, 0xD4, 0xA2, 0xAF, 0x9C, 0xA4, 0x72, 0xC0,
    0xB7, 0xFD, 0x93, 0x26, 0x36, 0x3F, 0xF7, 0xCC, 0x34, 0xA5, 0xE5, 0xF1, 0x71, 0xD8, 0x31, 0x15,
    0x04, 0xC7, 0x23, 0xC3, 0x18, 0x96, 0x05, 0x9A, 0x07, 0x12, 0x80, 0xE2, 0xEB, 0x27, 0xB2, 0x75,
    0x09, 0x83, 0x2C, 0x1A, 0x1B, 0x6E, 0x5A, 0xA0, 0x52, 0x3B, 0xD6, 0xB3, 0x29, 0xE3, 0x2F, 0x84,
    0x53, 0xD1, 0x00, 0xED, 0x20, 0xFC, 0xB1, 0x5B, 0x6A, 0xCB, 0xBE, 0x39, 0x4A, 0x4C, 0x58, 0xCF,
    0xD0, 0xEF, 0xAA, 0xFB, 0x43, 0x4D, 0x33, 0x85, 0x45, 0xF9, 0x02, 0x7F, 0x50, 0x3C, 0x9F, 0xA8,
    0x51, 0xA3, 0x40, 0x8F, 0x92, 0x9D, 0x38, 0xF5, 0xBC, 0xB6, 0xDA, 0x21, 0x10, 0xFF, 0xF3, 0xD2,
    0xCD, 0x0C, 0x13, 0xEC, 0x5F, 0x97, 0x44, 0x17, 0xC4, 0xA7, 0x7E, 0x3D, 0x64, 0x5D, 0x19, 0x73,
    0x60, 0x81, 0x4F, 0xDC, 0x22, 0x2A, 0x90, 0x88, 0x46, 0xEE, 0xB8, 0x14, 0xDE, 0x5E, 0x0B, 0xDB,
    0xE0, 0x32, 0x3A, 0x0A, 0x49, 0x06, 0x24, 0x5C, 0xC2, 0xD3, 0xAC, 0x62, 0x91, 0x95, 0xE4, 0x79,
    0xE7, 0xC8, 0x37, 0x6D, 0x8D, 0xD5, 0x4E, 0xA9, 0x6C, 0x56, 0xF4, 0xEA, 0x65, 0x7A, 0xAE, 0x08,
    0xBA, 0x78, 0x25, 0x2E, 0x1C, 0xA6, 0xB4, 0xC6, 0xE8, 0xDD, 0x74, 0x1F, 0x4B, 0xBD, 0x8B, 0x8A,
    0x70, 0x3E, 0xB5, 0x66, 0x48, 0x03, 0xF6, 0x0E, 0x61, 0x35, 0x57, 0xB9, 0x86, 0xC1, 0x1D, 0x9E,
    0xE1, 0xF8, 0x98, 0x11, 0x69, 0xD9, 0x8E, 0x94, 0x9B, 0x1E, 0x87, 0xE9, 0xCE, 0x55, 0x28, 0xDF,
    0x8C, 0xA1, 0x89, 0x0D, 0xBF, 0xE6, 0x42, 0x68, 0x41, 0x99, 0x2D, 0x0F, 0xB0, 0x54, 0xBB, 0x16,
)

InvSbox = (
    0x52, 0x09, 0x6A, 0xD5, 0x30, 0x36, 0xA5, 0x38, 0xBF, 0x40, 0xA3, 0x9E, 0x81, 0xF3, 0xD7, 0xFB,
    0x7C, 0xE3, 0x39, 0x82, 0x9B, 0x2F, 0xFF, 0x87, 0x34, 0x8E, 0x43, 0x44, 0xC4, 0xDE, 0xE9, 0xCB,
    0x54, 0x7B, 0x94, 0x32, 0xA6, 0xC2, 0x23, 0x3D, 0xEE, 0x4C, 0x95, 0x0B, 0x42, 0xFA, 0xC3, 0x4E,
    0x08, 0x2E, 0xA1, 0x66, 0x28, 0xD9, 0x24, 0xB2, 0x76, 0x5B, 0xA2, 0x49, 0x6D, 0x8B, 0xD1, 0x25,
    0x72, 0xF8, 0xF6, 0x64, 0x86, 0x68, 0x98, 0x16, 0xD4, 0xA4, 0x5C, 0xCC, 0x5D, 0x65, 0xB6, 0x92,
    0x6C, 0x70, 0x48, 0x50, 0xFD, 0xED, 0xB9, 0xDA, 0x5E, 0x15, 0x46, 0x57, 0xA7, 0x8D, 0x9D, 0x84,
    0x90, 0xD8, 0xAB, 0x00, 0x8C, 0xBC, 0xD3, 0x0A, 0xF7, 0xE4, 0x58, 0x05, 0xB8, 0xB3, 0x45, 0x06,
    0xD0, 0x2C, 0x1E, 0x8F, 0xCA, 0x3F, 0x0F, 0x02, 0xC1, 0xAF, 0xBD, 0x03, 0x01, 0x13, 0x8A, 0x6B,
    0x3A, 0x91, 0x11, 0x41, 0x4F, 0x67, 0xDC, 0xEA, 0x97, 0xF2, 0xCF, 0xCE, 0xF0, 0xB4, 0xE6, 0x73,
    0x96, 0xAC, 0x74, 0x22, 0xE7, 0xAD, 0x35, 0x85, 0xE2, 0xF9, 0x37, 0xE8, 0x1C, 0x75, 0xDF, 0x6E,
    0x47, 0xF1, 0x1A, 0x71, 0x1D, 0x29, 0xC5, 0x89, 0x6F, 0xB7, 0x62, 0x0E, 0xAA, 0x18, 0xBE, 0x1B,
    0xFC, 0x56, 0x3E, 0x4B, 0xC6, 0xD2, 0x79, 0x20, 0x9A, 0xDB, 0xC0, 0xFE, 0x78, 0xCD, 0x5A, 0xF4,
    0x1F, 0xDD, 0xA8, 0x33, 0x88, 0x07, 0xC7, 0x31, 0xB1, 0x12, 0x10, 0x59, 0x27, 0x80, 0xEC, 0x5F,
    0x60, 0x51, 0x7F, 0xA9, 0x19, 0xB5, 0x4A, 0x0D, 0x2D, 0xE5, 0x7A, 0x9F, 0x93, 0xC9, 0x9C, 0xEF,
    0xA0, 0xE0, 0x3B, 0x4D, 0xAE, 0x2A, 0xF5, 0xB0, 0xC8, 0xEB, 0xBB, 0x3C, 0x83, 0x53, 0x99, 0x61,
    0x17, 0x2B, 0x04, 0x7E, 0xBA, 0x77, 0xD6, 0x26, 0xE1, 0x69, 0x14, 0x63, 0x55, 0x21, 0x0C, 0x7D,
)

LUT_2 = [0x00, 0x02, 0x04, 0x06, 0x08, 0x0a, 0x0c, 0x0e, 0x10, 0x12, 0x14, 0x16, 0x18, 0x1a, 0x1c, 0x1e,
         0x20, 0x22, 0x24, 0x26, 0x28, 0x2a, 0x2c, 0x2e, 0x30, 0x32, 0x34, 0x36, 0x38, 0x3a, 0x3c, 0x3e,
         0x40, 0x42, 0x44, 0x46, 0x48, 0x4a, 0x4c, 0x4e, 0x50, 0x52, 0x54, 0x56, 0x58, 0x5a, 0x5c, 0x5e,
         0x60, 0x62, 0x64, 0x66, 0x68, 0x6a, 0x6c, 0x6e, 0x70, 0x72, 0x74, 0x76, 0x78, 0x7a, 0x7c, 0x7e,
         0x80, 0x82, 0x84, 0x86, 0x88, 0x8a, 0x8c, 0x8e, 0x90, 0x92, 0x94, 0x96, 0x98, 0x9a, 0x9c, 0x9e,
         0xa0, 0xa2, 0xa4, 0xa6, 0xa8, 0xaa, 0xac, 0xae, 0xb0, 0xb2, 0xb4, 0xb6, 0xb8, 0xba, 0xbc, 0xbe,
         0xc0, 0xc2, 0xc4, 0xc6, 0xc8, 0xca, 0xcc, 0xce, 0xd0, 0xd2, 0xd4, 0xd6, 0xd8, 0xda, 0xdc, 0xde,
         0xe0, 0xe2, 0xe4, 0xe6, 0xe8, 0xea, 0xec, 0xee, 0xf0, 0xf2, 0xf4, 0xf6, 0xf8, 0xfa, 0xfc, 0xfe,
         0x1b, 0x19, 0x1f, 0x1d, 0x13, 0x11, 0x17, 0x15, 0x0b, 0x09, 0x0f, 0x0d, 0x03, 0x01, 0x07, 0x05,
         0x3b, 0x39, 0x3f, 0x3d, 0x33, 0x31, 0x37, 0x35, 0x2b, 0x29, 0x2f, 0x2d, 0x23, 0x21, 0x27, 0x25,
         0x5b, 0x59, 0x5f, 0x5d, 0x53, 0x51, 0x57, 0x55, 0x4b, 0x49, 0x4f, 0x4d, 0x43, 0x41, 0x47, 0x45,
         0x7b, 0x79, 0x7f, 0x7d, 0x73, 0x71, 0x77, 0x75, 0x6b, 0x69, 0x6f, 0x6d, 0x63, 0x61, 0x67, 0x65,
         0x9b, 0x99, 0x9f, 0x9d, 0x93, 0x91, 0x97, 0x95, 0x8b, 0x89, 0x8f, 0x8d, 0x83, 0x81, 0x87, 0x85,
         0xbb, 0xb9, 0xbf, 0xbd, 0xb3, 0xb1, 0xb7, 0xb5, 0xab, 0xa9, 0xaf, 0xad, 0xa3, 0xa1, 0xa7, 0xa5,
         0xdb, 0xd9, 0xdf, 0xdd, 0xd3, 0xd1, 0xd7, 0xd5, 0xcb, 0xc9, 0xcf, 0xcd, 0xc3, 0xc1, 0xc7, 0xc5,
         0xfb, 0xf9, 0xff, 0xfd, 0xf3, 0xf1, 0xf7, 0xf5, 0xeb, 0xe9, 0xef, 0xed, 0xe3, 0xe1, 0xe7, 0xe5]

LUT_3 = [0x00, 0x03, 0x06, 0x05, 0x0c, 0x0f, 0x0a, 0x09, 0x18, 0x1b, 0x1e, 0x1d, 0x14, 0x17, 0x12, 0x11,
         0x30, 0x33, 0x36, 0x35, 0x3c, 0x3f, 0x3a, 0x39, 0x28, 0x2b, 0x2e, 0x2d, 0x24, 0x27, 0x22, 0x21,
         0x60, 0x63, 0x66, 0x65, 0x6c, 0x6f, 0x6a, 0x69, 0x78, 0x7b, 0x7e, 0x7d, 0x74, 0x77, 0x72, 0x71,
         0x50, 0x53, 0x56, 0x55, 0x5c, 0x5f, 0x5a, 0x59, 0x48, 0x4b, 0x4e, 0x4d, 0x44, 0x47, 0x42, 0x41,
         0xc0, 0xc3, 0xc6, 0xc5, 0xcc, 0xcf, 0xca, 0xc9, 0xd8, 0xdb, 0xde, 0xdd, 0xd4, 0xd7, 0xd2, 0xd1,
         0xf0, 0xf3, 0xf6, 0xf5, 0xfc, 0xff, 0xfa, 0xf9, 0xe8, 0xeb, 0xee, 0xed, 0xe4, 0xe7, 0xe2, 0xe1,
         0xa0, 0xa3, 0xa6, 0xa5, 0xac, 0xaf, 0xaa, 0xa9, 0xb8, 0xbb, 0xbe, 0xbd, 0xb4, 0xb7, 0xb2, 0xb1,
         0x90, 0x93, 0x96, 0x95, 0x9c, 0x9f, 0x9a, 0x99, 0x88, 0x8b, 0x8e, 0x8d, 0x84, 0x87, 0x82, 0x81,
         0x9b, 0x98, 0x9d, 0x9e, 0x97, 0x94, 0x91, 0x92, 0x83, 0x80, 0x85, 0x86, 0x8f, 0x8c, 0x89, 0x8a,
         0xab, 0xa8, 0xad, 0xae, 0xa7, 0xa4, 0xa1, 0xa2, 0xb3, 0xb0, 0xb5, 0xb6, 0xbf, 0xbc, 0xb9, 0xba,
         0xfb, 0xf8, 0xfd, 0xfe, 0xf7, 0xf4, 0xf1, 0xf2, 0xe3, 0xe0, 0xe5, 0xe6, 0xef, 0xec, 0xe9, 0xea,
         0xcb, 0xc8, 0xcd, 0xce, 0xc7, 0xc4, 0xc1, 0xc2, 0xd3, 0xd0, 0xd5, 0xd6, 0xdf, 0xdc, 0xd9, 0xda,
         0x5b, 0x58, 0x5d, 0x5e, 0x57, 0x54, 0x51, 0x52, 0x43, 0x40, 0x45, 0x46, 0x4f, 0x4c, 0x49, 0x4a,
         0x6b, 0x68, 0x6d, 0x6e, 0x67, 0x64, 0x61, 0x62, 0x73, 0x70, 0x75, 0x76, 0x7f, 0x7c, 0x79, 0x7a,
         0x3b, 0x38, 0x3d, 0x3e, 0x37, 0x34, 0x31, 0x32, 0x23, 0x20, 0x25, 0x26, 0x2f, 0x2c, 0x29, 0x2a,
         0x0b, 0x08, 0x0d, 0x0e, 0x07, 0x04, 0x01, 0x02, 0x13, 0x10, 0x15, 0x16, 0x1f, 0x1c, 0x19, 0x1a]


def divide_by_3(x):
    for i in range(256):
        if LUT_3[i] == x:
            return i

    return -1


def divide_by_2(x):
    for i in range(256):
        if LUT_2[i] == x:
            return i

    return -1

# learnt from http://cs.ucsb.edu/~koc/cs178/projects/JT/aes.c


def xtime(a): return (((a << 1) ^ 0x1B) & 0xFF) if (a & 0x80) else (a << 1)


Rcon = (
    0x00, 0x01, 0x02, 0x04, 0x08, 0x10, 0x20, 0x40,
    0x80, 0x1B, 0x36, 0x6C, 0xD8, 0xAB, 0x4D, 0x9A,
    0x2F, 0x5E, 0xBC, 0x63, 0xC6, 0x97, 0x35, 0x6A,
    0xD4, 0xB3, 0x7D, 0xFA, 0xEF, 0xC5, 0x91, 0x39,
)


def text2matrix(text):
    matrix = []
    for i in range(16):
        byte = (text >> (8 * (15 - i))) & 0xFF
        if i % 4 == 0:
            matrix.append([byte])
        else:
            matrix[int(i / 4)].append(byte)
    return matrix


def matrix2text(matrix):
    text = 0
    for i in range(4):
        for j in range(4):
            text |= (matrix[i][j] << (120 - 8 * (4 * i + j)))
    return text


class AES:
    def __init__(self, master_key):
        self.change_key(master_key)

    def change_key(self, master_key):
        self.round_keys = text2matrix(master_key)
        # print self.round_keys

        for i in range(4, 4 * 11):
            self.round_keys.append([])
            if i % 4 == 0:
                byte = self.round_keys[i - 4][0]        \
                    ^ Sbox[self.round_keys[i - 1][1]]  \
                    ^ Rcon[int(i / 4)]
                self.round_keys[i].append(byte)

                for j in range(1, 4):
                    byte = self.round_keys[i - 4][j]    \
                        ^ Sbox[self.round_keys[i - 1][(j + 1) % 4]]
                    self.round_keys[i].append(byte)
            else:
                for j in range(4):
                    byte = self.round_keys[i - 4][j]    \
                        ^ self.round_keys[i - 1][j]
                    self.round_keys[i].append(byte)

        # print self.round_keys

    def encrypt(self, plaintext):
        self.plain_state = text2matrix(plaintext)

        self.__add_round_key(self.plain_state, self.round_keys[:4])

        for i in range(1, 10):
            self.__round_encrypt(
                self.plain_state, self.round_keys[4 * i: 4 * (i + 1)])

        self.__sub_bytes(self.plain_state)
        self.__shift_rows(self.plain_state)
        self.__add_round_key(self.plain_state, self.round_keys[40:])

        return matrix2text(self.plain_state)

    def decrypt(self, ciphertext):
        self.cipher_state = text2matrix(ciphertext)

        self.__add_round_key(self.cipher_state, self.round_keys[40:])
        self.__inv_shift_rows(self.cipher_state)
        self.__inv_sub_bytes(self.cipher_state)

        for i in range(9, 0, -1):
            self.__round_decrypt(
                self.cipher_state, self.round_keys[4 * i: 4 * (i + 1)])

        self.__add_round_key(self.cipher_state, self.round_keys[:4])

        return matrix2text(self.cipher_state)

    def __add_round_key(self, s, k):
        for i in range(4):
            for j in range(4):
                s[i][j] ^= k[i][j]

    def __round_encrypt(self, state_matrix, key_matrix):
        self.__sub_bytes(state_matrix)
        self.__shift_rows(state_matrix)
        self.__mix_columns(state_matrix)
        self.__add_round_key(state_matrix, key_matrix)

    def __round_decrypt(self, state_matrix, key_matrix):
        self.__add_round_key(state_matrix, key_matrix)
        self.__inv_mix_columns(state_matrix)
        self.__inv_shift_rows(state_matrix)
        self.__inv_sub_bytes(state_matrix)

    def __sub_bytes(self, s):
        for i in range(4):
            for j in range(4):
                s[i][j] = Sbox[s[i][j]]

    def __inv_sub_bytes(self, s):
        for i in range(4):
            for j in range(4):
                s[i][j] = InvSbox[s[i][j]]

    def __shift_rows(self, s):
        s[0][1], s[1][1], s[2][1], s[3][1] = s[1][1], s[2][1], s[3][1], s[0][1]
        s[0][2], s[1][2], s[2][2], s[3][2] = s[2][2], s[3][2], s[0][2], s[1][2]
        s[0][3], s[1][3], s[2][3], s[3][3] = s[3][3], s[0][3], s[1][3], s[2][3]

    def __inv_shift_rows(self, s):
        s[0][1], s[1][1], s[2][1], s[3][1] = s[3][1], s[0][1], s[1][1], s[2][1]
        s[0][2], s[1][2], s[2][2], s[3][2] = s[2][2], s[3][2], s[0][2], s[1][2]
        s[0][3], s[1][3], s[2][3], s[3][3] = s[1][3], s[2][3], s[3][3], s[0][3]

    def __mix_single_column(self, a):
        # please see Sec 4.1.2 in The Design of Rijndael
        t = a[0] ^ a[1] ^ a[2] ^ a[3]
        u = a[0]
        a[0] ^= t ^ xtime(a[0] ^ a[1])
        a[1] ^= t ^ xtime(a[1] ^ a[2])
        a[2] ^= t ^ xtime(a[2] ^ a[3])
        a[3] ^= t ^ xtime(a[3] ^ u)

    def __mix_columns(self, s):
        for i in range(4):
            self.__mix_single_column(s[i])

    def __inv_mix_columns(self, s):
        # see Sec 4.1.3 in The Design of Rijndael
        for i in range(4):
            u = xtime(xtime(s[i][0] ^ s[i][2]))
            v = xtime(xtime(s[i][1] ^ s[i][3]))
            s[i][0] ^= u
            s[i][1] ^= v
            s[i][2] ^= u
            s[i][3] ^= v

        self.__mix_columns(s)

    def PrintLastRoundKey(self):
        lastrkey = matrix2text(self.round_keys[40:])
        hexlastrkey = '{0:032x}'.format(lastrkey)
        print("0x"+hexlastrkey.upper())

    def GetLastRoundKey(self):
        return (self.round_keys[40:])


key = 0x101a1e3a5df3403cc751114111daa222
aes_obj = AES(key)

CT = text2matrix(0xd8fdc9b896a929cb33df86b634e0dc04)
CT_f = text2matrix(0x32622c1f5deed912b18a59996444273f)
CT1 = text2matrix(0xaa5e77e2064d15e14babd14f5feafa77)
CT1_f = text2matrix(0xb7565eced22c123b2d6e2fc9101d2315)
ans = [[0, 0, 0, 0] for i in range(4)]


def get_possible_values_K00_K31_K22_K13(CT, CT_f):
    possible_keys1 = []
    for K00 in range(256):
        for K31 in range(256):
            l1 = InvSbox[K00 ^ CT[0][0]] ^ InvSbox[K00 ^ CT_f[0][0]]
            l1 = divide_by_2(l1)
            l2 = InvSbox[K31 ^ CT[3][1]] ^ InvSbox[K31 ^ CT_f[3][1]]
            if(l1 == l2):
                possible_keys1.append([K00, K31])

    possible_keys2 = []
    for K22 in range(256):
        for K13 in range(256):
            l3 = InvSbox[K22 ^ CT[2][2]] ^ InvSbox[K22 ^ CT_f[2][2]]
            l4 = InvSbox[K13 ^ CT[1][3]] ^ InvSbox[K13 ^ CT_f[1][3]]
            l4 = divide_by_3(l4)
            if(l3 == l4):
                possible_keys2.append([K22, K13])

    possible_values = []
    for K00, K31 in possible_keys1:
        for K22, K13 in possible_keys2:
            l1 = InvSbox[K00 ^ CT[0][0]] ^ InvSbox[K00 ^ CT_f[0][0]]
            l1 = divide_by_2(l1)
            l2 = InvSbox[K31 ^ CT[3][1]] ^ InvSbox[K31 ^ CT_f[3][1]]
            l3 = InvSbox[K22 ^ CT[2][2]] ^ InvSbox[K22 ^ CT_f[2][2]]
            l4 = InvSbox[K13 ^ CT[1][3]] ^ InvSbox[K13 ^ CT_f[1][3]]
            l4 = divide_by_3(l4)
            if(l1 == l2 and l1 == l3 and l1 == l4):
                if(l2 == l3 and l2 == l4):
                    if(l3 == l4):
                        possible_values.append([K00, K31, K22, K13])
    return possible_values


def get_possible_values_K10_K01_K32_K23(CT, CT_f):
    possible_keys1 = []
    for K10 in range(256):
        for K01 in range(256):
            l1 = InvSbox[K10 ^ CT[1][0]] ^ InvSbox[K10 ^ CT_f[1][0]]
            l2 = InvSbox[K01 ^ CT[0][1]] ^ InvSbox[K01 ^ CT_f[0][1]]
            if(l1 == l2):
                possible_keys1.append([K10, K01])

    possible_keys2 = []
    for K32 in range(256):
        for K23 in range(256):
            l3 = InvSbox[K32 ^ CT[3][2]] ^ InvSbox[K32 ^ CT_f[3][2]]
            l4 = InvSbox[K23 ^ CT[2][3]] ^ InvSbox[K23 ^ CT_f[2][3]]
            l3 = divide_by_3(l3)
            l4 = divide_by_2(l4)
            if(l3 == l4):
                possible_keys2.append([K32, K23])

    possible_values = []
    for K10, K01 in possible_keys1:
        for K32, K23 in possible_keys2:
            l1 = InvSbox[K10 ^ CT[1][0]] ^ InvSbox[K10 ^ CT_f[1][0]]
            l2 = InvSbox[K01 ^ CT[0][1]] ^ InvSbox[K01 ^ CT_f[0][1]]
            l3 = InvSbox[K32 ^ CT[3][2]] ^ InvSbox[K32 ^ CT_f[3][2]]
            l4 = InvSbox[K23 ^ CT[2][3]] ^ InvSbox[K23 ^ CT_f[2][3]]
            l3 = divide_by_3(l3)
            l4 = divide_by_2(l4)
            if(l1 == l2 and l1 == l3 and l1 == l4):
                if(l2 == l3 and l2 == l4):
                    if(l3 == l4):
                        possible_values.append([K10, K01, K32, K23])
    return possible_values


def get_possible_values_K20_K11_K02_K33(CT, CT_f):
    possible_keys1 = []
    for K20 in range(256):
        for K11 in range(256):
            l1 = InvSbox[K20 ^ CT[2][0]] ^ InvSbox[K20 ^ CT_f[2][0]]
            l2 = InvSbox[K11 ^ CT[1][1]] ^ InvSbox[K11 ^ CT_f[1][1]]
            l2 = divide_by_3(l2)
            if(l1 == l2):
                possible_keys1.append([K20, K11])

    possible_keys2 = []
    for K02 in range(256):
        for K33 in range(256):
            l3 = InvSbox[K02 ^ CT[0][2]] ^ InvSbox[K02 ^ CT_f[0][2]]
            l4 = InvSbox[K33 ^ CT[3][3]] ^ InvSbox[K33 ^ CT_f[3][3]]
            l3 = divide_by_2(l3)
            if(l3 == l4):
                possible_keys2.append([K02, K33])

    possible_values = []
    for K20, K11 in possible_keys1:
        for K02, K33 in possible_keys2:
            l1 = InvSbox[K20 ^ CT[2][0]] ^ InvSbox[K20 ^ CT_f[2][0]]
            l2 = InvSbox[K11 ^ CT[1][1]] ^ InvSbox[K11 ^ CT_f[1][1]]
            l2 = divide_by_3(l2)
            l3 = InvSbox[K02 ^ CT[0][2]] ^ InvSbox[K02 ^ CT_f[0][2]]
            l3 = divide_by_2(l3)
            l4 = InvSbox[K33 ^ CT[3][3]] ^ InvSbox[K33 ^ CT_f[3][3]]
            if(l1 == l2 and l1 == l3 and l1 == l4):
                if(l2 == l3 and l2 == l4):
                    if(l3 == l4):
                        possible_values.append([K20, K11, K02, K33])
    return possible_values


def get_possible_values_K30_K21_K12_K03(CT, CT_f):
    possible_keys1 = []
    for K30 in range(256):
        for K21 in range(256):
            l1 = InvSbox[K30 ^ CT[3][0]] ^ InvSbox[K30 ^ CT_f[3][0]]
            l2 = InvSbox[K21 ^ CT[2][1]] ^ InvSbox[K21 ^ CT_f[2][1]]
            l1 = divide_by_3(l1)
            l2 = divide_by_2(l2)
            if(l1 == l2):
                possible_keys1.append([K30, K21])

    possible_keys2 = []
    for K12 in range(256):
        for K03 in range(256):
            l3 = InvSbox[K12 ^ CT[1][2]] ^ InvSbox[K12 ^ CT_f[1][2]]
            l4 = InvSbox[K03 ^ CT[0][3]] ^ InvSbox[K03 ^ CT_f[0][3]]
            if(l3 == l4):
                possible_keys2.append([K12, K03])

    possible_values = []
    for K30, K21 in possible_keys1:
        for K12, K03 in possible_keys2:
            l1 = InvSbox[K30 ^ CT[3][0]] ^ InvSbox[K30 ^ CT_f[3][0]]
            l2 = InvSbox[K21 ^ CT[2][1]] ^ InvSbox[K21 ^ CT_f[2][1]]
            l1 = divide_by_3(l1)
            l2 = divide_by_2(l2)
            l3 = InvSbox[K12 ^ CT[1][2]] ^ InvSbox[K12 ^ CT_f[1][2]]
            l4 = InvSbox[K03 ^ CT[0][3]] ^ InvSbox[K03 ^ CT_f[0][3]]
            if(l1 == l2 and l1 == l3 and l1 == l4):
                if(l2 == l3 and l2 == l4):
                    if(l3 == l4):
                        possible_values.append([K30, K21, K12, K03])
    return possible_values


p1 = get_possible_values_K00_K31_K22_K13(CT, CT_f)
p2 = get_possible_values_K00_K31_K22_K13(CT1, CT1_f)
p3 = get_possible_values_K10_K01_K32_K23(CT, CT_f)
p4 = get_possible_values_K10_K01_K32_K23(CT1, CT1_f)
p5 = get_possible_values_K20_K11_K02_K33(CT, CT_f)
p6 = get_possible_values_K20_K11_K02_K33(CT1, CT1_f)
p7 = get_possible_values_K30_K21_K12_K03(CT, CT_f)
p8 = get_possible_values_K30_K21_K12_K03(CT1, CT1_f)

p = []
for i in p1:
    for j in p2:
        if i == j:
            p.append(j)
assert(len(p) == 1)
p = p[0]
ans[0][0] = p[0]
ans[3][1] = p[1]
ans[2][2] = p[2]
ans[1][3] = p[3]

p = []
for i in p3:
    for j in p4:
        if i == j:
            p.append(j)
assert(len(p) == 1)
p = p[0]
ans[1][0] = p[0]
ans[0][1] = p[1]
ans[3][2] = p[2]
ans[2][3] = p[3]

p = []
for i in p5:
    for j in p6:
        if i == j:
            p.append(j)
assert(len(p) == 1)
p = p[0]
ans[2][0] = p[0]
ans[1][1] = p[1]
ans[0][2] = p[2]
ans[3][3] = p[3]

p = []
for i in p7:
    for j in p8:
        if i == j:
            p.append(j)
assert(len(p) == 1)
p = p[0]
ans[3][0] = p[0]
ans[2][1] = p[1]
ans[1][2] = p[2]
ans[0][3] = p[3]


def pretty(text):
    hexlastrkey = '{0:032x}'.format(text)
    return ("0x"+hexlastrkey.upper())


print("Actual Last Round Key: ", pretty(
    matrix2text(aes_obj.GetLastRoundKey())))
print("Predicted Last Round Key: ", pretty(matrix2text(ans)))
assert(ans == aes_obj.GetLastRoundKey())