# TO TRANSLATE NORMAL ENGLISH TO THE SECRET CODE

# CODING:
# IF THE WORD CONTAINS AT LEAST 3 CHARACTERS, REMOVE THE FIRST LETTER AND APPEND IT AT THE END
# NOW APPEND THREE RANDOM CHARACTERS AT THE STARTING AND THE END
# ELSE:
# SIMPLY REVERSE THE STRING

# DECODING:
# IF THE WORD CONTAIN LESS THAN 3 CHARACTERS, REVERSE IT
# ELSE:
# REMOVE 3 RANDOM CHARACTERS FROM START AND END.NOW REMOVE THE LAST LETTER AND APPEND IT TO THE BEGINNING
# YOUR PROGRAMME SHOULD ASK WHETHER YOU WANT TO CODE OR DECODE


import random


def secret_code():
    end_start = "qwertyuioplkjhgfdsazxcvbnmMNBVCXZASDFGHJKLPOIUYTREWQ"

    # Taking input
    message = input("Enter the message: ").strip()
    if not message:
        print("Error: Empty input! Please enter a valid message.")
        return

    words = message.split()
    choice = input("Enter 1 for Coding or 0 for Decoding: ").strip()

    if choice == "1":  # Encoding
        encoded_words = []
        for word in words:
            if len(word) >= 3:
                prefix = ''.join(random.choices(end_start, k=3))
                suffix = ''.join(random.choices(end_start, k=3))
                new_word = prefix + word[1:] + word[0] + suffix
                encoded_words.append(new_word)
            else:
                encoded_words.append(word[::-1])  # Reverse small words
        print("Encoded Message:", " ".join(encoded_words))

    elif choice == "0":  # Decoding
        decoded_words = []
        for word in words:
            if len(word) >= 3:
                core_word = word[3:-3]  # Removing random characters
                decoded_word = core_word[-1] + core_word[:-1]
                decoded_words.append(decoded_word)
            else:
                decoded_words.append(word[::-1])  # Reverse small words
        print("Decoded Message:", " ".join(decoded_words))

    else:
        print("Invalid choice! Enter 1 to encode or 0 to decode.")


# Run the function
secret_code()