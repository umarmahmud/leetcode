def longest_common_prefix(arr):
    lengths = [len(i) for i in arr]
    min_length = min(lengths)
    new_arr = [i[:min_length] for i in arr]

    results_string = ''

    for n in range(min_length):
        s = set()
        for i in range(len(new_arr)):
            for j in range(n, n + 1):
                s.add(new_arr[i][j])
        if len(s) == 1:
            results_string += new_arr[i][j]
        else:
            break

    return results_string
