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
        products = Product.objects.filter(archived=False)
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


@api_view(['GET', 'PUT', 'DELETE'])
def cart_detail(request, pk):
    try:
        cart_item = CartItem.objects.get(id=pk)
    except CartItem.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    # get product
    if request.method == 'GET':
        cart_serializer = CartSerializer_two(cart_item, many=False)
        return Response(cart_serializer.data)

    if request.method == 'DELETE':
        cart_item.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    # update product
    if request.method == 'PUT':
        cart_serializer = CartSerializer_two(instance=cart_item, data=request.data)
        if cart_serializer.is_valid():
            cart_serializer.save()
            return Response(cart_serializer.data, status=status.HTTP_201_CREATED)
        return Response(cart_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
