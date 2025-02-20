def long_and_short (string1, string2):
    if len(string1) > len(string2):
        print ("The longer string is:", string1)
        print ("The shorter string is:", string2)
    if len(string2)> len(string1):
        print ("The longer string is:", string2)
        print ("The shorter string is:", string1)
    if len(string1)==len(string2):
        print ("The two strings have the same length.")

long_and_short ("five", "six")
long_and_short ("kick", "five")
long_and_short ("in", "extra")
