import math
""" isUnique
Implement an algorithm if a string has all unique characters.
"""

def is_unique(s):
    verify = {}
    for l in s:
        if verify.get(l, False) == False:
            verify[l] = True
        else:
            return False
    return True


""" permutation
Given two string, write a method to decide if a string is a permutation of the other
"""

def permutation(s1, s2):
    check = {}
    for l in s1:
        check[l] = check.get(l, 0) + 1
    for l in s2:
        check[l] = check.get(l, 0) - 1
    if sum(check.values()) == 0:
        return True
    return False


""" Palindrome permutation
Given a string, write a function to check if it is a permutation of a palindrome.
"""

def palindrome_permutation(s):
    check = {}
    for l in s:
        check[l] = check.get(l, False) ^ True
    tmp = [b for b in check.values() if b]
    if len(check.values())%2 == 1 and len(tmp) == 1:
        return True
    elif len(tmp) == 0:
        return True
    else:
        return False


""" One away
There are three types of edits that can be perform on strings:
- insert a character
- remove a character
- replace a character.
Given two string, write a function to check if they are one (or zero) edit away.
"""

def one_away(s1, s2):
    if len(s1) > len(s2):
        return one_away(s2, s1)

    previous_row = range(len(s2) + 1)
    for i, l1 in enumerate(s1):
        current_row = [i +1]
        for j, l2 in enumerate(s2):
            insert = previous_row[j+1] + 1
            delete = current_row[j] + 1
            sub = previous_row[j] + (l1 != l2)
            current_row.append(min(insert, delete, sub))
        previous_row = current_row
    if previous_row[-1] > 1:
        return False
    return True

""" string compression
Implement a method to perform basic string compression using the count of repeated characters.
aabcccccaaa => a2b1c5a3
"""

def string_compression(s1):
    cnt, current = 0, ''
    res = ''
    for l in s1:
        if current == '':
            current = l
        elif l != current:
            res += "%s%d" % (current, cnt)
            cnt = 0
            current = l
        cnt += 1
    res += "%s%d" % (current, cnt)
    if len(res) < len(s1):
        return res
    else:
        return s1



""" Rotate Matrix
Given a image represented by an N*N matrix, where each pixel in the page is 4 byte, write a method to rotate the image by 90 degrees. Can you do this in place ?
"""

def rotate_matrix(matrix, n):
    x = n / 2
    for i in xrange(x+1):
        for j in xrange(x):
            normal = matrix[i][j]
            gauche = matrix[j][n-i-1]
            droite = matrix[n-j-1][i]
            opposite = matrix[n-i-1][n-j-1]
            matrix[i][j], matrix[j][n-i-1], matrix[n-i-1][n-j-1], matrix[n-j-1][i] = matrix[n-j-1][i], matrix[i][j], matrix[j][n-i-1], matrix[n-i-1][n-j-1]
    return matrix


""" Zero matrix
Write an algorithm such that if an element in a MxN matrix is 0, the entire row and column are set to 0
"""

def zero_matrix(matrix):
    indexes = {
        "x": set(),
        "y": set()
    }
    for i in xrange(len(matrix)):
        for j in xrange(len(matrix[0])):
            if matrix[i][j] == 0:
                indexes["x"].add(i)
                indexes["y"].add(j)
    for i in xrange(len(matrix)):
        for j in xrange(len(matrix[0])):
            if i in indexes["x"] or j in indexes["y"]:
                matrix[i][j] = 0
    return matrix


""" String Rotation
Assume you have a method isSubstring which check if one word is a substring of another.
Given two strings, s1 and s2, write code to check if s2 is a rotation of s1 using only one isSubstring
example waterbottle is a rotation of erbottlewat
"""

def string_rotation(s1, s2):
    if len(s1) != len(s2):
        return False
    return s2 in (s1 + s1)



print "is unique true", is_unique("qwertyuiop") == True
print "is unique false", is_unique("qwertrewq") == False

print "permutation kakatoa oatakak", permutation("kakatoa", "oatakak") == True
print "permutation qweerqwe oatakak", permutation("qweerqwe", "oatakak") == False

print "palindrome permutation taco cat", palindrome_permutation("taco cato") == True
print "palindrome permutation qwerty", palindrome_permutation("qwerty") == False

print "one away pale pal", one_away("pale", "pal") == True
print "one away pale bale", one_away("pale", "bale") == True
print "one away pale bal", one_away("pale", "bal") == False

print "string compression aabcccccaaa", string_compression("aabcccccaaa") == "a2b1c5a3"

test = [
    [1, 2, 3, 4, 11],
    [34, 5, 6, 15, 12],
    [33, 36, 7, 16, 13],
    [32, 35, 26, 25, 14],
    [31, 24, 23, 22, 21],
]

check = [
    [31, 32, 33, 34, 1],
    [24, 35, 36, 5, 2],
    [23, 26, 7, 6, 3],
    [22, 25, 16, 15, 4],
    [21, 14, 13, 12, 11],
]

print "rotate matrix test 5", rotate_matrix(test, 5) == check

print "zero matrix [0, 1, 2], [1, 2, 3], [3, 2, 0]", zero_matrix([[0, 1, 2], [1, 2, 3], [3, 2, 1]]) == [[0, 0, 0], [0, 2, 3], [0, 2, 1]]

print "string rotation waterbottle erbottlewat", string_rotation("waterbottle", "erbottlewat") == True
print "string rotation waterbottle erbotltewat", string_rotation("waterbottle", "erbotltewat") == False
