from assignment8 import (cmpValue,
                         cmpRatio,
                         cmpWork,
                         greedyAdvisor)


def test_greedyAdvisor():
    sub_dict = {'6.00': (16, 8), '1.00': (7, 7), '6.01': (5, 3),
                '15.01': (9, 6)}

    assert greedyAdvisor(sub_dict, 10, cmpValue) == {'6.00': (16, 8)}
    assert greedyAdvisor(sub_dict, 15, cmpValue) == {'6.00': (16, 8),
                                                     '15.01': (9, 6)}
    assert greedyAdvisor(sub_dict, 20, cmpWork) == {'6.01': (5, 3),
                                                    '15.01': (9, 6),
                                                    '1.00': (7, 7)}
    assert greedyAdvisor(sub_dict, 5, cmpWork) == {'6.01': (5, 3)}
    assert greedyAdvisor(sub_dict, 15, cmpRatio) == {'6.00': (16, 8),
                                                     '6.01': (5, 3)}
