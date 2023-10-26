import pytest

from codexample.functions import return_value, raise_error

def test_return_value():
    value = 5
    assert return_value(value) == 5

def test_zero_division():
    with pytest.raises(ZeroDivisionError):
        result = 1 / 0


def test_recursion_depth():
    with pytest.raises(RuntimeError) as excinfo:

        def f():
            f()

        f()
    assert "maximum recursion" in str(excinfo.value)


def test_match():
    msg_kw = "123"
    with pytest.raises(ValueError, match=r".* %s .*" % msg_kw):
        raise_error(msg_kw)
