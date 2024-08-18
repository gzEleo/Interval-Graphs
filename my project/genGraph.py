def insert_number_sequences(existing_sequences, num_to_insert, position_to_maintain):
    new_sequences = []

    for seq in existing_sequences:
        for i in range(len(seq) + 1):
            if seq.index(position_to_maintain) < i:
                new_seq = seq[:i] + [num_to_insert] + seq[i:]
                new_sequences.append(new_seq)
    
    return new_sequences

def generate_all_sequences(n):

    sequences = [[i for i in range(1, n + 1)]]
    

    for i in range(1, n + 1):
        sequences = insert_number_sequences(sequences, n + i, i)
    
    return sequences

def connectivity_checker(sequences, n):
    qualified_sequences = []

    for sequence in sequences:
        counter = 0
        for i, num in enumerate(sequence):
            if num >= 1 and num <= n:
                counter += 1
            elif num > n and num <= 2 * n:
                counter -= 1

            if counter == 0 and i < len(sequence) - 1:
                # print(f"Sequence {sequence} disqualified: counter=0 at index {i+1}")
                break
        else:
            qualified_sequences.append(sequence)

    return qualified_sequences

def remove_ordered_sequences(sequences, n):
   
    target_sequence = list(range(1, n + 1))
     
    filtered_sequences = []
    
    for sequence in sequences:
        
        if sequence[:n] != target_sequence:
            filtered_sequences.append(sequence)
        # else:
        #     print(f"Sequence {sequence} removed: first {n} elements are ordered as {target_sequence}")
    
    return filtered_sequences

# n = 8

# all_sequences = generate_all_sequences(n)
# qualified_sequences = connectivity_checker(all_sequences,n)
# filtered_sequences = remove_ordered_sequences(qualified_sequences,n)

# print(len(all_sequences))
# print(len(qualified_sequences))
# print(len(filtered_sequences))
# output_path = 'remove_ordered_sequences_output.txt'
# with open(output_path, 'w') as file:
#     for perm in filtered_sequences:
#         file.write(','.join(map(str, perm)) + '\n')
# print(f"total results: {len(filtered_sequences)}")