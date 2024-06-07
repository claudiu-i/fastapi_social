from app.calculations import add

def test_add():
    print("testing add function")
    sum = add(5,3)
    assert 8 == sum
    