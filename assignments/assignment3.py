def countSubStringMatch(target, key):
    """
    Returns how many occurrences of `key` are there in `target`
    """
    count = 0
    index = 0

    while True:
        index = target.find(key, index)

        if index == -1:
            return count

        index += len(key)
        count += 1


def countSubStringMatchRecursive(target, key):
    """
    Returns how many occurrences of `key` are there in `target`
    """
    index = target.find(key)

    if index == -1:
        return 0

    return 1 + countSubStringMatchRecursive(target[index + len(key):], key)


def subStringMatchExact(target, key):
    """
    Returns a tuple of the indices of `key` that occurs in  `target`
    """
    indices = ()
    index = 0

    for i in target:
        index = target.find(key, index)

        if index == -1:
            return indices

        indices += (index,)

        if len(key) == 0:
            index += 1
        else:
            index += len(key)

    return indices


def constrainedMatchPair(firstMatch, secondMatch, length):
    """
    Returns a tuple of indices from `firstMatch` if `firstMatch`+ `length` + 1
    is equals to `secondMatch` is True
    """
    result = ()

    for i in firstMatch:
        if (i + length + 1) in secondMatch:
            result += (i,)

    return result


def getAllCombinations(s):
    """
    Returns all possible combinations with one substitution in `string`
    e.g "abcd"  ->  (("", "bcd"), ("ab", "d"), ("abcd"), ("a", "cd"))
    """
    combnations = []

    for i in range(len(s)):
        combnations.append((s[:i], s[i+1:]))

    return combnations


def subStringMatchExactlyOneSub(target, key):
    """
    Returns a tuple of indices of `key` in `target` for which exactly one
    substitution is required
    """
    all_key_combinations = getAllCombinations(key)
    results = ()

    for pair in all_key_combinations:
        firstMatch = subStringMatchExact(target, pair[0])
        secondMatch = subStringMatchExact(target, pair[1])
        length = len(pair[0])

        all_matches = constrainedMatchPair(firstMatch, secondMatch, length)

        for m in all_matches:
            if m not in subStringMatchExact(target, key):
                results += (m,)

    return results
