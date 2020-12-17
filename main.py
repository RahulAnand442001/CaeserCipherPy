from art import logo

alphabet = [
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o',
    'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd',
    'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's',
    't', 'u', 'v', 'w', 'x', 'y', 'z'
]

print(f"{logo} \n")


def caeser(message, shiftAmount, directionType):
    cypher_message = ""
    for letter in message:
        if letter not in alphabet:
            cypher_message += letter
        else:
            letterIndex = alphabet.index(letter)
            if (directionType == "encode"):
                newPosition = letterIndex + shiftAmount
            elif (directionType == "decode"):
                newPosition = letterIndex - shiftAmount
            cypher_message += alphabet[newPosition]
    print(f"Your {directionType}d message is {cypher_message} !")


should_Continue = True

while should_Continue:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    proper_shift = shift % len(alphabet)
    caeser(message=text, shiftAmount=proper_shift, directionType=direction)
    res = input("Want to Try Again ? Type Yes or No ! \n").lower()

    if res == "no":
        should_Continue = False
        print("GoodBye !")
