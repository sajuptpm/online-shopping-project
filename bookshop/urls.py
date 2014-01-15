from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    

    url(r'^admin/', include(admin.site.urls)),
    url(r'^users/add$','book.views.add_user', name='adduser'),
    url(r'^users/login$','book.views.login_user', name='loginuser'),
    url(r'^products/add','book.views.add_product', name='addproduct')
    #url(r'^users/product$','book.views.add_product', name='addproduct')

)
