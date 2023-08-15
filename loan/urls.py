from django.urls import path
from loan import views
from rest_framework.routers import DefaultRouter,SimpleRouter


router = SimpleRouter()
router.register(r'loan-beneficaries',views.AllLoanBeneficaries,basename="loan-beneficaries")
router.register(r'loan-transactions',views.AllLoanTransactions,basename="loan-transactions")


urlpatterns = [

]
urlpatterns+= router.urls
