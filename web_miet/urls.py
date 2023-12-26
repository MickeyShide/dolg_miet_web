"""
URL configuration for web_miet project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.contrib import admin
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.template.defaulttags import url
from django.urls import path, include

from users import views as users_views
from web_miet import views, settings
from web_miet.models import Work, LikeDislike

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/subjects', views.subject_list),
    path('api/prepods', views.prepod_list),
    path('api/works', views.work_list),
    path('api/likes_count/<int:id>', views.likes_count),
    path('', views.index),
    path('subject/<int:id>/', views.show_subject),
    path('registration/', users_views.registration),
    path('login/', users_views.login, name='login'),
    path('logout/', logout, ),
    path('api/work/<int:pk>/like/', login_required(views.VotesView.as_view(model=Work, vote_type=LikeDislike.LIKE)), name='work_like'),
    path('api/work/<int:pk>/dislike/', login_required(views.VotesView.as_view(model=Work, vote_type=LikeDislike.DISLIKE)), name='work_dislike'),
]
