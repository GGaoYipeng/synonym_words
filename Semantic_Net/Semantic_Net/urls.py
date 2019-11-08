"""Semantic_Net URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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

# official code
# from django.contrib import admin
# from django.urls import path
#
# urlpatterns = [
#     path('admin/', admin.site.urls),
# ]

"""
绑定URL与视图
"""
# from django.conf.urls import url
# from . import view
#
# urlpatterns = [
#     url(r'^$', view.hello),
# ]


"""
Django path() 可以接收四个参数，分别是两个必选参数：route、view 和两个可选参数：kwargs、name。
"""
from django.urls import path
from . import view

urlpatterns = [
    path('homepage/', view.main),
    path('similarwords/', view.similarwords),
    path('similarlists/', view.similarlists),
    path('differentword/', view.differentword),
    path('synonymwords/', view.sysnonymwords)
]