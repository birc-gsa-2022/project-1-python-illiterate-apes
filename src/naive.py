"""Implementation of the naive exact matching algorithm."""

import argparse
import fasta
import fastq

def naive(read, genome):
    length = len(read[1])
    for i in range(len(genome[1]) - len(read[1]) + 1):
        for j in range(len(read[1])):
            if genome[1][i + j] != read[1][j]:
                break
        else:
            print(f"{read[0]}\t{genome[0]}\t{i + 1}\t{length}M\t{read[1]}")

        

def main():
    argparser = argparse.ArgumentParser(
        description="Exact matching using the naive method")
    argparser.add_argument("genome", type=argparse.FileType('r'))
    argparser.add_argument("reads", type=argparse.FileType('r'))
    args = argparser.parse_args()
    genomes = fasta.fasta_parse(args.genome)
    reads = fastq.fastq_parser(args.reads)

    for r in reads: 
        for g in genomes:
            naive(r, g)
    


if __name__ == '__main__':
    main()
