import random

MISSISSIPPI = True

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

def border_array(x: str) -> list[int]:
    """
    Construct the border array for x.

    >>> border_array("aaba")
    [0, 1, 0, 1]
    >>> border_array("ississippi")
    [0, 0, 0, 1, 2, 3, 4, 0, 0, 1]
    >>> border_array("")
    []
    >>> strict_border_array("abaabaa")
    [0, 0, 1, 1, 2, 3, 4]
    >>> border_array("abcabdabcabc")
    [0, 0, 0, 1, 2, 0, 1, 2, 3, 4, 5, 3]
    """
    if x=="":
        return []
    border_list = [0 for _ in x]
    for i, c in enumerate(x):
        border_index = i
        while True:
            if border_index == 0:
                # border_list[i] = 0 # The list was initialized with zeros
                break
            previousBorder = border_list[border_index-1]
            if c == x[previousBorder]:
                border_list[i] = previousBorder+1
                break
            # We go backwards throughout the border
            border_index = previousBorder
    return border_list

# Returns the border length of the last border in the given string
def lastBorder(x):
    border = border_array(x)
    index = len(border)-1
    if index<0:
        return 0
    else:
        return border[index]

def findPattern(chain, pattern):
    patternIndexes = []
    start = 0
    while True:
        start = chain.find(pattern, start) + 1
        if start > 0:
            patternIndexes.append(start)
        else:
            return patternIndexes

def embedString(base, insertion, index):
    return base[:index] + insertion + base[index+len(insertion):]

def __adapt_chain__(chain, pattern, min_matches, max_matches):
    if chain == "" or pattern == "":
        return chain

    if len(pattern)*max_matches > len(chain):
        max_matches = len(chain)//len(pattern)

    n_matches = randomRange(min_matches, max_matches)

    currentMatches = len(findPattern(pattern, chain))

    if currentMatches < n_matches:
        # Random probabilities of a match at the beginning and at the end (20% each)
        beginMatch = random.random() > 0.8
        if beginMatch:
            chain[:len(pattern)] = pattern
            currentMatches = len(findPattern(pattern, chain))

        if currentMatches >= n_matches: return chain

        endMatch = random.random() > 0.8
        if endMatch:
            chain[-len(pattern):] = pattern
            currentMatches = len(findPattern(pattern, chain))
        
        if currentMatches >= n_matches: return chain

        # Force having two patterns in the chain with overlapping solutions if possible.
        # If not, simply put them one after the other.
        # Chance of this happening on purpose: 20%
        overlappingMatches = random.random() > 0.8
        if currentMatches>0 and overlappingMatches:
            selectedMatch = random.choice(range(currentMatches))
            borderPos = lastBorder(pattern)
            indexSelectedMatch = findPattern(pattern, chain)[selectedMatch]
            # Special case when selecting the last match (we put the pattern before the string instead of after)
            if selectedMatch == currentMatches-1:
                # Overlap before the final string
                positionModification = indexSelectedMatch-len(pattern)*2+borderPos
                embedString(chain, pattern, positionModification)
            else:
                # Overlap after the string
                positionModification = indexSelectedMatch+len(pattern)+borderPos
                embedString(chain, pattern, positionModification)

        currentMatches = len(findPattern(pattern, chain))
        # Chain modification loop
        rangeIndexes = range(0, 1)
        if len(chain)-len(pattern) > 0:
            rangeIndexes = range(len(chain)-len(pattern))
            print("Hola")
        while currentMatches < n_matches:
            print(currentMatches)
            randomIndex = random.choice(rangeIndexes)
            embedString(chain, pattern, randomIndex)
            currentMatches = len(findPattern(pattern, chain))
    
    return chain


def adapt_chains(chains, patterns, min_matches, max_matches):
    if isinstance(chains, list):
        for chain, pattern in chains, patterns:
            __adapt_chain__(chain, pattern, min_matches, max_matches)
    else:
        __adapt_chain__(chains, patterns, min_matches, max_matches)
    
    return chains


def output_chains(name, startIndex, file, chains):
    if isinstance(chains, list):
        chainNames = [name+str(i+1+startIndex) for i in range(len(chains))]
        for i, chain in enumerate(chains):
            file.write(chainNames[i]+'\n')
            file.write(chain+'\n')
        return chainNames
    else:
        chainName = name+str(1+startIndex)
        file.write(chainName+'\n')
        file.write(chains+'\n')
        return [chainName]


def generate_sam(file, fasta, fastaName, fastq, fastqNames):
    # TODO: generate the sam format. You expect to receive only a fasta (with his name in fastaName) and a set of patterns in a list (fastq). The names of these patterns are into another list called fastqNames. You have to write it on the file using the function 'file.write()'
    pass

def generate_test():
    ALPHABET = ['m', 'i', 's', 'p']
    GENERATION_METHODS = [generate_random_sequence, generate_same_before, generate_multiple, generate_different, generate_fibonacci]
    CHAINS_PER_TYPE = 5

    # Set seed
    random.seed(0)

    fastqNames = None
    fastqChains = []
    if MISSISSIPPI:
        fastqChains = ['ississippi']
    
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
        fastqNames = output_chains(NAME_FASTQ, 0, fastq_file, fastqChains)
        fastq_file.close()

    NAME_FASTA = "> chr"

    MIN_FASTA_LENGTH = 2*10**3
    MAX_FASTA_LENGTH = 10**4

    MIN_MATCHES = 0
    MAX_MATCHES = 10

    fasta_file = open('fasta.txt', 'w')
    sam_file = open('sam.txt', 'w')

    fasta_index = 0
    if MISSISSIPPI:
        chain = 'ississippi'
        nameFasta = output_chains(NAME_FASTA, 0, fasta_file, chain)[0]
        generate_sam(sam_file, chain, nameFasta, fastqChains, fastqNames)
        fasta_index = 1

    for i in range(10):
        fastaChain = generate_chains(1, ALPHABET, generate_random_sequence, i, i)[0]
        fastaChain = adapt_chains(fastaChain, fastqChains[fasta_index], MIN_MATCHES, MAX_MATCHES)
        nameFasta = output_chains(NAME_FASTA, fasta_index, fasta_file, fastaChain)[0]
        generate_sam(sam_file, fastaChain, nameFasta, fastqChains, fastqNames)
        fasta_index += 1

    # Random chains
    for gen in GENERATION_METHODS:
        fastaChains = generate_chains(CHAINS_PER_TYPE, ALPHABET, gen, MIN_FASTA_LENGTH, MAX_FASTA_LENGTH)
        for fastaChain in fastaChains:
            #fastaChain = adapt_chains(fastaChain, fastqChains[fasta_index], MIN_MATCHES, MAX_MATCHES)
            nameFasta = output_chains(NAME_FASTA, fasta_index, fasta_file, fastaChain)[0]
            generate_sam(sam_file, fastaChain, nameFasta, fastqChains, fastqNames)
            fasta_index += 1

    fasta_file.close()

def main():
    generate_test()

if __name__=='__main__':
    main()