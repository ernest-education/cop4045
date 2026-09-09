def find_pythagorean(n):
    triples = []

    #dark and evil brute force method
    for a in range(1, n+1):
        for b in range(1, n+1):
            for c in range(1, n+1):

                if (((a**2) + (b**2)) == (c**2)):
                    triples.append((a, b, c))
    return triples

n = int(input("enter a value to check up to: "))

triples = find_pythagorean(n)

for triple in triples:
    print(triple)
