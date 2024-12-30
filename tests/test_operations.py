from src.math_operations import add,sub


def test_add():
    assert add(2,3)==5
    assert add(-1,1)==0
    
def test_sub():
    assert sub(5,2)==3
    assert sub(17,5)==12
    assert sub(6,1)==5
    assert sub(3,9)==-6



