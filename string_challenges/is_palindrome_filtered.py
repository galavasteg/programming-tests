"""
Write a function that filter string from excluded chars
and check if a string is the palindrome.
'vnm,  ..mnv.'  # True
'vnm,  ..mv.'   # False
'.='            # True
''              # True
"""

DEPRECATED_CHARS = '_ ,.!?-=;:'


def is_palindrome(s: str, exclude_chars=DEPRECATED_CHARS) -> bool:
    """
    >>> is_palindrome('abccba')
    True
    >>> is_palindrome('abcabc')
    False
    >>> is_palindrome('') == True
    True
    >>> is_palindrome('_-------__') == True
    True
    >>> is_palindrome('a_b.c,D.c-b.a;')
    True
    >>> is_palindrome('a_b.c,D.c-b.a;a')
    False
    >>> is_palindrome('_ ,.!?vnm,  ..mnv.')
    True
    >>> is_palindrome('_ ,.!?-=;: aba')
    True
    >>> is_palindrome(' A_ ,.!?-=;: ')
    True

    """
    l_ind, r_ind = 0, len(s) - 1

    while True:
        while l_ind < len(s) and s[l_ind] in exclude_chars:
            l_ind += 1
        while r_ind >= 0 and s[r_ind] in exclude_chars:
            r_ind -= 1

        if l_ind > r_ind:
            return True
        elif s[l_ind] == s[r_ind]:
            l_ind += 1
            r_ind -= 1
        else:
            return False
