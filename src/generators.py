import random
import string

def generate_random_sequence(name, nChains, minLength, maxLength, alphabet):
    output = ""
    for i in range(nChains):
        output += name+str(i+1)+"\n"
        chainLength = random.choice(range(minLength, maxLength+1))
        # If you try to join a non empty string with this it explodes
        output += "".join(random.choice(alphabet) for _ in range(chainLength))
        output += "\n"

    return output
    
def generate_fasta(nChains, minLength, maxLength, alphabet):
    return generate_random_sequence("> chr", nChains, minLength, maxLength, alphabet)

def generate_fastq(nChains, minLength, maxLength, alphabet):
    return generate_random_sequence("@read", nChains, minLength, maxLength, alphabet)

def main():
    print(generate_fastq(10, 10, 20, string.ascii_lowercase[:26]))

if __name__=='__main__':
    main()