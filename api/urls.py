from django.urls import path, re_path
from api.views import views, auth
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt import views as jwt_views


router = DefaultRouter()
router.register('providers', views.ProviderViewSet, basename='providers')  
router.register('orders', views.OrderViewSet, basename='orders')           
router.register('categories', views.CategoryViewSet, basename='categories')
router.register('reviews', views.ReviewViewSet, basename='reviews')        
router.register('products', views.ProductViewSet, basename='products')     
router.register('profiles', auth.UserProfileViewSet, basename='profiles')  
router.register('logout', auth.LogoutViewSet, basename='logout')           
router.register('signup', auth.SignUpViewSet, basename='signup')           

urlpatterns = [
    path('categories/<int:pk>/products/', views.CategoryProductsView.as_view()),
    path('providers/<int:pk>/products/', views.ProviderProductsView.as_view()),
    path('users/', auth.UserList.as_view()),
    path('login/', jwt_views.TokenObtainPairView.as_view(), name='token_obtain_pair'), 
    path('login/refresh', jwt_views.TokenRefreshView.as_view(), name='token_refresh'), 
]
urlpatterns+=router.urls