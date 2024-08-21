from flask import Flask
from controllers.message_controller import MessageController

app = Flask(__name__)

# Configura a rota principal
app.add_url_rule('/process_message', view_func=MessageController.as_view('process_message'))

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
