from django.conf.urls import url
from testapp import views

urlpatterns = [
    url('about',views.About),
    url('contact',views.showContact),
    url('^$',views.greeting),

]
