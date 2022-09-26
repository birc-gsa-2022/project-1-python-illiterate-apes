"""Implementation of a linear time exact matching algorithm."""

import argparse
import fasta
import fastq
from generators import border_array

# def border_array(x: str) -> list[int]:
#     """
#     Construct the border array for x.

#     >>> border_array("aaba")
#     [0, 1, 0, 1]
#     >>> border_array("ississippi")
#     [0, 0, 0, 1, 2, 3, 4, 0, 0, 1]
#     >>> border_array("")
#     []
#     """
#     ba = [0] * len(x)
#     for i in range(len(x)):
#         if i == 0:
#             continue
#         if x[ba[i-1]] == x[i]:
#             ba[i] = ba[i-1] + 1

#     return ba

def linear(read, genome):
    ba = border_array(read[1])
    i = 0
    j = 0
    n = len(genome[1])
    m = len(read[1])
    out = []
    if read[1] == "" or genome[1] == "":
        return out
    while (j < n):
        while i < m and j < n and genome[1][j] == read[1][i]:
            j += 1
            i += 1

        if i == m:
            out.append(f"{read[0]}\t{genome[0]}\t{j - m + 1}\t{m}M\t{read[1]}")

        if i == 0:
            j += 1
        else:
            i = ba[i - 1]
    
    return out



def main():
    argparser = argparse.ArgumentParser(
        description="Exact matching in linear time")
    argparser.add_argument("genome", type=argparse.FileType('r'))
    argparser.add_argument("reads", type=argparse.FileType('r'))
    args = argparser.parse_args()
    genomes = fasta.fasta_parse(args.genome)
    reads = fastq.fastq_parser(args.reads)

    result = []
    for r in reads: 
        for g in genomes:
            out = linear(r,g)
            for o in out:
                print(o)
            #print(linear(r,g))
    


if __name__ == '__main__':
    main()
