
import hw

def test_function_int():
    assert hw.function(5) == 10
    assert hw.function(0) == 0

def test_function_str():
    assert hw.function('a') == 'aa'
    assert hw.function('') == ''
