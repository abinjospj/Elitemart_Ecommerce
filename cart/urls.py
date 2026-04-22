from django.urls import path
from cart import views
app_name = 'cart'

urlpatterns = [
    path('cart/<int:i>', views.AddToCart.as_view(), name='addtocart'),
    path('cartview', views.CartView.as_view(), name='cartview'),
    path('cartremove/<int:i>', views.CartRemove.as_view(), name='cartremove'),
    path('cartdecrement/<int:i>', views.CartDecrement.as_view(), name='cartdecrement'),
    path('checkout', views.Checkout.as_view(), name='checkout'),
    path('paymentsuccess', views.PaymentSuccess.as_view(), name='paymentsuccess'),
    
    path('summary/', views.OrderSummary.as_view(), name='summary'),


]