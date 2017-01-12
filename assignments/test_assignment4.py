from assignment4 import nestEggFixed, nestEggVariable, postRetirement


def test_nestEggFixed():
    assert nestEggFixed(10000, 10, 15, 5) == [1000.0,
                                              2150.0, 3472.5,
                                              4993.375,
                                              6742.3812499999995]


def test_nestEggVariable():
    assert nestEggVariable(10000, 10, [3, 4, 5, 0, 3]) == [1000.0, 2040.0,
                                                           3142.0, 4142.0,
                                                           5266.2600000000002]


def test_postRetirement():
    assert postRetirement(100000,
                          [10, 5, 0, 5, 1],
                          30000) == [80000.000000000015,
                                     54000.000000000015,
                                     24000.000000000015,
                                     -4799.999999999985,
                                     -34847.999999999985]
