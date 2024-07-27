from django.urls import path, include
from rest_framework.routers import DefaultRouter
from vanroute.views import AlunoViewSet, MotoristaViewSet, EnderecoViewSet, VanViewSet, optimize_route
from django.contrib import admin

router = DefaultRouter()
router.register(r'alunos', AlunoViewSet)
router.register(r'motoristas', MotoristaViewSet)
router.register(r'enderecos', EnderecoViewSet)
router.register(r'vans', VanViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('admin/', admin.site.urls),
    path('optimize-route/<int:van_id>/', optimize_route, name='optimize_route'),
]
