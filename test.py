from WiFiman import WiFiman
wfm = WiFiman()

def test_launch():
    assert wfm

def test_Wifiman_check():
    assert wfm.getSpeedPerMinute()
