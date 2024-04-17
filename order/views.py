from rest_framework import viewsets, status
from rest_framework.views import APIView
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from .models import Order
from .serializers import OrderSerializer
from category.models import flower
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string

class PlaceOrderView(APIView):
    def post(self, request):
        user = request.user
        flower_id = request.data.get('flower_id')
        if flower_id:
            flower_instance = get_object_or_404(flower, id=flower_id)
            if flower_instance.quantity > 0:
                # Reduce the quantity by 1
                flower_instance.quantity -= 1
                flower_instance.save()
                # Create the order
                order = Order.objects.create(user=user, flower=flower_instance)
                serializer = OrderSerializer(order)
                # Send order confirmation email
                try:
                    email_subject = "Order Confirmation"
                    email_body = render_to_string('order_confirmation_email.html', {'order': order})
                    
                    email = EmailMultiAlternatives(email_subject, '', to=[user.email])
                    email.attach_alternative(email_body, "text/html")
                    email.send()
                except Exception as e:
                    print(f"Error sending email: {e}")
                    # If there's an error sending the email, still return the response with order details
                    return Response(serializer.data, status=status.HTTP_201_CREATED)
                
                # If email is sent successfully, return success response
                return Response(serializer.data, status=status.HTTP_201_CREATED)
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            else:
                return Response({'message': 'Flower out of stock'}, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response({'message': 'Flower ID is required'}, status=status.HTTP_400_BAD_REQUEST)
        
class OrderHistoryView(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

    def get_queryset(self):
        queryset = super().get_queryset()
        user_id = self.request.query_params.get('user_id')
        if user_id:
            queryset = queryset.filter(user_id=user_id)
        return queryset
