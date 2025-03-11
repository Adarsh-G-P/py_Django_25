from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CollectionViewSet, PromotionViewSet, ProductViewSet, CustomerViewSet,OrderViewSet, AddressViewSet, OrderItemViewSet, CartViewSet, CartItemViewSet

router = DefaultRouter()
router.register(r'collections', CollectionViewSet)
router.register(r'promotions', PromotionViewSet)
router.register(r'products', ProductViewSet)
router.register(r'customers', CustomerViewSet)
router.register(r'orders', OrderViewSet)
router.register(r'addresses', AddressViewSet)
router.register(r'order-items', OrderItemViewSet)
router.register(r'carts', CartViewSet)
router.register(r'cart-items', CartItemViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
