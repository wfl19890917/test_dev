import pytest
def test_success():
    assert True
def test_failure():
    assert False
def test_skip():
    pytest.skip('for a repwason')
def test_broken():
    raise Exception("ols"
                    "ps")