from django.urls import path
from contructors import views
from rest_framework.routers import DefaultRouter,SimpleRouter


router = SimpleRouter()
router.register(r'contructor-beneficaries',views.ContructorBeneficariesViews,basename="contructor-beneficaries")

urlpatterns = [
   
]
urlpatterns+= router.urls