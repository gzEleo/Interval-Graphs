import itertools

def generate_coloring_vectors(n):
    """
    Generate all valid color assignment vectors for n vertices,
    considering only three colors: 0, 1, and 2.
    The first position is always 0 and the second number appearing is always 1.
    """
    vectors = []
    for vector in itertools.product([0, 1, 2], repeat=n):
        if vector[0] == 0 and vector.count(1) > 0:
            # Ensure the second appearing number is 1
            second_num = next((x for x in vector if x != 0), None)
            if second_num == 1 and all(vector.count(x) % 2 == 0 for x in [0, 1, 2] if vector.count(x) > 0):
                vectors.append(vector)
    return vectors

# Example usage
# n = 8
# coloring_vectors = generate_coloring_vectors(n)
# total_vectors = len(coloring_vectors)
# print(f"Total valid coloring vectors for {n} vertices: {total_vectors}")
# output_path = 'coloring.txt'
# with open(output_path, 'w') as file:
#     for perm in coloring_vectors:
#         file.write(','.join(map(str, perm)) + '\n')