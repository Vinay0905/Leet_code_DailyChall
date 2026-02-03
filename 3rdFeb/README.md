# 🧠 LeetCode – Valid Palindrome

**Problem Link:**  

[https://leetcode.com/problems/valid-palindrome/description/](https://leetcode.com/problems/valid-palindrome/description/)

---

## 🔹 Code Approach 1 – Two Pointer Technique

### 💻 Code

```python

s = "A man, a plan, a canal: Panama"

def palindrome(s):
    l = 0
    r = len(s) - 1

    while l < r:
        while l < r and not alphnum(s[l]):
            l += 1
        while r > l and not alphnum(s[r]):
            r -= 1

        if s[l].lower() != s[r].lower():
            return False

        l, r = l + 1, r - 1

    return True

def alphnum(c):
    return (
        ord('A') <= ord(c) <= ord('Z') or
        ord('a') <= ord(c) <= ord('z') or
        ord('0') <= ord(c) <= ord('9')
    )

print(palindrome(s))
print(palindrome("0P"))
```

### 🖼️ Screenshot

![First Approach Submission](Submission1.jpg) *(Insert your submission screenshot here)*

### 🧩 Explanation first approch

- Use two pointers: one from the left, one from the right.
- Skip non-alphanumeric characters.
- Compare characters ignoring case.
- Move inward until mismatch or completion.
- If no mismatch occurs, the string is a palindrome.

---

## 🔹 Code Approach 2 – String Cleaning + Reverse Check

### 💻 Code Approch 2

```python
def isPalindrome(s: str) -> bool:
    temp_s = ''.join(char for char in s if char.isalnum())
    s = temp_s.lower()
    return s == s[::-1]

print(isPalindrome("0P"))
print(isPalindrome("race a car"))
print(isPalindrome("A man, a plan, a canal: Panama"))
```

### 🖼️ Screenshot Second Approach

![Second Approach Submission](Submission2.jpg)

### 🧩 Explanation

- Remove non-alphanumeric characters.
- Convert to lowercase.
- Reverse the string.
- Compare original and reversed strings.
- Matching strings confirm a palindrome.

---

## 📝 Key Takeaways

- Two-pointer approach is space-efficient.
- String cleanup approach is concise and readable.
- Both methods solve the problem effectively.
