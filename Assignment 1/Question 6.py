# Prompt: Counting DNA Nucleotides
# A string is simply an ordered collection of symbols selected from some alphabet and formed into a word; the length of a string is the number of symbols that it contains.
# An example of a length 21 DNA string (whose alphabet contains the symbols 'A', 'C', 'G', and 'T') is "ATGCTTCAGAAAGGTCTTACG."
# Given: A DNA string s of length at most 1000 nt.
# Return: Four integers (separated by spaces) counting the respective number of times that the symbols 'A', 'C', 'G', and 'T' occur in s.

def main():
	s = "ACGAGACCCTCCAGGACTCTCATATGCACTACGATAGGTCCGCTCCAGGTGTTCAAATCTTCGTTACGAATCGCTAAGTGCCGGCGGCTACATCCTCCGGGCTCTCCAACAACCTCTAGGCTGCTTGGGGCACGTCACCAAAGGAGCCAGTGTGGAGAGCGGCGACCTGCTTATTGACTATAGGACCATTCTCCTAACTGGGCCTGGCTAGGACCGCCACAGTTTGGTATATCGCATGTGCGTTCTAACACCGATAACGTATATACTCGTAAAACCGGTTTGGCGTGTACCAACCCACTTTTTGCCACTATTGGTTCCTTCGCATCGCAGAACCGCGCCGAGCGCTAGTTTTCCGCAGACAACACTGGACAAGCTGTCAGTCTGAACGTCCTCTCAGCGCAAAGGCTCATGCGGTCACGTATGCGACCTACACTAATATCCCCTCTAAGATCGCCAGGCGGAGAACTCCAATCTAGTTTTAGGTCAACATGCAGTACTCGGGTTTTTTCCAACGGGAGGTGGAGAAAACTAACTTTGCATACAGCGCATATAGTCCCGAGGCTGTATGACGAACTATCGCACGTTGAGTTCTACGCTCTTCCTTACGACTGGACTAGAACCGACGTTCCCCCCACAGCATTGCTCCTGAGTCGAGCCTTCACCAAAGTAGTGTACAGGATCAAGTCGCGGGACAGTCCGTTGCCTAACCTTTAAGCTAGATGTCCCGTATTTGGCAGTTGCGTCCTTGGCGATATTTCCGATCCAACTGATTTTAGCCCAATTTGTGGGACTAAACTCTGTCCGGGGGGAGTCTTTCCGTATTTTAGATAGGTGGTAACCAAGCCAAATCCGACCAGAGCCCACTTCATGCGTTTTCCAGTACGACACACTCGCCTGAC"
	d = {'A':0, 'C':0, 'G':0, 'T':0}   # initialize a dictionary of ACGT
	for x in range (0, len(s)):
		d[s[x]] = d[s[x]] + 1
	output = ""
	for key, value in d.items():
		output = output + str(value) + " "
	print (output)

if __name__ == "__main__":
  main()