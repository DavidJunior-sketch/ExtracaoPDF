from pypdf import PdfReader
import re

caminho = r"C:\Users\lenovo\Downloads\lorem-ipsum.pdf"
#verificador de texto
def Obter_texto_validado(caminho):
    reader = PdfReader(caminho)
    texto_acumulado = ""

    for page in reader.pages:
        extraido = page.extract_text()
        if extraido:
            texto_acumulado += extraido
    return texto_acumulado if texto_acumulado.strip() else None

def normalizar_texto(texto_bruto):
    #Passa para minusculas e limpa espacos extras
    texto = texto_bruto.lower()
    texto = re.sub(r'\s+',' ',texto)
    return texto.strip()

def fragmentar_por_limite(texto , limite=1000):
    fragmentos = [texto[i:i+limite] for i in range(0 ,len(texto),limite)]
    return fragmentos

texto_bruto = Obter_texto_validado(caminho)

if texto_bruto:
    print("O PDF possui texto extraivel")
    texto_final = normalizar_texto(texto_bruto)
    blocos = [texto_final[i:i+1000] for i in range (0, len(texto_final),1000)]

    print(f"___ inciando apresentacao de {len(blocos)} Fragemntos ---\n")

    for indice, trecho in enumerate(blocos ,1):
         print(f"### Exibindo Fragmento {indice} ###")
         print(trecho)
         print("_"* 50)

else:
    print("arquivo PDF não possui texto extraivel")








