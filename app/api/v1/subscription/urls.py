from django.urls import path


from app.api.v1.subscription.views import SubscriptionCreate, SubscriptionDelete, SubscriptionList

urlpatterns = [


    path('subscriptions/create/', SubscriptionCreate.as_view(), name='create_view'),
    path('subscriptions/', SubscriptionList.as_view(), name='list_view'),
    path('subscriptions/delete/<int:pk>/', SubscriptionDelete.as_view(), name='delete_view'),

]
