import random
import string

def generate_random_sequence(chainLength, alphabet):
    """
    Returns a string of length='chainLength' made up from random characters from 'alpabet'
    Arguments:
    chainLength: Expects an integer > 0 to determine the length of the string output
    alphabet: A Python list containing all valid characters
    """
    # If you try to join a non empty string with this it explodes
    output = "".join(random.choice(alphabet) for _ in range(chainLength))
    return output

def generate_same_before(chainLength, alphabet, prob):
    """
    Returns a string of length='chainLength' made up from random characters from 'alphabet'
    For every character a random float between 0 and 1 is chosen: if it's lower than prob
    the character used for generating the previous character is used
    chainLength: Expects an integer > 0 to determine the length of the string output
    alphabet: A Python list containing all valid characters
    prob: A probability between 0 and 1
    """
    output = ""
    selectedChar = random.choice(alphabet)
    for i in range(chainLength):
        if random.random()>=prob:
            selectedChar = random.choice(alphabet)
        output += selectedChar
    return output

def generate_multiple(chainLength, alphabet, prob, minStrike, maxStrike):
    """
    Returns a string of length='chainLength' made up from random characters from 'alphabet'
    For every character a random float between 0 and 1 is chosen: if it's lower than prob
    the character is printed n times, where n is a random value between 'minStrike' and 'maxStrike'
    (included)
    chainLength: Expects an integer > 0 to determine the length of the string output
    alphabet: A Python list containing all valid characters
    prob: A probability between 0 and 1
    minStrike: The minimum amount of characters that will appear in a strike
    maxStrike: The maximum amount of characters that will appear in a strike
    """
    output = ""
    for i in range(chainLength):
        selectedChar = random.choice(alphabet)
        if random.random()>=prob:
            output += selectedChar
        else:
            strikeLength = random.choice(range(minStrike, maxStrike+1))
            if strikeLength > chainLength-i:
                strikeLength = i
            output += "".join(selectedChar for _ in range(strikeLength))
            i += strikeLength-1
    return output

def generate_different(chainLength, alphabet):
    """
    Returns a string of length='chainLength' made up from random characters from 'alphabet'.
    It's ensured that the same character cannot appear two times in a row
    chainLength: Expects an integer > 0 to determine the length of the string output
    alphabet: A Python list containing all valid characters
    """
    output = ""
    prevChar = ""
    for i in range(chainLength):
        selectedChar = random.choice(alphabet)
        while selectedChar==prevChar:
            selectedChar = random.choice(alphabet)
        output += selectedChar
        prevChar = selectedChar
    return output

def generate_chains(name, nChains, minLength, maxLength, alphabet):
    output = ""
    for i in range(nChains):
        chainLength = random.choice(range(minLength, maxLength+1))
        output += name+str(i+1)+"\n"
        output += generate_different(chainLength, alphabet)
        output += "\n"
    return output

def generate_fasta(nChains, minLength, maxLength, alphabet):
    return generate_chains("> chr", nChains, minLength, maxLength, alphabet)

def generate_fastq(nChains, minLength, maxLength, alphabet):
    return generate_chains("@read", nChains, minLength, maxLength, alphabet)

def main():
    print(generate_fastq(10, 10, 20, ['a','c','g','t']))

if __name__=='__main__':
    main()