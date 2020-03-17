"""learning_log URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls import include, url
from django.contrib import admin
 
urlpatterns = [
    #url(r'^admin/', include(admin.site.urls)), 
    url(r'^admin/', admin.site.urls),# 不用include()函数,a
    # url(r'^admin/', include(admin.site.urls)), 
    #url(r'', include(('learning_logs.urls'), namespace='learning_logs')),
    url(r'', include('learning_logs.urls')), # 或者修改为include(pattern_list)这种用法也是可以的！！！,a
    #path('admin/', admin.site.urls),
    #path('', include('learning_logs.urls')),
]
