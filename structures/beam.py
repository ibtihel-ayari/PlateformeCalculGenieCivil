# structures/beam.py
"""
Module pour calculs simples de poutre (ex: poutre simplement appuyée sous charge répartie q).
Formules basiques :
- Moment max pour charge uniformément répartie q sur portée L : M_max = q * L^2 / 8
- Contrainte de flexion sigma = M*y/I  (ici on donne une estimation pour une section rectangulaire)
"""

import math

def moment_max_uniform(q, L):
    """
    q : charge répartie (kN/m) -> on utilisera N/m (convertir si utile)
    L : portée (m)
    Retour : moment max (kN·m)
    """
    return q * L**2 / 8.0

def section_rectangular_inertia(b, h):
    """
    b : largeur (m)
    h : hauteur (m)
    I : moment d'inertie pour section rectangulaire = b*h^3/12 (m^4)
    """
    return b * h**3 / 12.0

def flexural_stress(M_kNm, b, h, y=None):
    """
    Estime la contrainte de flexion (N/mm^2)
    M_kNm : moment en kN·m
    b, h : dimensions section (m)
    y : distance de la fibre neutre (m). si None, prend h/2.
    Retourne contrainte en MPa (N/mm^2)
    """
    if y is None:
        y = h / 2.0
    # convertir M en N·mm : kN·m -> N·mm = *1e6
    M_Nmm = M_kNm * 1e6
    I_m4 = section_rectangular_inertia(b, h)
    # I en mm^4 : 1 m^4 = 1e12 mm^4
    I_mm4 = I_m4 * 1e12
    y_mm = y * 1000.0
    sigma_MPa = M_Nmm * y_mm / I_mm4  # N/mm^2 = MPa
    return sigma_MPa
