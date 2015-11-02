import string
# print string.ascii_lowercase
#abcdefghijklmnopqrstuvwxyz
# print string.ascii_uppercase
#ABCDEFGHIJKLMNOPQRSTUVWXYZ


def buildCoder(shift):
    """
    Returns a dict that can apply a Caesar cipher to a letter.
    The cipher is defined by the shift value. Ignores non-letter characters
    like punctuation, numbers, and spaces.

    shift: 0 <= int < 26
    returns: dict
    """
    ### TODO 
    Dic = {}
    for i in range(len(string.ascii_lowercase)):
        encrypting_value = (i + shift) % len(string.ascii_lowercase) # or I could write 26
    # Because there are 26 ascii characters
        character = string.ascii_lowercase[i]
        encrypted_character = string.ascii_lowercase[encrypting_value]
        Dic[character] = encrypted_character
        Dic[character.upper()] = encrypted_character.upper()    
    return Dic
    
# Test 1
buildCoder(9)

# Test 2
buildCoder(3)