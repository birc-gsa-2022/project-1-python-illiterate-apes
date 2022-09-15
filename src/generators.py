from itertools import chain
import random
import pickle
from unittest.util import _MAX_LENGTH

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
    for _ in range(chainLength):
        selectedChar = random.choice(alphabet)
        while selectedChar==prevChar:
            selectedChar = random.choice(alphabet)
        output += selectedChar
        prevChar = selectedChar
    return output

def generate_fibonacci(chainLength, alphabet):
    match chainLength:
        case 0:
            return ""
        case 1:
            return random.choice(alphabet)

    a = random.choice(alphabet)
    b = random.choice(alphabet)
    while a==b:
        b = random.choice(alphabet)

    while len(b)<chainLength:
        a, b = b, a + b
    return b[:chainLength]
    


def generate_chains(name, nChains, minLength, maxLength, alphabet):
    output = ""
    for i in range(nChains):
        chainLength = random.choice(range(minLength, maxLength+1))
        output += name+str(i+1)+"\n"
        output += generate_different(chainLength, alphabet)
        output += "\n"
    return output

def generate_fasta():
    ALPHABET = ['a', 'c', 'g', 't']

    NAME = "> chr"
    MIN_LENGTH = 10**3
    MAX_LENGTH = 10**4

    f = open('fasta.txt', 'w')

    # Random chains
    N_CHAINS = 15

    for i in range(N_CHAINS):
        chainLength = random.choice(range(MIN_LENGTH, MAX_LENGTH+1))
        f.write(NAME+str(i+1)+'\n')
        f.write(generate_different(chainLength, ALPHABET)+'\n')
    
    chainsGenerated = N_CHAINS
    # Same as before chains
    N_CHAINS = 10

    for i in range(N_CHAINS):
        chainLength = random.choice(range(MIN_LENGTH, MAX_LENGTH+1))
        f.write(NAME+str(chainsGenerated+i+1)+'\n')
        f.write(generate_same_before(chainLength, ALPHABET, 0.3)+'\n')
    
    chainsGenerated = N_CHAINS
    # Strike chains
    N_CHAINS = 20

    for i in range(N_CHAINS):
        chainLength = random.choice(range(MIN_LENGTH, MAX_LENGTH+1))
        f.write(NAME+str(chainsGenerated+i+1)+'\n')
        f.write(generate_multiple(chainLength, ALPHABET, 0.5, 5, 1000)+'\n')
    
    chainsGenerated = N_CHAINS
    # Different chains
    N_CHAINS = 15

    for i in range(N_CHAINS):
        chainLength = random.choice(range(MIN_LENGTH, MAX_LENGTH+1))
        f.write(NAME+str(chainsGenerated+i+1)+'\n')
        f.write(generate_different(chainLength, ALPHABET)+'\n')
    
    chainsGenerated = N_CHAINS
    # Fibonacci chains
    N_CHAINS = 20

    for i in range(N_CHAINS):
        chainLength = random.choice(range(MIN_LENGTH, MAX_LENGTH+1))
        f.write(NAME+str(chainsGenerated+i+1)+'\n')
        f.write(generate_fibonacci(chainLength, ALPHABET)+'\n')
    
    f.close()


#def generate_fasta(nChains, minLength, maxLength, alphabet):
#    return generate_chains("> chr", nChains, minLength, maxLength, alphabet)

#def generate_fastq(nChains, minLength, maxLength, alphabet):
#    return generate_chains("@read", nChains, minLength, maxLength, alphabet)

def main():
    generate_fasta()
    #print(generate_fastq(10, 10, 20, ['a','c','g','t']))

if __name__=='__main__':
    main()