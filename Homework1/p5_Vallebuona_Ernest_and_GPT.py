# p5_Vallebuona_Ernest_and_GPT.py

def caesar_cipher(text, shift):
    result = ""

    for char in text:
        if char.isalpha():
            if char.isupper():
                result += chr((ord(char) - ord('A') + shift) % 26 + ord('A'))
            else:
                result += chr((ord(char) - ord('a') + shift) % 26 + ord('a'))
        else:
            result += char

    return result


def caesar_decipher(cyphertext, shift):
    return caesar_cipher(cyphertext, -shift)


def letter_frequency(text):
    frequency = {}

    for i in range(26):
        frequency[chr(ord('a') + i)] = 0

    for char in text:
        if char.isalpha():
            char = char.lower()
            frequency[char] += 1

    return frequency


def main():
    text = input("Enter a message: ")
    shift = int(input("Enter shift value: "))

    while True:
        print("\n1. Encrypt message")
        print("2. Decrypt message")
        print("3. Show letter frequencies")
        print("4. Show all")
        print("5. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            print("Ciphered text:", caesar_cipher(text, shift))

        elif choice == "2":
            ciphered = caesar_cipher(text, shift)
            print("Ciphered text:", ciphered)
            print("Deciphered text:", caesar_decipher(ciphered, shift))

        elif choice == "3":
            frequency = letter_frequency(text)

            for letter in frequency:
                print(letter + ":", frequency[letter])

        elif choice == "4":
            ciphered = caesar_cipher(text, shift)
            frequency = letter_frequency(text)
            deciphered = caesar_decipher(ciphered, shift)

            print("\nCiphered text:", ciphered)

            print("\nLetter frequencies:")
            for letter in frequency:
                print(letter + ":", frequency[letter])

            print("\nDeciphered text:", deciphered)

        elif choice == "5":
            break

        else:
            print("Invalid choice.")


if __name__ == "__main__":
    main()