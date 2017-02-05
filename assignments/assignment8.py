import time

Subject_Filename = 'subjects.txt'
VALUE, WORK = 0, 1


def loadSubjects(filename):
    """
    Returns  dictionary mapping subject name to (value, work)
    """
    subjects_dict = {}
    inputFile = open(filename)

    for line in inputFile:
        name, value, work = line.split(',')

        subjects_dict[name.strip()] = (int(value), int(work))

    return subjects_dict


def printSubjects(subjects):
    """
    Prints a string containing name, value, and work of each subject in
    the dictionary of subjects and total value and work of all subjects
    """
    totalVal, totalWork = 0, 0
    if len(subjects) == 0:
        return 'Empty SubjectList'
    res = 'Course\tValue\tWork\n======\t====\t=====\n'
    subNames = subjects.keys()
    sorted(subNames)
    for s in subNames:
        val = subjects[s][VALUE]
        work = subjects[s][WORK]
        res = res + s + '\t' + str(val) + '\t' + str(work) + '\n'
        totalVal += val
        totalWork += work
    res = res + '\nTotal Value:\t' + str(totalVal) + '\n'
    res = res + 'Total Work:\t' + str(totalWork) + '\n'
    print(res)


def cmpValue(subInfo1, subInfo2):
    """
    Returns True if value in (value, work) tuple subInfo1 is GREATER than
    value in (value, work) tuple in subInfo2
    """
    val1 = subInfo1[VALUE]
    val2 = subInfo2[VALUE]
    return val1 > val2


def cmpWork(subInfo1, subInfo2):
    """
    Returns True if work in (value, work) tuple subInfo1 is LESS than than work
    in (value, work) tuple in subInfo2
    """
    work1 = subInfo1[WORK]
    work2 = subInfo2[WORK]
    return work1 < work2


def cmpRatio(subInfo1, subInfo2):
    """
    Returns True if value/work in (value, work) tuple subInfo1 is
    GREATER than value/work in (value, work) tuple in subInfo2
    """
    val1 = subInfo1[VALUE]
    val2 = subInfo2[VALUE]
    work1 = subInfo1[WORK]
    work2 = subInfo2[WORK]
    return float(val1) / work1 > float(val2) / work2


def greedyAdvisor(subjects, maxWork, comparator):
    """
    Returns a dictionary mapping subject name to (value, work) which includes
    subjects selected by the algorithm, such that the total work of subjects in
    the dictionary is not greater than maxWork.  The subjects are chosen using
    a greedy algorithm.  The subjects dictionary should not be mutated.
    """
    best_subjects = {}
    total_best_work = 0

    while total_best_work < maxWork:
        best_sub = None
        for sub in subjects.keys():
            if sub in best_subjects:
                continue

            if not best_sub:
                best_sub = sub

            if comparator(subjects.get(sub), subjects.get(best_sub)):
                if (total_best_work + subjects.get(sub)[WORK]) > maxWork:
                    continue
                best_sub = sub

        if (total_best_work + subjects.get(best_sub)[WORK]) > maxWork:
            return best_subjects

        best_subjects[best_sub] = subjects.get(best_sub)
        total_best_work += subjects.get(best_sub)[WORK]


def bruteForceAdvisor(subjects, maxWork):
    """
    Returns a dictionary mapping subject name to (value, work), which
    represents the globally optimal selection of subjects using a brute force
    algorithm.
    """
    nameList = list(subjects.keys())
    tupleList = list(subjects.values())
    bestSubset, bestSubsetValue = bruteForceAdvisorHelper(tupleList, maxWork,
                                                          0, None, None, [], 0, 0)
    outputSubjects = {}

    for i in bestSubset:
        outputSubjects[nameList[i]] = tupleList[i]

    return outputSubjects


def bruteForceAdvisorHelper(subject_values, maxWork, i, bestSubset, bestSubsetValue,
                            subset, subsetValue, subsetWork):
    # Hit the end of the list.
    if i >= len(subject_values):
        if bestSubset == None or subsetValue > bestSubsetValue:
            # Found a new best.
            return subset[:], subsetValue
        else:
            # Keep the current best.
            return bestSubset, bestSubsetValue
    else:
        s = subject_values[i]
        # Try including subject_values[i] in the current working subset.
        if subsetWork + s[WORK] <= maxWork:
            subset.append(i)
            bestSubset, bestSubsetValue = bruteForceAdvisorHelper(subject_values,
                    maxWork, i+1, bestSubset, bestSubsetValue, subset,
                    subsetValue + s[VALUE], subsetWork + s[WORK])
            subset.pop()
        bestSubset, bestSubsetValue = bruteForceAdvisorHelper(subject_values,
                maxWork, i+1, bestSubset, bestSubsetValue, subset,
                subsetValue, subsetWork)
        return bestSubset, bestSubsetValue


def bruteForceTime(subjects, maxWork):
    start = time.time()

    bruteForceAdvisor(subjects, maxWork)

    time_taken = time.time() - start

    print("Brute force took **", time_taken, "s** to finish.")
    # maxWork: 5    time: 0.9307436943054199s
    # maxWork: 10   time: 208.03178524971008s


def dpBruteForceAdvisorHelper(subject_values, maxWork, i, bestSubset,
                              bestSubsetValue, subset, subsetValue, subsetWork,
                              memo):
    key = ','.join([str(bestSubset), str(bestSubsetValue), str(subsetValue), str(subsetWork)])

    if memo.get(key):
        return memo.get(key)

    # Hit the end of the list.
    if i >= len(subject_values):
        if bestSubset == None or subsetValue > bestSubsetValue:
            # Found a new best.
            result = subset[:], subsetValue
            memo[key] = result

            return result
        else:
            # Keep the current best.
            result = bestSubset, bestSubsetValue
            memo[key] = result

            return result
    else:
        s = subject_values[i]
        # Try including subject_values[i] in the current working subset.
        if subsetWork + s[WORK] <= maxWork:
            subset.append(i)
            bestSubset, bestSubsetValue = dpBruteForceAdvisorHelper(subject_values,
                    maxWork, i+1, bestSubset, bestSubsetValue, subset,
                    subsetValue + s[VALUE], subsetWork + s[WORK], memo)
            subset.pop()
        bestSubset, bestSubsetValue = dpBruteForceAdvisorHelper(subject_values,
                maxWork, i+1, bestSubset, bestSubsetValue, subset,
                subsetValue, subsetWork, memo)

        result = bestSubset, bestSubsetValue
        memo[key] = result

        return result


def dpAdvisor(subjects, maxWork):
    nameList = list(subjects.keys())
    tupleList = list(subjects.values())
    memo = {}
    bestSubset, bestSubsetValue = dpBruteForceAdvisorHelper(tupleList, maxWork,
                                                            0, None, None, [],
                                                            0, 0, memo)
    outputSubjects = {}

    for i in bestSubset:
        outputSubjects[nameList[i]] = tupleList[i]

    return outputSubjects


def dpAdvisorTiming(subjects, maxWork):
    start = time.time()

    dpAdvisor(subjects, maxWork)

    time_taken = time.time() - start

    print("Time taken by dbAdvisor", time_taken, "s")
    # maxWork: 5    time: 0.2260580062866211
    # maxWork: 10   time: 0.9983208179473877


if __name__ == '__main__':
    subjects = loadSubjects(Subject_Filename)

    dpAdvisorTiming(subjects, 20)
