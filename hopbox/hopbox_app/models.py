from django.core.exceptions import ValidationError
from django.db import models
from django import forms
from django.forms.fields import EmailField
import re

def name_validator(value):
    if len(value) < 2:
        raise ValidationError(
            "first/last name must be longer than 1 character"
        )

def address_validator(value):
    ADD_REGEX = re.compile(r'\d+ [\w ]+,? [\w ]+,? ?\w{2}\s\d{5}')
    if not ADD_REGEX.match(value):
        raise ValidationError(
            "please input a valid street address, state abbreviation and zip code (ex: 123 Main St Anywhere GA 12345)"
        )

def password_validator(value):
    PW_REGEX = re.compile(r'^(?=.*\d)(?=.*[a-z])(?=.*[A-Z])(?=.*[a-zA-Z]).{8,}$')
    if not PW_REGEX.match(value):
        raise ValidationError(
            "password must be at least 8 characters, contain one uppercase letter, one lowercase letter, and one number"
        )

def review_validator(value):
    if len(value) < 10:
        raise ValidationError(
            "description must be at least 10 characters"
        )

# Create your models here.
# we don't need any validators because we will manually create the product objects
class Product(models.Model):
    description = models.TextField()
    image_path = models.CharField(max_length=255)
    image_alt = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Subscription(models.Model):
    description = models.TextField(null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    option_id = models.CharField(max_length=255, default="custom")
    selected_product = models.ManyToManyField(Product) # ManyToMany with product  
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    # subscription_reviews = list of all reviews for this subscription
    # users_subscribed = list of all users subscribed to this subscription

class User(models.Model):
    firstname = models.CharField(max_length=255, validators=[name_validator])
    lastname = models.CharField(max_length=255, validators=[name_validator])
    email = models.EmailField(max_length=254)
    password = models.CharField(max_length=255, validators=[password_validator])
    address = models.CharField(max_length=255, validators=[address_validator])
    subscribed_user = models.ForeignKey(Subscription, on_delete=models.CASCADE, related_name="users_subscribed", blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(auto_now=True, editable=False)
    # user_reviews = list of all reviews provided by this user
    # user_images = list of all images uploaded by user

class Review(models.Model):
    comment = models.TextField(validators=[review_validator])
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