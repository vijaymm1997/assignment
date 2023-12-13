import requests
from django.conf import settings

def generate_product_description(title):
    # Use OpenAI API or any other text completion API
    # Replace 'YOUR_OPENAI_API_KEY' with your actual API key
    api_key = settings.OPENAI_API_KEY
    endpoint = 'https://api.openai.com/v1/complete'

    headers = {'Authorization': f'Bearer {api_key}'}
    data = {'prompt': f'Generate a product description for {title}', 'max_tokens': 200}

    response = requests.post(endpoint, headers=headers, data=data)
    description = response.json().get('choices', [])[0].get('text', '')

    return description

def extract_keywords_from_text(text):
    # Extract keywords from the text (you can use any keyword extraction method)
    # Here, we are using a simple approach by splitting the text into words
    keywords = text.split()
    return keywords

def extract_keywords_from_image(image_path):
    # Use Google Cloud Vision API or OpenCV for image recognition
    # Replace 'YOUR_GOOGLE_API_KEY' with your actual API key
    api_key = 'YOUR_GOOGLE_API_KEY'
    endpoint = 'https://vision.googleapis.com/v1/images:annotate'

    # Prepare the image data
    with open(image_path, 'rb') as image_file:
        image_data = image_file.read()

    # Prepare the request payload
    request_data = {
        'requests': [
            {
                'image': {'content': image_data},
                'features': [{'type': 'TEXT_DETECTION'}, {'type': 'LABEL_DETECTION'}]
            }
        ]
    }

    params = {'key': api_key}
    response = requests.post(endpoint, params=params, json=request_data)
    keywords = []

    # Extract keywords from the response (you may need to adapt this based on the API used)
    response_data = response.json()
    text_annotations = response_data.get('responses', [{}])[0].get('textAnnotations', [])
    label_annotations = response_data.get('responses', [{}])[0].get('labelAnnotations', [])

    for annotation in text_annotations:
        keywords.append(annotation.get('description', ''))

    for annotation in label_annotations:
        keywords.append(annotation.get('description', ''))

    return keywords
