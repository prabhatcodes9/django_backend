from django.urls import path
from rest_framework.routers import SimpleRouter
from . import views
from pprint import pprint

router = SimpleRouter()
router.register('products', views.ProductViewSet)
router.register('collections', views.CollectionViewSet)
pprint(router.urls)

# URLConf
urlpatterns = router.urls