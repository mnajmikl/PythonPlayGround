from oddeven import oddnumbers, evennumbers, oddevens

def test_1_10_5():
    o,e = oddevens(1, 10)
    assert oddnumbers(1, 10) == len(o), f"oddnumbers(1, 10) should return {len(o)}"
    assert evennumbers(1, 10) == len(e), f"evennumbers(1, 10) should return {len(e)}"

def test_1_11_6():
    o,e = oddevens(1, 11)
    assert oddnumbers(1, 11) == len(o), f"oddnumbers(1, 11) should return {len(o)}"
    assert evennumbers(1, 11) == len(e), f"evennumbers(1, 11) should return {len(e)}"
    
def test_9_11_2():
    o,e = oddevens(9, 11)
    assert oddnumbers(9, 11) == len(o), f"oddnumbers(9, 11) should return {len(o)}"
    assert evennumbers(9, 11) == len(e), f"evennumbers(9, 11) should return {len(e)}"

def test_1_100_50():
    o,e = oddevens(1, 100)
    assert oddnumbers(1, 100) == len(o), f"oddnumbers(1, 100) should return {len(o)}"
    assert evennumbers(1, 100) == len(e), f"evennumbers(1, 100) should return {len(e)}"

def test_1_99_50():
    o,e = oddevens(1, 99)
    assert oddnumbers(1, 99) == len(o), f"oddnumbers(1, 99) should return {len(o)}"
    assert evennumbers(1, 99) == len(e), f"evennumbers(1, 99) should return {len(e)}"

def test_0_100_50():
    o,e = oddevens(0, 100)
    assert oddnumbers(0, 100) == len(o), f"oddnumbers(0, 100) should return {len(o)}"
    assert evennumbers(0, 100) == len(e), f"evennumbers(0, 100) should return {len(e)}"

def test_neg3_99_52():
    o,e = oddevens(-3, 99)
    assert oddnumbers(-3, 99) == len(o), f"oddnumbers(-3, 99) should return {len(o)}"
    assert evennumbers(-3, 99) == len(e), f"evennumbers(-3, 99) should return {len(e)}"
