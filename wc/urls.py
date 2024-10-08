"""
URL configuration for deformback project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from django.urls import path
from .views import BlockView, PaymentView, ProductView, PostView, MediaView, OrderView, UserView

urlpatterns = [
    # block
    path('get-all/', BlockView.getAll, name='get_all'),
    path('get-block/', BlockView.get, name='get_block'),
    path('add-block/', BlockView.add, name='add_block'),
    path('update-block/', BlockView.update, name='update_block'),
    path('delete-block/', BlockView.delete, name='delete_block'),
    path('delete-block-by-user-id/', BlockView.deleteByUserId, name='delete_block_by_user_id'),

    # product
    path('add-product/', ProductView.add, name='add_product'),
    path('create-product/',ProductView.create, name='create_product'),

    # post
    path('create-post/',PostView.create, name='create_post'),
    path('update-post/',PostView.update, name='update_post'),
    path('get-post/',PostView.get, name='get_post'),
    path('delete-post/',PostView.delete, name='delete_post'),

    # media
    path('add-media/',MediaView.add, name='add_media'),
    path('delete-media/',MediaView.delete, name='delete_media'),
    path('get-media-by-author/',MediaView.get_media_by_author, name='get_media_by_author'),

    #order
    path('make-order/',OrderView.make_order, name='make_order'),

    #user
    path('get-user/',UserView.get_user, name='get_user'),
    path('add-auth/',UserView.add_auth, name='add_auth'),
    path('get-auth/',UserView.get_auth, name='get_auth'),
    path('update-auth/',UserView.update_auth, name='update_auth'),
    path('delete-auth/',UserView.delete_auth, name='delete_auth'),
    path('delete-auth-all/',UserView.delete_auth_all, name='delete_auth')

    # payment
    path('get-all-payments/',PaymentView.get_all_payments, name='get_all_payments'),
]
