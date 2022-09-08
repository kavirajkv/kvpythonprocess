import mypy
import pytest

@pytest.mark.skip(reason='I want to skip this particularly')
def test_ad():
    mysum=mypy.ad(2,3)
    assert mysum==5
    
def test_mul():
    mymul=mypy.mul(2,3)
    assert mymul==6