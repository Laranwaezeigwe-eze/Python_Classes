def is_palindrome(string):
    reverse = string[::-1]
    return reverse.casefold() == string.casefold()
# print(is_palindrome("eye"))

word = input("enter word to check: ")
if is_palindrome(word):
    print("'{}' is a Palindrome".format(word))
else:
    print("'{}' is not a Palindrome".format(word))
