s="A man, a plan, a canal: Panama"
def palindrome (s):
    l=0
    r=len(s)-1
    while l<r:
        while l<r and not alphnum(s[l]):
            l+=1
        while r>l and not alphnum(s[r]):
            r-=1    
        if s[l].lower()!=s[r].lower():
            return False
        l,r=l+1,r-1
        
    return True
def alphnum(c):
    return (ord('A')<=ord(c)<=ord('Z') or
            ord('a')<=ord(c)<=ord('z') or
            ord('0')<=ord(c)<=ord('9'))

print(palindrome(s))
print(palindrome("0P"))

# Two walkers meet: Start one pointer at beginning (left=0), one at end (right=last char). They walk toward center.

# Skip junk: If left finds space/punctuation, move left forward. If right finds junk, move right backward. Repeat till both find letters/numbers.

# Match check: Compare letters (ignore case). If no match, false. Move inward. Reach middle without mismatch = true!