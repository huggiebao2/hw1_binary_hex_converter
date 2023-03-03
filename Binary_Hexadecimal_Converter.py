# Convert to binary
def Convert_2_Bin(input_num):
    binary_num = ''
    if input_num == 0:
        binary_num = '0'
    while input_num >= 1:
        # Digits of binary_num are the remainders of the division of 2
        binary_num = str(input_num % 2) + binary_num
        input_num = input_num // 2
    return binary_num

# Convert to hexadecimal
def Convert_2_Hex(input_num):
    # Define hex digits
    hex_digits = {
        0: '0',
        1: '1',
        2: '2',
        3: '3',
        4: '4',
        5: '5',
        6: '6',
        7: '7',
        8: '8',
        9: '9',
        10: 'A',
        11: 'B',
        12: 'C',
        13: 'D',
        14: 'E',
        15: 'F'
    }
    hex_num = ''
    if input_num == 0:
        hex_num = '0'
    while input_num >= 1:
        # Digits of binary_num are the remainders of the division of 16
        hex_num = hex_digits[input_num % 16] + hex_num
        input_num = input_num // 16
    return hex_num
while True:
    while True: 
        # input
        input_num = input('Input an integer (Decimal, from 0~255):')

        # if integer
        try: 
            input_num = int(input_num)
            # if range(0,256)
            if 0 <= input_num <= 255:
                break
            else:
                print('Out of range. Please enter an integer in 0~255.')
                continue

        # if not integer
        except ValueError:
            print( 'Invalid input. Please enter an integer.')
        
    print('You entered: %d' %(input_num))

    print("Binary representation:", Convert_2_Bin(input_num))
    print("Hexadecimal representation:", Convert_2_Hex(input_num))