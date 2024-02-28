from project import valid_email,check_ans,login_valid,valid_pw



def test_valid_pw():
    assert valid_pw("123456","123456") == None
    assert valid_pw("123","123") == "Password must have six characters at least"
    assert valid_pw("111111","123456") == "Passwords didn't match"

def test_login_valid():
    assert login_valid("winnie","123456") == 1
    assert login_valid("logan","111111") == 1
    assert login_valid("winnie","111111") == 2
    assert login_valid("david","121212") == 2

def test_valid_email():
    assert valid_email("winnie@gmail.com") ==None
    assert valid_email("winnie@@gmail.com") =="Invalid email"

def test_check_ans():
    assert check_ans(["3","3","1","2","1"])== 5
    assert check_ans(["3","2","2","2","1"])== 3
    assert check_ans(["1","2","3","4","1"])== 1
    assert check_ans(["2","1","2","2","3"])== 1
    assert check_ans(["2","2","3","1","3"])== 0