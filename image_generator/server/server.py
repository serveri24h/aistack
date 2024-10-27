from flask import Flask, render_template, request, jsonify
from PIL import Image
import secrets
import json
from flask_cors import CORS, cross_origin
from pipelines.create_imgs import run_stable_diffusion
import torch

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "http://localhost:6969"}}) 

# generate random secret key
app.config['SECRET_KEY'] = secrets.token_hex(16)

@app.route('/')
def hello():
    # home page
    
    return render_template(
        "index.html", 
        # pass variables into the HTML template
        btn_range = range(3), 
        prompt_images = ["/static/images/placeholder_image.png" for i in range(3)]
    )

@app.route('/prompt', methods=['POST', 'GET'])
def prompt():
    # generate images from user prompt
    data = json.loads(request.data.decode("utf-8"))
    print("HER22", data)
    run_stable_diffusion(prompt=data["prompt"])
    return jsonify({'answer':"NO SUCH MODELS"}), 200


@app.route('/supersample', methods=['POST', 'GET'])
def supersample():
    # enlarge and save prompt image in high quality
    print("save button", request.form['save_btn'], "was clicked!")

    return render_template(
        "index.html", 
        # pass variables into the HTML template
        btn_range = range(3), 
        prompt_images = ["/static/images/placeholder_image.png" for i in range(3)]
    )

if __name__ == '__main__':
    print("CUDA IS", torch.cuda.is_available())
    # run application
    app.run(
        host = '0.0.0.0', 
        port = 5000, 
        debug = True
    )   