from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CategoryViewSet, ProductViewSet, ShopViewSet, CategoryByShopSlugView

router = DefaultRouter()
router.register(r'shops', ShopViewSet)
router.register(r'categories', CategoryViewSet)
router.register(r'products', ProductViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
    path('api/<slug:shop_slug>/categories', CategoryByShopSlugView.as_view(), name='category-by-shop-slug'),
]
