class translator:

    def deciToRoman(self, num):
        n = num
        ans = ""
        while(n > 0):
            if n >= 1000 and n < 4000:
                ans += "M"
                n -= 1000
            elif n >= 900:
                ans += "CM"
                n -= 900
            elif n >= 500:
                ans += "D"
                n -= 500
            elif n >= 400:
                ans += "CD"
                n -= 400
            elif n >= 100:
                ans += "C"
                n -= 100
            elif n >= 90:
                ans += "XC"
                n -= 90
            elif n >= 50:
                ans += "L"
                n -= 50
            elif n >= 40:
                ans += "XL"
                n -= 40
            elif n >= 10:
                ans += "X"
                n -= 10
            elif n >= 9:
                ans += "IX"
                n -= 9
            elif n >= 5:
                ans += "V"
                n -= 5
            elif n >= 4:
                ans += "IV"
                n -= 4
            elif n >= 1:
                ans += "I"
                n -= 1
        return ans

    def romanToDeci(self, s):
        dic = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
        }
        s = s.replace("IX", "VIIII")
        s = s.replace("IV", "IIII")
        s = s.replace("XC", "LXXXX")
        s = s.replace("XL", "XXXX")
        s = s.replace("CM", "DCCCC")
        s = s.replace("CD", "CCCC")
        num = 0
        for i in s:
            num += dic[i]
        return num


num = int(input("Enter number to translate : "))

print(translator().deciToRoman(num))

print(translator().romanToDeci(translator().deciToRoman(num)))
