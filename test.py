from WiFiman import WiFiman

wfm = WiFiman()


def test_launch():
    assert wfm


def test_Wifiman_check():
    assert wfm.getSpeed()
    # while true:
    #   wfm.driver.implicitly_wait(60)
    #   assert wfm.getSpeed()
    ## This loop should go until the process is terminated to continuously gauge network speed
