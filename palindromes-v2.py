#This is the Python Essentials 2 LAB 2.5.1.7 Palindromes

def user_input():
    # This function prompts the user and validates the input
    # It returns text in lower case without spaces
    # Now check user input for alphanumeric characters and spaces.
    # Blank strings are not allowed
    while True:
        text = input("Enter one line of text to check (Roman alphabet only): ")
        text = text.replace(" ", "") # spaces are allowed
        if not text.isalpha() or len(text) == 0:
            print("Invalid input. Only alphabetic characters and spaces are allowed.")
        else:
            return text
    

def is_palindrome(text):
    # Main algorithm that accepts string and returns True if string is a palindrome.
    # Palindrome is a word which look the same when read forward and backward.
    # For example, "kayak" is a palindrome, while "loyal" is not.
    if len(text) == 0: return False # blank strings are not allowed
    text = text.lower()             # we will work only with lower case letters
    text = text.replace(" ", "")    # spaces are not taken into account 
    return text == text[::-1]       # simple and elegant solution


def tests():
    # typical function that tries test cases
    print("Self-test ...")
    test_texts = ("Ten animals I slam in a net",
                  "Eleven animals I slam in a net")
    test_results = (True,
                    False)
    for i in range(len(test_texts)):
        txt = test_texts[i]
        result = is_palindrome(txt)
        print(txt, "->", result, end=" ")
        if result == test_results[i]:
                print("OK")
        else:
                print("Failed")


# Main
if __name__ == "__main__":
    text = user_input()
    if is_palindrome(text):
        print("It's a palindrome")
    else:
        print("It's not a palindrome")

##tests() # uncomment to perform self-test
