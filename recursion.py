def fibonnaci(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fibonnaci(n - 1) + fibonnaci(n - 2)


def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)


def compareTo(s1, s2):
    if s1 == "" and s2 == "":
        return 0
    if s1 == "":
        return -1
    if s2 == "":
        return 1
    if s1[0] != s2[0]:
        return ord(s1[0]) - ord(s2[0])
    return compareTo(s1[1:], s2[1:])