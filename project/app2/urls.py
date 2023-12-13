from django.urls import path
from .views import ProductDescriptionAPIView, ImageRecognitionAPIView

urlpatterns = [
    path('generate-product-description/', ProductDescriptionAPIView.as_view(), name='generate_product_description'),
    path('image-recognition/', ImageRecognitionAPIView.as_view(), name='image_recognition'),
]
