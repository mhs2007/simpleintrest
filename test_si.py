from si import simple_interest

def test_si_1():
    assert simple_interest(10000,5,2)==1000
    
def test_si_2():
    assert simple_interest(20000,10,2)==4000
    
def test_si_3():
    assert simple_interest(100000,5,3)==15000