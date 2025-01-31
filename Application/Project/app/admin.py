from django.contrib import admin
from .models import Post, Barangay, Service, Request, Feedback, UserProfile

admin.site.register(Post)
admin.site.register(Barangay)
admin.site.register(Service)
admin.site.register(Request)
admin.site.register(Feedback)
admin.site.register(UserProfile)
