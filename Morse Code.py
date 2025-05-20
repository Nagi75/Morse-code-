import time

# Morse Code Dictionary
MORSE_CODE_DICT = {
    'A': '.-',    'B': '-...',  'C': '-.-.',
    'D': '-..',   'E': '.',     'F': '..-.',
    'G': '--.',   'H': '....',  'I': '..',
    'J': '.---',  'K': '-.-',   'L': '.-..',
    'M': '--',    'N': '-.',    'O': '---',
    'P': '.--.',  'Q': '--.-',  'R': '.-.',
    'S': '...',   'T': '-',     'U': '..-',
    'V': '...-',  'W': '.--',   'X': '-..-',
    'Y': '-.--',  'Z': '--..',
    '1': '.----', '2': '..---', '3': '...--',
    '4': '....-', '5': '.....', '6': '-....',
    '7': '--...', '8': '---..', '9': '----.',
    '0': '-----', ' ': '/'
}

# Invert the dictionary for decoding
INVERSE_MORSE_DICT = {v: k for k, v in MORSE_CODE_DICT.items()}


def encode_to_morse(text: str) -> str:
    return ' '.join(MORSE_CODE_DICT.get(char.upper(), '?') for char in text)


def decode_from_morse(morse: str) -> str:
    return ''.join(INVERSE_MORSE_DICT.get(code, '?') for code in morse.strip().split())


def greet():
    print("👋 Hey there! Welcome to the Morse Code Buddy.\n")
    time.sleep(1)
    print("You can *encode* your messages into Morse Code, or *decode* them back into English.")
    print("Let’s keep your secrets safe... or just nerd out a bit. 😄\n")


def main():
    greet()
    while True:
        print("\nWhat would you like to do?")
        print("1. Encode text to Morse")
        print("2. Decode Morse to text")
        print("3. Exit")
        choice = input("Pick a number (1/2/3): ").strip()

        if choice == '1':
            text = input("\nType your message: ")
            morse = encode_to_morse(text)
            print("\n📡 Here's your Morse Code:")
            print(morse)
        elif choice == '2':
            morse = input("\nEnter Morse Code (use space between letters, '/' for space):\n> ")
            text = decode_from_morse(morse)
            print("\n🔍 Here's what it says:")
            print(text)
        elif choice == '3':
            print("\n👋 Catch you later! Keep buzzing like Morse.")
            break
        else:
            print("🤔 Hmm, that’s not a valid option. Try again.")

        time.sleep(1.2)


if __name__ == "__main__":
    main()
