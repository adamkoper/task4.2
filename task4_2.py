string = "KajaK"

def palindrome(str):
    """
        Checks if a word is a palindrome
        Prints answer
    """


    if string.lower().replace(' ','') == string.lower().replace(' ','')[::-1]:
        return True
    else:
        return False

 
if palindrome(string):
    print("Ten wyraz jest palindromem")
else:
    print("Ten wyraz nie jest palindromem")


