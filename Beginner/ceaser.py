import math
goAgain = True
while goAgain:
    alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    def ceaser(start_text,shift_number,direction):
            message = ""
            if shift_number > 26:
                shift_number %= 26
                print(shift_number)
            if direction =="decode":
                shift_number *=-1
            for letter in start_text:
                if letter in alphabet:

                    index = alphabet.index(letter)
                    new_index = index + shift_number
                    new_letter = alphabet[new_index]
                    message +=new_letter
                else:
                    message+=letter
            print(f"{direction}d message is {message}")
    
    ceaser(text,shift,direction)
    rollover = input("Do you want to try again? 'yes' or 'no'\n").lower()
    if rollover == "no":
        goAgain = False
        print("Good bye")
