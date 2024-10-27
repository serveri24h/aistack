from flask import Flask, redirect, request, jsonify
from rags.rag1.query_data import query_rag
from flask_cors import CORS
import json

app = Flask(__name__)
CORS(app, resources={r"/models/*": {"origins": "http://localhost:6969"}}) 

@app.route('/models/<model_name>', methods=['POST'])
def redirect_model(model_name:str):

    data = json.loads(request.data.decode("utf-8"))

    # Route based on the model_name
    match model_name:
        case 'raggy':
            answer = query_rag(data["prompt"])
            return jsonify({'answer': answer}), 200
        case _other:
            return jsonify({'answer':"NO SUCH MODELS"}), 200

if __name__ == '__main__':
    print("\nAI SERVER IS STARTING............\n")
    # Run the Flask app on port 5000
    app.run(host="0.0.0.0", port=5000, debug=True)