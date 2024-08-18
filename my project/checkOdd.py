import genColoring as gc
import genGraph as gg
# The check_odd_coloring function
def check_odd_coloring(p, c, n):
    """
    Check if a given coloring c is an odd coloring for permutation p.
    p: permutation of the vertices
    c: coloring vector
    n: number of vertices
    """
    for i in range(1, n + 1):
        count = 0
        for j in range(1, n + 1):
            if i != j and c[i-1] == c[j-1] and check_intersection(i, j, p, n):
                count += 1
        if count % 2 == 0:
            return False
    return True

# The check_intersection function is also needed for this to work correctly
def check_intersection(i, j, p, n):
    """
    Check if vertex i and vertex j intersect in permutation p.
    i and j intersect if either:
    1. At least one endpoint of j is in between i and i+n in p
    2. At least one endpoint of i is in-between j and j+n in p
    """
    Li = p.index(i) + 1
    Ri = p.index(i + n) + 1
    Lj = p.index(j) + 1
    Rj = p.index(j + n) + 1
    
    return max(Li, Lj) <= min(Ri, Rj)



# Sequence to test
# sequence = [1,2,3,4,12,5,9,10,6,7,11,8,16,13,15,14]
# n = 8  # Number of vertices
# coloring_vectors =gc.generate_coloring_vectors(n)
# # Use the generated coloring vectors to check for odd coloring
# valid_coloring_found = False
# for c in coloring_vectors:
#     if check_odd_coloring(sequence, c, n):
#         print(c)
#         valid_coloring_found = True
#         break

# print(valid_coloring_found)

n = 8  # Number of vertices
coloring_vectors = gc.generate_coloring_vectors(n)
all_sequences = gg.generate_all_sequences(n)
qualified_sequences = gg.connectivity_checker(all_sequences,n)
filtered_sequences = gg.remove_ordered_sequences(qualified_sequences,n)
# Iterate over each sequence in sequences
for sequence in filtered_sequences:
    valid_coloring_found = False
    for c in coloring_vectors:
        if check_odd_coloring(sequence, c, n):
            # print(f"Valid coloring for sequence {sequence}: {c}")
            valid_coloring_found = True
            break
    if not valid_coloring_found:
        print(f"No valid coloring found for sequence {sequence}")


