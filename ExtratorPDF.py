from pypdf import  PdfReader
from flask import Flask , request , jsonify
import io
import re

app = Flask(__name__)

ALLOWED_EXTENSIONS = {'pdf'}

#verifica se o arquivo é pdf
def allowed_file(filename):
    return'.' in filename and\
           filename.rsplit('.',1)[1].lower() in ALLOWED_EXTENSIONS

#verificador de texto
def Obter_texto_validado(file_stream):
    # le o fluxo de dados que ve, da internet
    reader = PdfReader(file_stream)
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

 # A ROTA DA API

@app.route('/extraction', methods=['POST'])
def extractions():
    #Verifica se o arquivo foi enviado
    if 'file' not in request.files:
        return jsonify({"message": "Nenhum arquivo enviado"}),400

    file = request.files['file']

    if not allowed_file(file.filename):
        return jsonify({"message": "Formato invelido! Envie apenas arquivos .pdf"}), 415
    try:
        #Extrai o taxto usando na funcao
        texto_bruto = Obter_texto_validado(io.BytesIO(file.read()))

        if not texto_bruto :
           return jsonify({"message": "Arquivo PDF nao possui texto extraivel"}), 400

        texto_final = normalizar_texto(texto_bruto)

       #retorna o texto inteiro
        return jsonify({
        "message": texto_final
         }), 200

    except Exception as e:
          return jsonify({"message": f"Erro ao processar: {str(e)}"}), 500

if __name__ == '__main__':
    app.run(debug=True)








