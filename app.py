from flask import Flask
from controllers import PDFController

app = Flask(__name__)

#redireciona as requisições do Flask ao controller
app.add_url_rule('/extractions', view_func=PDFController.extrair, methods=['POST'])


if __name__ == '__main__':
    app.run(debug=True)








