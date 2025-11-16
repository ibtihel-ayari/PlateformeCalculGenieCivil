from structures.beam import moment_max_uniform, flexural_stress

def test_moment_max_uniform():
    # q = 5 kN/m, L = 4 m => M = q*L^2/8 = 5*16/8 = 10 kN·m
    assert moment_max_uniform(5, 4) == 10

def test_flexural_stress():
    # test simple pour vérifier que ça tourne et renvoie une valeur positive
    M = 20  # kN·m
    b = 0.3
    h = 0.5
    sigma = flexural_stress(M, b, h)
    assert sigma > 0
