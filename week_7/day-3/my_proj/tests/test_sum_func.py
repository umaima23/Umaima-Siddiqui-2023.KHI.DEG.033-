from my_proj.sum_func import add, add_positive

def test_add_1_2_returns_3():
    assert add(1, 2) == 3
    
def test_add_positive():
    assert add_positive(2, 3) == 5

def test_add_a_negative_b_positive():
    assert add_positive(-2, 3) == None
    
def test_add_b_zero():
    assert add_positive(2, 0) == None
        
def test_add_a_zero_b_zero():
    assert add_positive(0, 0) == None
    

