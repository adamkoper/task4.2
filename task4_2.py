string = "KajaK"

def palindrome(str):
    """
        Checks if a word is a palindrome
        Prints answer
    """
<<<<<<< HEAD
    
    string.lower().replace(' ','')[::-1]
    if string.lower().replace(' ','') == string.lower().replace(' ','')[::-1]:
        return True
    else:
        return False
=======
        
    for i in range(0, int(len(str)/2)):
        if str[i] != str[len(str)-i-1]:
            return False
    return True
>>>>>>> main


 
if palindrome(string):
    print("Ten wyraz jest palindromem")
else:
    print("Ten wyraz nie jest palindromem")


