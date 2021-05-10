def palindrome(str):
    """
        Checks if a word is a palindrome
        Prints answer
    """
        
    for i in range(0, int(len(str)/2)):
        if str[i] != str[len(str)-i-1]:
            return False
    return True

string = "kajak"

 
if palindrome(string):
    print("Ten wyraz jest palindromem")
else:
    print("Ten wyraz nie jest palindromem")