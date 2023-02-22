from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from product.models import Product,CartItem
from .serializers import ProductSerializer,CartSerializer_two,CartSerializer


@api_view(['GET', 'POST'])
def products(request):
    """
    List all products, or create a new product.
    """
    if request.method == 'GET' : # list products
        products = Product.objects.all()
        products_serializer = ProductSerializer(products, many=True)
        return Response(products_serializer.data)

    elif request.method == 'POST': # create new product
        products_serializer  = ProductSerializer(data=request.data)
        if products_serializer .is_valid():
            products_serializer.save()
            return Response(products_serializer .data, status=status.HTTP_201_CREATED)
        return Response(products_serializer .errors, status=status.HTTP_400_BAD_REQUEST)    
    

   
class ProductDetail(APIView):
    """
    Retrieve, update or delete a snippet instance.
    """
    def get_object(self, pk):
        try:
            return Product.objects.get(pk=pk)
        except Product.DoesNotExist:
            raise Http404

    def get(self, pk):
        product = self.get_object(pk)
        products_serializer = ProductSerializer(product)
        return Response(products_serializer.data)

    def put(self, request, pk):
        product = self.get_object(pk)
        products_serializer = ProductSerializer(product, data=request.data)
        if products_serializer.is_valid():
            products_serializer.save()
            return Response(products_serializer.data)
        return Response(products_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self,pk):
        product = self.get_object(pk)
        product.status = 'AR'
        product.save()
        return Response(status=status.HTTP_204_NO_CONTENT)



@api_view(['GET', 'POST'])
def cart(request):
    if request.method == 'GET':
        cart_item = CartItem.objects.all()
        cart_serializer = CartSerializer_two(cart_item, many=True)
        return Response(cart_serializer.data)

    elif request.method == 'POST':
        cart_serializer = CartSerializer(data=request.data)
        if cart_serializer.is_valid():
            cart_serializer.save()
            return Response(cart_serializer.data, status=status.HTTP_201_CREATED)
        return Response(cart_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class CartDetail(APIView):
    """
    Retrieve, update or delete a snippet instance.
    """
    def get_object(self, pk):
        try:
            return CartItem.objects.get(pk=pk)
        except CartItem.DoesNotExist:
            raise Http404

    def get(self,pk):
        cart_item = self.get_object(pk)
        serializer = CartSerializer(cart_item)
        return Response(serializer.data)

    def put(self, request, pk):
        cart_item = self.get_object(pk)
        serializer = CartSerializer(cart_item, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, pk):
        cart_item = self.get_object(pk)
        cart_item.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    


