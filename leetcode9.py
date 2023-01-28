def isPalindrome(x: int) -> bool:
        string = str(x)
        n = len(string) // 2
        return string[:n] == string[-1:-n-1:-1]


def test():
    assert isPalindrome(x=121) == True
    assert isPalindrome(x=11) == True
    assert isPalindrome(123) == False
