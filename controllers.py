from flask import request, jsonify
from services import PDFService
from models import TextoExtraido

class PDFController:
    @staticmethod
    def extrair():
        if 'file' not in request.files:
            return jsonify({"message": "Nenhum arquivo enviado"}), 400

        file = request.files['file']

        try:
            #chama o serviço
            resultado_texto = PDFService.processar_pdf(file.read())

            if not resultado_texto:
                return jsonify({"message": "PDF sem texto"}), 400

            #Cria o modelo e retorna
            resposta = TextoExtraido(resultado_texto)
            return jsonify(resposta.to_dict()), 200

        except Exception as e:
            return jsonify({"message": f"Erro interno: {str(e)}"}), 500




