def evennumbers(start, end):
    return len(range((start if start%2==0 else start+1), end+1, 2))

def test_1_10_5():
    assert evennumbers(1, 10) == 5, "evennumbers(1, 10) should return 5"

def test_1_11_5():
    assert evennumbers(1, 11) == 5, "evennumbers(1, 11) should return 5"
    
def test_9_11_1():
    assert evennumbers(9, 11) == 1, "evennumbers(9, 11) should return 1"

def test_1_100_50():
    assert evennumbers(1, 100) == 50, "evennumbers(1, 100) should return 50"

def test_1_99_49():
    assert evennumbers(1, 99) == 49, "evennumbers(1, 99) should return 49"

def test_0_100_51():
    assert evennumbers(0, 100) == 51, "evennumbers(0, 100) should return 51"

def test_neg3_99_51():
    assert evennumbers(-3, 99) == 51, "evennumbers(-3, 99) should return 51"
