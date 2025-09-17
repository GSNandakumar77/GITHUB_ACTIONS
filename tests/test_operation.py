from src.math_operator import add,sub


def test_add():
    assert add(2,3)==5
    assert add(8,-8)==0

def test_sub():
    assert sub(10,5)==5
    assert sub(4,3)==1
    assert sub(10,8)==2