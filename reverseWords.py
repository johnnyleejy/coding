def reverseWords(s: str) -> str:
    result = ''
    curr = ''
    for char in s:
        # isalnum is O(1) time complexity
        if char.isalnum():
            curr += char
        else:
            # If encounter a special character, reverse current string and append to result
            result += curr[::-1]
            # Append the special character as per normal and reset curr string
            result += char
            curr = ''
    result += curr[::-1] + ' '
    # We don't need the last appended space in result
    return result[:-1]


# Tests
assert("gnirtS; eb2 desrever..." == reverseWords("String; 2be reversed..."))
assert("god,tac. olleh.!?" == reverseWords("dog,cat. hello.!?"))
assert("yM $yenoM si ruoy yenoM?!" == reverseWords("My $Money is your Money?!"))
assert("yadoT's etaD si: 10/90/3202" == reverseWords("Today's Date is: 01/09/2023"))
assert("erehT era ruof secaps retfa siht:     DNE" == reverseWords("There are four spaces after this:     END"))
assert("tolA fo laiceps sretcarahc\n \t ekil siht" == reverseWords("Alot of special characters\n \t like this"))
assert("  secaps2_erofeb_dna_retfa   dne!" == reverseWords("  2spaces_before_and_after   end!"))
