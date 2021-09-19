def check_palindrome(str1):
    return str1 == str1[::-1]


def palindromeindex(s):
    if check_palindrome(s):
        return -1
    else:
        ind = []
        z = len(s)-1
        for y in range(len(s)):
            if s[y] != s[z]:
                ind.append(y)
                ind.append(z)
            z -= 1
            if y==z:
                break

        res = -1
        for x in ind:
            if x+1 != len(s):
                if check_palindrome(s[x+1:]):
                    res = x
                if check_palindrome(s[:x]):
                    res = x
            else:
                if check_palindrome(s[:x]):
                    res = x

        return res


inp = ['aaab', 'baa', 'aaa']
for i in range(len(inp)):
    print(palindromeindex(inp[i]))
