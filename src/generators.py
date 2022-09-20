import random
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

def generate_same_before(chainLength, alphabet):
    """
    Returns a string of length='chainLength' made up from random characters from 'alphabet'
    For every character a random float between 0 and 1 is chosen: if it's lower than prob
    the character used for generating the previous character is used
    chainLength: Expects an integer > 0 to determine the length of the string output
    alphabet: A Python list containing all valid characters
    prob: 0.3
    """
    prob = 0.3
    output = ""
    selectedChar = random.choice(alphabet)
    for i in range(chainLength):
        if random.random()>=prob:
            selectedChar = random.choice(alphabet)
        output += selectedChar
    return output

def generate_multiple(chainLength, alphabet):
    """
    Returns a string of length='chainLength' made up from random characters from 'alphabet'
    For every character a random float between 0 and 1 is chosen: if it's lower than prob
    the character is printed n times, where n is a random value between 'minstreak' and 'maxstreak'
    (included)
    chainLength: Expects an integer > 0 to determine the length of the string output
    alphabet: A Python list containing all valid characters
    prob: A probability between 0 and 1 (0.2)
    minstreak: The minimum amount of characters that will appear in a streak (3)
    maxstreak: The maximum amount of characters that will appear in a streak (100)
    """
    prob = 0.2
    minstreak = 3
    maxstreak = 100
    output = ""
    for i in range(chainLength):
        selectedChar = random.choice(alphabet)
        if random.random()>=prob:
            output += selectedChar
        else:
            streakLength = random.choice(range(minstreak, maxstreak+1))
            if streakLength > chainLength-i:
                streakLength = i
            output += "".join(selectedChar for _ in range(streakLength))
            i += streakLength-1
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

def randomRange(min, max):
    if min >= max:
        return min
    else:
        return random.choice(range(min,max))

def generate_chains(nChains, alphabet, method, minLength, maxLength):
    chains = []
    
    for i in range(nChains):
        length = randomRange(minLength, maxLength)
        chains.append(method(length, alphabet))
    
    return chains

def find_border(chain):
    borderPos = 0
    for c in enumerate(chain[1:]):
        if c == chain[borderPos]:
            borderPos += 1
        elif c == chain[0]:
             borderPos = 1
        else:
            borderPos = 0
    
    return borderPos

def __adapt_chain__(chain, pattern, min_matches, max_matches):
    borderPos = len(pattern)-find_border(pattern)

    if len(pattern)*max_matches > len(chain):
        max_matches = len(chain)//len(pattern)

    n_matches = randomRange(min_matches, max_matches)




def adapt_chains(chains, patterns, min_matches, max_matches):
    if isinstance(chains, list):
        for chain, pattern in chains, patterns:
            __adapt_chain__(chain, pattern, min_matches, max_matches)
    else:
        __adapt_chain__(chains, patterns, min_matches, max_matches)
    
    return chains


def output_chains(name, startIndex, file, chains):
    if isinstance(chains, list):
        for i, chain in enumerate(chains):
            file.write(name+str(i+1+startIndex)+'\n')
            file.write(chain+'\n')
        return len(chains)
    else:
        file.write(name+str(1+startIndex)+'\n')
        file.write(chains+'\n')
        return 1


def generate_sam(file, chain, patterns):
    # TODO: generate the sam format. You expect to receive only a chain and a set of patterns in a list. You have to write it on the file using the function 'file.write()'
    pass

def generate_test():
    ALPHABET = ['a', 'c', 'g', 't']
    GENERATION_METHODS = [generate_random_sequence, generate_same_before, generate_multiple, generate_different, generate_fibonacci]
    CHAINS_PER_TYPE = 5

    # Set seed
    random.seed(0)

    fastqChains = []
    if True:
        NAME_FASTQ = "@read"

        MIN_FASTQ_LENGTH = 3
        MAX_FASTQ_LENGTH = 200

        for i in range(10):
            fastqChains.extend(generate_chains(1, ALPHABET, generate_random_sequence, i, i))

        # Generate fastq patterns
        for gen in GENERATION_METHODS:
            fastqChains.extend(generate_chains(CHAINS_PER_TYPE, ALPHABET, gen, MIN_FASTQ_LENGTH, MAX_FASTQ_LENGTH))

        fastq_file = open('fastq.txt', 'w')
        output_chains(NAME_FASTQ, 0, fastq_file, fastqChains)
        fastq_file.close()

    NAME_FASTA = "> chr"

    MIN_FASTA_LENGTH = 2*10**3
    MAX_FASTA_LENGTH = 10**4

    MIN_MATCHES = 0
    MAX_MATCHES = 10

    fasta_file = open('fasta.txt', 'w')
    sam_file = open('sam.txt', 'w')

    fasta_index = 0

    for i in range(10):
        fastaChain = generate_chains(1, ALPHABET, generate_random_sequence, i, i)[0]
        fastaChain = adapt_chains(fastaChain, fastqChains[fasta_index], MIN_MATCHES, MAX_MATCHES)
        generate_sam(sam_file, fastaChain, fastqChains)
        fasta_index += output_chains(NAME_FASTA, fasta_index, fasta_file, fastaChain)

    # Random chains
    for gen in GENERATION_METHODS:
        fastaChains = generate_chains(CHAINS_PER_TYPE, ALPHABET, gen, MIN_FASTA_LENGTH, MAX_FASTA_LENGTH)
        generate_sam(sam_file, fastaChain, fastqChains)
        fasta_index += output_chains(NAME_FASTA, fasta_index, fasta_file, fastaChains)

    fasta_file.close()

def main():
    generate_test()

if __name__=='__main__':
    main()