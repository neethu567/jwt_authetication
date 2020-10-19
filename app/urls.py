# from mysite.app import views
from django.urls import path
from rest_framework.routers import SimpleRouter
from .views import studentviewset

router = SimpleRouter()
router.register('app', studentviewset, basename="app")
urlpatterns = router.urls





#
# urlpatterns = [
#     path('studentlist/', views.StudentList.as_view()),
#     path('studendetail/<int:pk>/', views.StudentDetail.as_view()),
# ]