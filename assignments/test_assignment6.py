from assignment6 import get_combination


def test_get_combination():
    assert get_combination('omtsern', 'monster') is True
    assert get_combination('yello', 'hello') is False
    assert get_combination('cepeyr', 'creepy') is True
    assert get_combination('pien', 'pain') is False
    assert get_combination('mdr', 'maninder') is False
    assert get_combination('adr', 'manindr') is False
    assert get_combination('hello', 'hell') is True
    assert get_combination('rtsmoen', 'monster') is True
    assert get_combination('pyrec', 'creepy') is False
    assert get_combination('smufhpeuhrain', 'superman') is True
    assert get_combination('acihmmz', 'him') is True
    assert get_combination('acihmmz', 'cam') is True
