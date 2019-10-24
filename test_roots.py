#! /usr/ bin/python3

def test_quadroots_result():
    """
    This function tests the correctness of produced results with an example
    """

    assert roots.quad_roots(1.0, 1.0, -12.0) == ((3+0j), (-4+0j))

def test_quadroots_types():
    """
    This function tests that our roots.py raises and error when strings are passed
    """
    with pytest.raises(TypeError):
        roots.quad_roots("", "green", "hi")

def test_quadroots_zerocoeff():
    
    """ 
    This function tests for proper handling of zero coefficents
    """

    with pytest.raises(ValueError):
        roots.quad_roots(a=0.0)
