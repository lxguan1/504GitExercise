def count_nucleotides(dna_sequence):
    """Count the occurrences of each nucleotide in a DNA sequence.
    
    Parameters:
        dna_sequence: A string containing DNA nucleotides
    Returns:
        dict: A dictionary with nucleotides as keys and their counts as values
    """
    nucleotide_counts = dict()
    
    # Count each nucleotide in the DNA sequence
    for nucleotide in dna_sequence:
        if nucleotide not in nucleotide_counts:
            nucleotide_counts[nucleotide] = 1
        else:
            nucleotide_counts[nucleotide] += 1
            
    return nucleotide_counts

def display_nucleotide_freqs(nucleotide_counts):
    """Display the frequency of each nucleotide as a proportion of the total.
    
    Parameters:
        nucleotide_counts: Dictionary with nucleotides and their counts
    """
    
    # Calculate the total number of nucleotides
    total_nucleotides = float(sum(nucleotide_counts.values()))
    
    # Calculate and display the frequency of each nucleotide
    print('Nucleotide Frequencies:')
    for nucleotide in nucleotide_counts:
        frequency = nucleotide_counts[nucleotide] / total_nucleotides
        print(f'{nucleotide}: {frequency}')

dna_sequence = 'ATCTGACGCGCGCCGC'
nucleotide_counts = count_nucleotides(dna_sequence)
display_nucleotide_freqs(nucleotide_counts)
