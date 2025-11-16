# hydraulics/manning.py
"""
Calculs basiques avec Manning :
Q = (1/n) * A * R^(2/3) * S^(1/2)
où A = aire mouillée (m2), R = rayon hydraulique = A / P (m), P = mouillage (périmètre mouillé), S = pente.
"""

import math

def manning_Q(n, A, P, S):
    """
    n : coefficient de rugosité (ex 0.013 pour béton)
    A : aire mouillée (m2)
    P : périmètre mouillé (m)
    S : pente (sans unité, ex 0.001)
    Retourne Q en m3/s
    """
    if P <= 0:
        raise ValueError("Périmètre mouillé P doit être > 0")
    R = A / P
    Q = (1.0 / n) * A * (R ** (2.0/3.0)) * (S ** 0.5)
    return Q

def rectangular_channel_A_P(b, h):
    """
    canal rectangulaire :
    b : largeur (m)
    h : profondeur d'écoulement (m)
    retourne (A, P)
    """
    A = b * h
    P = b + 2 * h
    return A, P
