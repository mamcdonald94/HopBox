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
    price = models.DecimalField(max_digits=10, decimal_places=2)
    option_id = models.CharField(max_length=20, default="1")
    selected_product = models.ManyToManyField(Product) # ManyToMany with product  
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    # subscription_reviews = list of all reviews for this subscription
    # users_subscribed = list of all users subscribed to this subscription

class User(models.Model):
    firstname = models.CharField(max_length=255)
    lastname = models.CharField(max_length=255)
    email = models.EmailField(max_length=254)
    password = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    subscribed_user = models.ForeignKey(Subscription, on_delete=models.CASCADE, related_name="users_subscribed", blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    # user_reviews = list of all reviews provided by this user
    # user_images = list of all images uploaded by user

class Review(models.Model):
    comment = models.TextField()
    submitted_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name="user_reviews", blank=True, null=True)
    review_of = models.ForeignKey(Subscription, on_delete=models.CASCADE, related_name="subscription_reviews", blank=True, null=True)
    score = models.IntegerField(default=5)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    # review_image = image associated with this review

class UserImage(models.Model):
    user_image_path = models.CharField(max_length=255)
    user_image_alt = models.CharField(max_length=255)
    image_for_review = models.OneToOneField(Review, on_delete=models.CASCADE, related_name="review_image", blank=True, null=True)
    image_from_user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="user_images", blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)