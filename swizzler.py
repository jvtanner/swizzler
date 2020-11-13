#!/usr/bin/env python3

"""
Stanford CS106A Swizzler project
"""

import sys


def first_part(s):
    """
    Isolate the beginning symbolic characters in the string, if they exist.
    Return them as a string.
    >>> first_part('++jingle')
    '++'
    >>> first_part('k')
    ''
    >>> first_part('')
    ''
    >>> first_part('@$$')
    '@$$'
    """
    prefix = ''
    for i in range(len(s)):
        if not s[i].isalpha():
            prefix += s[i]
        if s[i].isalpha():
            break
    return prefix


def reverse(s):
    """
   Reverses a string.
   >>> reverse('hello')
   'olleh'
   >>> reverse('')
   ''
    """
    result = ''
    for i in range(len(s)):
        result = s[i] + result
    return result


def third_part(s):
    """
    Isolate the final symbols in a string, if they exist.
    Return as a string.
    >>> third_part('hey??')
    '??'
    >>> third_part('hey')
    ''
    """
    suffix = ''
    for i in range(len(s) - 1, len(first_part(s)) - 1, -1):
        if not s[i].isalpha():
            suffix = s[i] + suffix
        if s[i].isalpha():
            break
    return suffix


def swizzle(s):
    """
    Compute and return the swizzled version of string s.
    This is complicated, but can make heavy use of decomposed functions.
    No loops are required in this function.
    >>> swizzle('++Python!')
    '++Pyohtn!'
    >>> swizzle('^^^abcdefg$$$')
    '^^^abfedcg$$$'
    >>> swizzle('^ad-hoc$')
    '^adoh-c$'
    >>> swizzle('$^-@')  # 100% punctuation
    '$^-@'
    >>> swizzle('abcde')
    'abdce'
    >>> swizzle('abcd')
    'abcd'
    >>> swizzle('a')
    'a'
    """
    prefix = first_part(s)
    suffix = third_part(s)
    middle = s[len(prefix):len(s) - len(suffix)]
    # Define the lengths of each part
    if len(middle) <= 4:
        return prefix + middle + suffix
    # If the total length is too small, do not engage the reverse step
    first_two = middle[0:2]
    last_one = middle[len(middle) - 1:]
    reversed_middle = reverse(middle[2:len(middle) - 1])

    return prefix + first_two + reversed_middle + last_one + suffix


def swizzle_file(filename):
    """
    (provided code)
    Print out the contents of the given filename
    with each of its words swizzled.
    Works by splitting each line into "words",
    calling the swizzle() function to compute
    the swizzled version of each word for printing.
    """
    with open(filename, 'r') as f:
        for line in f:
            words = line.split()
            for word in words:
                swizzled = swizzle(word)
                print(swizzled + ' ', end='')
            print()  # print '\n' at end of each line


def main():
    """
    (provided code)
    The 1 command line argument is the file to process.
    Calls swizzle_file() with this filename to print it out.
    """
    args = sys.argv[1:]
    if len(args) == 1:
        swizzle_file(args[0])


# Python boilerplate
if __name__ == '__main__':
    main()
