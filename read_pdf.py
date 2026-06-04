import fitz
import sys
sys.stdout.reconfigure(encoding='utf-8')
doc = fitz.open(r'c:\Users\hanae\Desktop\projet ia\Cahier_des_Charges_Projet_IA.pdf')
for page in doc:
    print(page.get_text())
