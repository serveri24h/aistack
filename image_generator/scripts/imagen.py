import requests

url = 'http://localhost:11434/api/generate'
payload = {
    'model': 'imagen',
    'prompt': 'A futuristic cityscape at sunset',
    'options': {
        'num_images': 1
    }
}
response = requests.post(url, json=payload)
image_url = response.json().get('image_url')
print(f'Generated Image URL: {image_url}')