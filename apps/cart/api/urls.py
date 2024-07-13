from rest_framework.routers import DefaultRouter
from apps.cart.api.views import CartViewSet

router = DefaultRouter()

router.register(r'carts', CartViewSet)
# router.register(r'items', ItemViewSet)

urlpatterns = router.urls
