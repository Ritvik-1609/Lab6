def encoder(decoded_string):
    decoded_list = list(decoded_string)

    for i in range(0, len(decoded_list)):
        decoded_list[i] = int(decoded_list[i])
        decoded_list[i] += 3
        if decoded_list[i] >= 10:
            decoded_list[i] -= 10
            print('less than 10')
        decoded_list[i] = str(decoded_list[i])

    return ''.join(decoded_list)


def decoder(encoded_string):
    encoded_list = list(encoded_string)

    for i in range(0, len(encoded_list)):
        encoded_list[i] = int(encoded_list[i])
        encoded_list[i] -= 3
        if encoded_list[i]<0:
            encoded_list[i] += 10
        encoded_list[i] = str(encoded_list[i])

    return ''.join(encoded_list)


def main():
    user_input = 0
    while user_input != 3:
        print('Enter the password you want to encode or decode')
        password = input()
        print("Would you like to Encode or Decode")
        print('1. Encode')
        print('2. Decode')
        print("3. Quit")
        user_input = int(input())

        if user_input == 1:
            print(encoder(password))
        elif user_input == 2:
            print(decoder(password))
        elif user_input == 3:
            exit(0)
        else:
            print("Invalid")

if __name__ == "__main__":
    main()
