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
    

   
@api_view(['GET', 'PUT', 'DELETE'])
def product_detail(request, pk):
    try:
        product = Product.objects.get(id=pk)
    except Product.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    # get product
    if request.method == 'GET':
        serializer = ProductSerializer(product, many=False)
        return Response(serializer.data)

    # archive product(not really deleting it)
    if request.method == 'DELETE':
        product.archived = True
        product.save()
        return Response(status=status.HTTP_204_NO_CONTENT)

    # update product
    if request.method == 'PUT':
        serializer = ProductSerializer(instance=product, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
"""
class ProductDetail(APIView):
    def single_product(request, pk):
        try:
            product = Product.objects.get(id=pk)
        except Product.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def get(self, request, pk, format=None):
        product = self.get_object(pk)
        products_serializer = ProductSerializer(product)
        return Response(products_serializer.data)

    def put(self, request, pk, format=None):
        product = self.get_object(pk)
        products_serializer = ProductSerializer(product, data=request.data)
        if products_serializer.is_valid():
            products_serializer.save()
            return Response(products_serializer.data)
        return Response(products_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        product = self.get_object(pk)
        product.status = 'AR'
        product.save()
        return Response(status=status.HTTP_204_NO_CONTENT)
"""

@api_view(['GET', 'POST'])
def cart(request):
    """
    List all cart items, or create a new item.
    """
    if request.method == 'GET': # list cart 
        cart = CartItem.objects.all()
        cart_serializer = CartSerializer_two(cart, many=True)
        return Response(cart_serializer.data)

    elif request.method == 'POST': # create new cart
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

    def get(self, request, pk, format=None):
        cart_item = self.get_object(pk)
        serializer = CartSerializer(cart_item)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        cart_item = self.get_object(pk)
        serializer = CartSerializer(cart_item, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        cart_item = self.get_object(pk)
        cart_item.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    


@api_view(['POST'])
def add_to_cart(request,product_id):
    if request.method == 'POST': # create new product
        serializer = CartSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)    