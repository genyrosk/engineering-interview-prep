"""
A gene string can be represented by an 8-character long string, with
choices from 'A', 'C', 'G', and 'T'.

Suppose we need to investigate a mutation from a gene string startGene
to a gene string endGene where one mutation is defined as one single
character changed in the gene string.

For example, "AACCGGTT" --> "AACCGGTA" is one mutation.
There is also a gene bank bank that records all the valid gene mutations.
A gene must be in bank to make it a valid gene string.

Given the two gene strings startGene and endGene and the gene bank bank,
return the minimum number of mutations needed to mutate from startGene to
endGene. If there is no such a mutation, return -1.

Note that the starting point is assumed to be valid, so it might not be
included in the bank.


Example 1:

Input: startGene = "AACCGGTT", endGene = "AACCGGTA", bank = ["AACCGGTA"]
Output: 1


Example 2:

Input: startGene = "AACCGGTT", endGene = "AAACGGTA", bank = ["AACCGGTA","AACCGCTA","AAACGGTA"]
Output: 2
"""


class Solution:
    def minMutation(self, startGene: str, endGene: str, bank: [str]) -> int:
        # bfs
        gene_length = len(startGene)
        mutations = ["A", "C", "G", "T"]
        n_mutations = {startGene: 0}
        q = [startGene]

        while len(q) > 0:
            gene = q.pop(0)
            n_muts = n_mutations[gene]

            for i in range(gene_length):
                char = gene[i]
                possible_muts = [mut for mut in mutations if mut != char]

                for mut in possible_muts:
                    new_gene = gene[:i] + mut + gene[i + 1 :]

                    if new_gene in n_mutations.keys():  # we've seen it before
                        continue

                    if new_gene in bank:
                        if new_gene == endGene:
                            return n_muts + 1
                        else:
                            q.append(new_gene)
                            n_mutations[new_gene] = n_muts + 1

        return -1
