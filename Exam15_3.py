def isPalindrome(raw):
    raw = word = raw.lower()
    for i in raw:
        if ord(i) < 97 or ord(i) > 122:
            word = word.replace(i, "")
    if len(word) < 2:
        return True
    elif word[0] != word[-1]:
        return False
    else:
        return isPalindrome(word[1:-1])


def Palindrome(data):
    if isPalindrome(data):
        print(f"'{data}' is palindrome")
    else:
        print(f"'{data}' is not palindrome")


ip = input("Enter Input : ")
Palindrome(ip)
