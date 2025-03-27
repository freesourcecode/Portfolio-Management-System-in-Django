from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from . import views

urlpatterns = [
    path('', views.login),
    path('login/' ,views.login,name = 'login'),
    path('signup/',views.signup,name = 'signup'),
    path('Home/',views.enter,name = 'enter'),
    path('stocks/',views.getStocks,name = 'getStock'),
    path('register/',views.register,name = 'register'),
    path('home/',views.home,name='home'),
    path('mystocks/',views.mystock,name = 'mystock'),
    path('stockadded/<int:slug>',views.addStocks,name='addStock'),
    path('stockdeleted/<int:slug>',views.deleteStocks,name='delete'),
    path('stock/',views.stock,name='stock'),
    path('about/',views.about,name='about'),
    path('profile/',views.profile,name='profile'),
    path('logout/',views.logout,name='logout'),
    path('know/',views.know,name = 'know'),
    path('house/',views.house,name = 'house'),
    path('houseg/',views.getBar,name = 'getB')
    
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)