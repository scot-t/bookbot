def count_words(text):
    """
    Returns the integer count of the words in text input
    """
    count = len(text.split())
    return count

def get_char_frequency(text):
    """
    Returns a dictionary of all characters occurring in the string and the number of times they occurred
    """
    frequency = {}

    for c in text:
        c = c.lower() 
        # check - does c.lower() return the value or just modify the string - yes it does
        # check - does this result in strings if output is a number?
        if c not in frequency:
            frequency[c] = 0
        frequency[c] += 1 
        # check - does this result in 1 if value is not set yet?
    return frequency


def count_chars(text):
    """
    Return a list of dictionaries of char:count, sorted high-low by count.
    """
    # lesson note: since a dictionary is unsorted, we return a list of dictionaries.
    # do we use dictionaries over tuples so we can sort by key? could you sort a list of tuples?

    index = []
    char_freq = get_char_frequency(text)

    for item in char_freq:
        if item.isalpha():
            index.append({
                "char": item,
                "count": char_freq[item]
                })

    def sort_on(items):
        return items["count"]

    index.sort(reverse=True, key=sort_on)

    return index

