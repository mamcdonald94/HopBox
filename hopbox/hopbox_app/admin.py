from django.contrib import admin
from django.urls import path, include
from hopbox_app.models import *

class UserAdmin(admin.ModelAdmin):
    pass
admin.site.register(User, UserAdmin)

class ProductAdmin(admin.ModelAdmin):
    pass
admin.site.register(Product, UserAdmin)

class SubscriptionAdmin(admin.ModelAdmin):
    pass
admin.site.register(Subscription, UserAdmin)

class ReviewAdmin(admin.ModelAdmin):
    pass
admin.site.register(Review, UserAdmin)

class UserImageAdmin(admin.ModelAdmin):
    pass
admin.site.register(UserImage, UserAdmin)