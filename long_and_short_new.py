def long_and_short (string1, string2):
    '''
    Returns which of two strings is longer or shorter than the other or that they have the same length

        Parameters:
            string1 (str): A string
            string2 (str): Another string

        Returns:
            result (str): A string message saying which of two strings is longer or shorter than the other or that they have the same length
    '''
    if len(string1) > len(string2):
        result = "The longer string is:", string1 + "\nThe shorter string is:", string2
        print("The longer string is:", string1 + "\nThe shorter string is:", string2)
        return result
    if len(string2)> len(string1):
        result = "The longer string is:", string2 + "\nThe shorter string is:", string1
        print("The longer string is:", string2 + "\nThe shorter string is:", string1)
        return result
    if len(string1)==len(string2):
        result = "The two strings have the same length."
        print(result)
        return result

