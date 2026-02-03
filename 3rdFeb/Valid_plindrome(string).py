
def isPalindrome(s:str) -> bool:
    
    temp_s = ''.join(char for char in s if char.isalnum())
    s = temp_s.lower()
    return s == s[::-1]



print(isPalindrome("0P"))          # False ('p' != '0p')
print(isPalindrome("race a car"))  # False
print(isPalindrome("A man, a plan, a canal: Panama"))  # True

    
    
    
    
# Clean the string: Keep only letters and numbers, make all lowercase (ignore spaces, punctuation).

# Check reverse: See if the cleaned string equals itself backwards (like "racecar" vs "racecar").

# Done: It's a palindrome if they match—fast and easy!