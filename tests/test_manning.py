from hydraulics.manning import manning_Q, rectangular_channel_A_P

def test_rectangular_channel():
    A, P = rectangular_channel_A_P(2, 1)
    assert A == 2
    assert P == 2 + 2*1  # = 4

def test_manning_Q():
    b = 2
    h = 1
    n = 0.013
    S = 0.001
    A, P = rectangular_channel_A_P(b, h)
    Q = manning_Q(n, A, P, S)
    assert Q > 0
