# 408. Valid Word Abbreviation: Input: word = "kubernetes", abbr = "k8s"  Output: true
# https://leetcode.com/problems/valid-word-abbreviation/

def validWordAbbreviation(word, abbr):
    wi, ai = 0, 0  # Initialize pointers for word and abbreviation
    while wi < len(word) and ai < len(abbr):
        if word[wi] == abbr[ai]:
            wi += 1
            ai += 1
            continue

        if not abbr[ai].isdigit() or abbr[ai] == '0':  # Avoid leading '0'
            return False

        num = 0  # To calculate the number in the abbreviation
        while ai < len(abbr) and abbr[ai].isdigit():
            num = num * 10 + int(abbr[ai])  # Build the numeric value
            ai += 1

        wi += num  # Skip characters in the word based on the number

    return wi == len(word) and ai == len(abbr)