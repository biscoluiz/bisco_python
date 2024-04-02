import re
import pandas as pd
from PIL import Image
import pytesseract

pytesseract.pytesseract.tesseract_cmd = r'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'

# Imagem
image_path = 'irocr.png'  # Substitua pelo seu caminho de imagem
image = Image.open(image_path)

# OCR
text = pytesseract.image_to_string(image, lang='por')  # 'por' para português
#print(text) 

# Gambiarra
patterns = {
    "Total dos Rendimentos (Inclusive Férias)": r"01\.\s*Tote!\s*dos\s*Rendimentos\s*\(Inclusive\s*Férias\)\s*([\d.]+)",
    "Contribuição Previdenciária Oficial": r"\|o2\.\s*Contribuição\s*Previdenciária\s*Oficia!\s*([\d.,]+)",
    "Contribuição a entidades de previdência": r"o2\.\s*Contrib\.\s*s\s*entidade\s*de\s*previdencia\s*complementar\s*publ\.\s*priv\.fundos\s*spos\s*([\d.,]+)",
    "Pensão Alimentícia": r"\|04\.\s*Pensão\s*Alimentícia\s*\(Informar\s*o\s*Beneficiário\s*no\s*Quadro\s*07\)\s*([\d.,]+)",
    "Imposto de Renda Retido": r"\|05\.\s*Imposto\s*de\s*Renda\s*Retido\s*([\d.,]+)",
}

results = {}


for key, pattern in patterns.items():
    match = re.search(pattern, text)
    if match:
        value = match.group(1).replace('.', '').replace(',', '.')
        try:
            results[key] = float(value)
        except ValueError:
            results[key] = value


df = pd.DataFrame([results])
pd.options.display.float_format = '{:,.2f}'.format

df.columns = ['Total Rendimentos (Incl. Férias)', 'Contrib. Previdenciária Oficial', 'Contrib. Entidades Previdência', 'Pensão Alimentícia', 'Imposto de Renda Retido']

print(df)
