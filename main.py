# main.py
import sys
from structures.beam import moment_max_uniform, flexural_stress
from hydraulics.manning import manning_Q, rectangular_channel_A_P
from geotech.slope import fs_simple
from reports.pdf_report import create_pdf_report

def prompt_float(prompt_text):
    while True:
        try:
            return float(input(prompt_text + " "))
        except ValueError:
            print("Entrée invalide. Tapez un nombre (ex: 3.5).")

def run_beam():
    print("\n=== Calcul poutre (simple) ===")
    q = prompt_float("Charge répartie q (kN/m) ?")
    L = prompt_float("Portée L (m) ?")
    b = prompt_float("Largeur section b (m) ?")
    h = prompt_float("Hauteur section h (m) ?")
    M = moment_max_uniform(q, L)
    sigma = flexural_stress(M, b, h)
    print(f"Moment max M = {M:.3f} kN·m")
    print(f"Contrainte de flexion approximative = {sigma:.3f} MPa")
    return {"Module": "Poutre", "q (kN/m)": q, "L (m)": L, "M_max (kN·m)": round(M,3), "sigma (MPa)": round(sigma,3)}

def run_manning():
    print("\n=== Calcul Manning ===")
    b = prompt_float("Largeur du canal b (m) ?")
    h = prompt_float("Profondeur h (m) ?")
    n = prompt_float("Coefficient de rugosité n (ex 0.013) ?")
    S = prompt_float("Pente S (ex 0.001) ?")
    A, P = rectangular_channel_A_P(b, h)
    Q = manning_Q(n, A, P, S)
    print(f"Débit Q = {Q:.4f} m3/s")
    return {"Module": "Hydraulique", "b (m)": b, "h (m)": h, "n": n, "S": S, "Q (m3/s)": round(Q,6)}

def run_slope():
    print("\n=== Stabilité talus (très simplifié) ===")
    W = prompt_float("Poids de la tranche W (kN/m) ?")
    c = prompt_float("Cohésion c (kN/m2) ?")
    phi = prompt_float("Phi (deg) ?")
    alpha = prompt_float("Angle talus alpha (deg) ?")
    FS = fs_simple(W, c, phi, alpha)
    print(f"Facteur de sécurité approximatif FS = {FS:.3f}")
    return {"Module": "Géotechnique", "W (kN/m)": W, "c": c, "phi (deg)": phi, "alpha (deg)": alpha, "FS": round(FS,3)}

def main():
    print("=== Mini plateforme génie civil (débutant) ===")
    results = {}
    while True:
        print("\nChoisir un module :")
        print("1 - Poutre (structures)")
        print("2 - Manning (hydraulique)")
        print("3 - Talus (géotechnique)")
        print("4 - Générer PDF des derniers résultats")
        print("0 - Quitter")
        choice = input("Entrez votre choix : ").strip()
        if choice == "1":
            r = run_beam()
            results.update(r)
        elif choice == "2":
            r = run_manning()
            results.update(r)
        elif choice == "3":
            r = run_slope()
            results.update(r)
        elif choice == "4":
            out = create_pdf_report("rapport_resultats.pdf", "Rapport de calculs - Mini plateforme", results)
            print("PDF créé :", out)
        elif choice == "0":
            print("Au revoir !")
            sys.exit(0)
        else:
            print("Choix invalide.")

if __name__ == "__main__":
    main()
