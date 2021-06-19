DICT_POLYNOMIAL = {'CRC-1' : [1, 0],
                    'CRC-4' : [4, 1, 0],
                    'CRC-7' : [7, 3, 0],
                    'CRC-8' : [8, 7, 6, 4, 2, 0],
                    'CRC-10' : [10, 9, 5, 4, 1, 0],
                    'CRC-11' : [11, 9, 8, 7, 2, 0]
                    }


def get_coefficient(binary_data: str) -> list:
    """
    IN: '1010000111'
    OUT: [9, 7, 2, 1, 0]
    """
    coefficients = []
    size_data = len(binary_data)
    for x in range(size_data):
        if int(binary_data[x]):
            coefficients.append(size_data - x - 1)
    return coefficients


def get_binary(coefficients: list) -> str:
    """
    IN: [11, 9, 8, 7, 2, 0]
    OUT: '101110000101'

    # coefficients[0] - max in list
    """
    invert_coeff = [coefficients[0] - i for i in coefficients]
    binary_data = ''
    for i in range(coefficients[0] + 1):
        if i in invert_coeff:
            binary_data += '1'
        else:
            binary_data += '0'
    return binary_data


def text_to_bin(text: str) -> list:
    return [format(ord(i), 'b') for i in text]


def bin_to_text(binary_text: list) -> str:
    return ''.join([chr(int(i, base=2)) for i in binary_text])


def cyclic_coder(fl_txt: str, divisor_polinom: str) -> str:
    tmp_xor = ''
    for j in range(len(fl_txt)):
        if int(fl_txt[j]):
            index = j
            fl_txt = fl_txt[j:]
            break
    numerator = fl_txt[:len(divisor_polinom)]
    for i in range(len(fl_txt) - len(divisor_polinom)+1):
        if numerator[0] == '0' and i != 0:
            for j in range(len(divisor_polinom)):
                tmp_xor += str(int(numerator[j]) ^ 0)
        else:
            for j in range(len(divisor_polinom)):
                tmp_xor += str(int(numerator[j]) ^ int(divisor_polinom[j]))
        left_half = tmp_xor[1:]
        try:
            right_half = fl_txt[i + len(divisor_polinom)]
        except:
            right_half = fl_txt[i + len(divisor_polinom)-1]
            polinom = (left_half + right_half)[:-1]
            return fl_txt[:len(fl_txt)-len(polinom)], polinom
        numerator = left_half + right_half
        tmp_xor = ''

if __name__ == '__main__':
    polynomials_name = 'CRC-8'
    array_q = '10101001010110101011'
    
    coeff_q = get_coefficient(array_q)
    array_p = get_binary(DICT_POLYNOMIAL[polynomials_name])
    multiply_q_coeff = [int(i) + max(DICT_POLYNOMIAL[polynomials_name]) for i in coeff_q]
    multiply_q_array = get_binary(multiply_q_coeff)
    data, crc = cyclic_coder(multiply_q_array, array_p)
    print(f'Code for {data} = {crc}')
