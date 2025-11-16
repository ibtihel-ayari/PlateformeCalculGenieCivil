# geotech/slope.py
"""
Calcul très simplifié d'un facteur de sécurité FS (approximatif) pour talus.
Formule simplifiée utilisée ici (très approximative) :
FS = (c + (W * cos(alpha) * tan(phi))) / (W * sin(alpha))
où W est le poids de la tranche de sol (per unité de longueur), alpha angle talus.
Ceci n'est PAS un substitut à une vraie étude géotechnique.
"""

import math

def fs_simple(W, c, phi_deg, alpha_deg):
    """
    W : poids de la tranche par mètre de longueur (kN/m)
    c : cohésion (kN/m2)
    phi_deg : angle de frottement interne (degrés)
    alpha_deg : angle de la surface du talus par rapport à l'horizontal (degrés)
    Retourne facteur de sécurité (adimensionnel)
    """
    phi = math.radians(phi_deg)
    alpha = math.radians(alpha_deg)
    numerator = c + (W * math.cos(alpha) * math.tan(phi))
    denominator = W * math.sin(alpha)
    if denominator == 0:
        raise ValueError("Denominator zero: alpha cannot be 0 or 180 deg in this formula")
    FS = numerator / denominator
    return FS
