def closest_pair_to_k(tuples, k):
    if k >= len(tuples):
        return None

    target = sum(tuples[k])
    closest_pair = None
    min_distance = float('inf')

    for i, tup in enumerate(tuples):
        if i != k:
            distance = abs(target - sum(tup))
            if distance < min_distance:
                min_distance = distance
                closest_pair = tup

    return closest_pair

tuples = [(1, 2, 3), (4, 5, 6), (7, 8, 9)]  # hard coded for simplicity
k = 1
closest_pair = closest_pair_to_k(tuples, k)
print(closest_pair)