# reports/pdf_report.py
from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
from datetime import datetime
import os

def create_pdf_report(output_path, title, results_dict):
    """
    output_path : chemin fichier PDF final (ex: 'rapport.pdf')
    title : titre du rapport
    results_dict : dictionnaire clé->valeur à afficher (ex: {'Moment max (kN.m)': 12.3})
    """
    c = canvas.Canvas(output_path, pagesize=A4)
    width, height = A4
    margin = 50
    y = height - margin

    c.setFont("Helvetica-Bold", 16)
    c.drawString(margin, y, title)
    y -= 30

    c.setFont("Helvetica", 10)
    c.drawString(margin, y, f"Date : {datetime.now().strftime('%Y-%m-%d %H:%M')}")
    y -= 20

    for k, v in results_dict.items():
        line = f"{k}: {v}"
        c.drawString(margin, y, line)
        y -= 15
        if y < margin:
            c.showPage()
            y = height - margin

    c.showPage()
    c.save()
    return os.path.abspath(output_path)
