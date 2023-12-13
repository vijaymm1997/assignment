from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Product, ProductDescription
from .serializers import ProductDescriptionSerializer
from .utils import generate_product_description, extract_keywords_from_text, extract_keywords_from_image

class ProductDescriptionAPIView(APIView):
    def post(self, request, *args, **kwargs):
        title = request.data.get('title', '')

        # Generate product description
        description = generate_product_description(title)

        # Save product description to the database
        product = Product.objects.create(title=title)
        ProductDescription.objects.create(product=product, description=description)

        # Extract keywords from the generated description
        keywords = extract_keywords_from_text(description)

        # Serialize the response
        serializer = ProductDescriptionSerializer({'description': description, 'keywords': keywords})
        return Response(serializer.data, status=status.HTTP_200_OK)

class ImageRecognitionAPIView(APIView):
    def post(self, request, *args, **kwargs):
        image_path = 'path/to/IELTS-template.jpg'  # Replace with the actual path to the image file

        # Extract keywords from the image
        keywords = extract_keywords_from_image(image_path)

        # Serialize the response
        response_data = {'keywords': keywords}
        return Response(response_data, status=status.HTTP_200_OK)
