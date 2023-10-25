def main():
    pass


def encoder(decoded_string):
    decoded_list = list(decoded_string)

    for i in range (0, len(decoded_list)-1):
        decoded_list[i] += 3
    
    return decoded_list


def decoder(encoded_string):
    encoded_list = list(encoded_string)

    for num in encoded_list:
        num -= 3


if __name__ == "main":
    print(encoder("12345"))