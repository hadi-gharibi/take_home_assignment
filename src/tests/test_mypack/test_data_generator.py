from mypack.data_generator import *
import datetime
from random import randint
 
def test_user_gen_company_size():
    com_size = []
    for i in range(1000):
        s = User(1).company_size
        com_size.append(s)
        assert isinstance(s, str)

    
    assert com_size.count('small') > 650
    assert com_size.count('small') < 850

def test_user_gen_rand_session_number(user_class):
    if user_class.company_size == 'small': max_bound = 10
    else: 
        max_bound = 20
    
    for i in range(100):
        s = user_class.gen_rand_session_number()
        
        assert isinstance(i, int)
        assert 0 <= s 
        assert s <= max_bound

def test_gen_rand_timestamp(user_class):
    for i in range(1,13):
        for j in range(100):
            t = user_class.gen_rand_timestamp(i)

            assert isinstance(t, datetime.datetime)
            assert t.month == i

def test_user_gen_rand_sessions(user_class):
    for i in range(100):
        s = user_class.gen_rand_sessions(randint(1,12))
        
        assert isinstance(s, list)
        if s:
            assert isinstance(s[0], datetime.datetime)
            assert isinstance(s[-1], datetime.datetime)
    