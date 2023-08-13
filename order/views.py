
from rest_framework.response import Response
from rest_framework.views import APIView
from cart.models import Cart
from cart.views import calcCart
from .models import *

class CreateOrder(APIView):
    def post(self,request):
        data = request.data
        session_id = data['session_id']
        cart = Cart.objects.get(sessionID=session_id)
        order = Order.objects.create(**data)
        order.totalPrice = cart.totalPrice
        order.save()
        for cart_product in cart.products.all():
            OrderItem.objects.create(
                order=order,
                product=cart_product.product,
                productPrice=cart_product.productPrice,
                amount=cart_product.amount,
                totalPrice=cart_product.totalPrice,

            )
            cart_product.delete()
            calcCart(cart)

        return Response(status=200)
