from django.urls import path
from .views import (
    home,
    about,
    register,
    login_view,
    user_profile,
    post_list,
    post_detail,
    post_create,
    post_update,
    post_delete,
    barangay_list,
    barangay_detail,
    barangay_create,
    barangay_update,
    barangay_delete,
    service_list,
    service_detail,
    service_create,
    service_update,
    service_delete,
    userprofile_list,
    userprofile_detail,
    userprofile_create,
    userprofile_update,
    userprofile_delete,
    request_list,
    request_detail,
    request_create,
    request_update,
    request_delete
)

urlpatterns = [
    path('', home, name='home'),
    path('about/', about, name='about'),
    path('register/', register, name='register'),  # URL for registration
    path('login/', login_view, name='login'),      # URL for login
    path('profile/', user_profile, name='user-profile'),  # URL for user profile

    # Post URLs
    path('posts/', post_list, name='post-list'),
    path('posts/<int:pk>/', post_detail, name='post-detail'),
    path('posts/create/', post_create, name='post-create'),
    path('posts/<int:pk>/update/', post_update, name='post-update'),
    path('posts/<int:pk>/delete/', post_delete, name='post-delete'),

    # Barangay URLs
    path('barangays/', barangay_list, name='barangay-list'),
    path('barangays/<int:pk>/', barangay_detail, name='barangay-detail'),
    path('barangays/create/', barangay_create, name='barangay-create'),
    path('barangays/<int:pk>/update/', barangay_update, name='barangay-update'),
    path('barangays/<int:pk>/delete/', barangay_delete, name='barangay-delete'),

    # Service URLs
    path('services/', service_list, name='service-list'),
    path('services/<int:pk>/', service_detail, name='service-detail'),
    path('services/create/', service_create, name='service-create'),
    path('services/<int:pk>/update/', service_update, name='service-update'),
    path('services/<int:pk>/delete/', service_delete, name='service-delete'),

    # UserProfile URLs
    path('userprofiles/', userprofile_list, name='userprofile-list'),
    path('userprofiles/<int:pk>/', userprofile_detail, name='userprofile-detail'),
    path('userprofiles/create/', userprofile_create, name='userprofile-create'),
    path('userprofiles/<int:pk>/update/', userprofile_update, name='userprofile-update'),
    path('userprofiles/<int:pk>/delete/', userprofile_delete, name='userprofile-delete'),

    # Request URLs
    path('requests/', request_list, name='request-list'),
    path('requests/<int:pk>/', request_detail, name='request-detail'),
    path('requests/create/', request_create, name='request-create'),
    path('requests/<int:pk>/update/', request_update, name='request-update'),
    path('requests/<int:pk>/delete/', request_delete, name='request-delete'),
]
