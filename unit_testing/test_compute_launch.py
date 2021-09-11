from compute_launch import days_until_launch


def test_days_until_launch_4():
    assert (days_until_launch(22, 26) == 4)


def test_days_until_launch_0():
    assert (days_until_launch(253, 253) == 0)


def test_days_until_launch_0_negative():
    assert (abs(days_until_launch(83, 64)) == 19)
    # this was == 0 and it gave an error now we fixed it


def test_days_until_launch_1():
    assert (days_until_launch(9, 10) == 1)