# mine
def disemvowel(string_):
    string_ = string_.replace("a", "")
    string_ = string_.replace("e", "")
    string_ = string_.replace("i", "")
    string_ = string_.replace("o", "")
    string_ = string_.replace("u", "")
    string_ = string_.replace("A", "")
    string_ = string_.replace("E", "")
    string_ = string_.replace("I", "")
    string_ = string_.replace("O", "")
    string_ = string_.replace("U", "")

    return string_

# Best
def disemvowel(string):
    return "".join(c for c in string if c.lower() not in "aeiou")


print(disemvowel("Test"))
