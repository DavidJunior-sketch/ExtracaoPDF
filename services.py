from pypdf import PdfReader
import io
import re

class PDFService:
    @staticmethod
    def processar_pdf(file_bytes):
        stream = io.BytesIO(file_bytes)
        reader = PdfReader(stream)

        texto_bruto = ""
        for page in reader.pages:
            extraido = page.extract_text()
            if extraido:
                texto_bruto += extraido

        if texto_bruto:
           texto_limpo = texto_bruto.lower()
           texto_limpo = re.sub(r'\s+', ' ', texto_limpo)
           tempo_limpo = texto_limpo.strip()

           return texto_limpo

        return "Não foi possivel extrair texto deste PDF"