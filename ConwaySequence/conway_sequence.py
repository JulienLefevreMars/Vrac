# Conway's sequence
import sys

def successor(list):
	# Find the successor of a sequence of integer by counting each occurence, taking into account ordering
	# Example: sucessor(1121)=211211	
	new_list = []
	n = len(list)
	i = 0
	while i<n:
		j = 0 # nbr_consecutive_occurence
		while (list[i+j] == list[i]):
			j = j+1
			if (i+j>=n):
				break
		new_list.append(j)
		new_list.append(list[i])
		i = i+j
	return new_list


def compute_all_terms(N,list=[1]):
	all_terms = [list]
	for i in range(N):
		all_terms.append(successor(all_terms[-1]))
	return all_terms


def print_one_term(list):
	n = len(list)
	for i in range(n):
		print(list[i],end="")
	print()	
	
	
def print_all_terms(all_terms):
	N = len(all_terms)
	for i in range(N):
		#print(all_terms[i])
		print_one_term(all_terms[i])


if __name__ == "__main__":
	N = int(sys.argv[1])
	all_terms = compute_all_terms(N)
	print_all_terms(all_terms)

	

