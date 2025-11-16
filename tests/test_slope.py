from geotech.slope import fs_simple

def test_fs_simple_basic():
    W = 20     # kN/m
    c = 5      # kN/m2
    phi = 30   # deg
    alpha = 20 # deg
    fs = fs_simple(W, c, phi, alpha)
    assert fs > 0

def test_fs_simple_zero_denominator():
    W = 20
    c = 5
    phi = 30
    alpha = 0  # → doit lever erreur
    import pytest
    with pytest.raises(ValueError):
        fs_simple(W, c, phi, alpha)
