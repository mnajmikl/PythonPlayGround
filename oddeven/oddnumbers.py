def oddnumbers(start, end):
    return len(range((start if start%2==1 else start+1), end+1, 2))

def test_1_10_5():
    assert oddnumbers(1, 10) == 5, "oddnumbers(1, 10) should return 5"

def test_1_11_6():
    assert oddnumbers(1, 11) == 6, "oddnumbers(1, 11) should return 6"
    
def test_9_11_2():
    assert oddnumbers(9, 11) == 2, "oddnumbers(9, 11) should return 2"

def test_1_100_50():
    assert oddnumbers(1, 100) == 50, "oddnumbers(1, 100) should return 50"

def test_1_99_50():
    assert oddnumbers(1, 99) == 50, "oddnumbers(1, 99) should return 50"

def test_0_100_50():
    assert oddnumbers(0, 100) == 50, "oddnumbers(0, 100) should return 50"

def test_neg3_99_52():
    assert oddnumbers(-3, 99) == 52, "oddnumbers(-3, 99) should return 52"
