from django.db import models
import re
import bcrypt


# Create your models here.
class Product(models.Model):
    description = models.TextField()
    image_path = models.CharField(max_length=255)
    image_alt = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Subscription(models.Model):
    description = models.TextField()
    price = price = models.DecimalField(max_digits=10, decimal_places=2)
    option_id = models.CharField(max_length=20, default="1")
    selected_product = models.ManyToManyField(Product) #ManyToMany with product  
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    #subscription_reviews =
    #user_subscription = 

class User(models.Model):
    firstname = models.CharField(max_length=255)
    lastname = models.CharField(max_length=255)
    email = models.EmailField(max_length=254)
    pw_hash = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    subscribeded_user = models.ForeignKey(Subscription, on_delete=models.CASCADE, related_name="user_subscription", blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    #user_reviews = 
    #user_images = 

class Review(models.Model):
    comment = models.TextField()
    submited_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name="user_reviews", blank=True, null=True)
    review_of = models.ForeignKey(Subscription, on_delete=models.CASCADE, related_name="subscription_reviews", blank=True, null=True)
    score = models.IntegerField(default=5)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    #review_image =

class UserImage(models.Model):
    user_image_path = models.CharField(max_length=255)
    user_image_alt = models.CharField(max_length=255)
    image_for_review = models.ForeignKey(Review, on_delete=models.CASCADE, related_name="review_image", blank=True, null=True)
    image_from_user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="user_images", blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)