from django.db import models
import bcrypt

# Create your models here.
# models for class creation -- always makemigrations and migrate anytime we change models.py

# django auto mak                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             es ids and auto incrementing


class User(models.Model):
    first_name = models.CharField(max_length=60)
    last_name = models.CharField(max_length=60)
    email = models.CharField(max_length=60)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Movie(models.Model):
    title = models.CharField(max_length=45)
    description = models.TextField()
    release_date = models.DateField
    duration = models.IntegerField
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Hogwarts(models.Model):
    name = models.CharField(max_length=45)
    house = models.CharField(max_length=45)
    pet = models.CharField(max_length=45)
    year = models.IntegerField()


class Users(models.Model):
    first_name = models.CharField(max_length=45)
    last_name = models.CharField(max_length=45)
    email_address = models.CharField(max_length=45)
    age = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    objects = UserManager()


class UserManager(models.Manager):
    def validator(self, postData):
        errors = {}

        if len(postData['first_name']) < 2:
                errors['first_name'] = 'Your first name is too short'

        if len(postData['last_name']) < 2:
                errors['last_name'] = 'Your first name is too short'
        
        if len(postData['email']) < 2:
                errors['email'] = 'Your first name is too short'
        


class Shirt(models.Model):
    size = models.CharField(max_length=60)
    color = models.CharField(max_length=60)
    material = models.CharField(max_length=60)

    created_by = models.ForeignKey(User, related_name='users')
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

# To add a new record to a table:
#     ClassName.objects.create(field1="value for field1", field2="value for field2", etc.)
#     SQL Equivalent: "INSERT INTO tablename (field1, field2) VALUES ('value for field1', 'value for field2');"

    # person1 = User.objects..get(first_name = 'francisco')
    #person1.first_name = 'zach'
    # person1.save()

# ONE TO  MANY RELATIONSHIPS IN DATABASE
# class Author(models.Model):
#     name = models.CharField(max_length=255)
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)


# class Book(models.Model):
#     title = models.CharField(max_length=255)
#     author = models.ForeignKey(Author, related_name="books") #ONE AUTHOR CAN HAVE MANY BOOKS
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)


# this_author = Author.objects.get(id=2)	# get an instance of an Author
# my_book = Book.objects.create(title="Little Women", author=this_author)	# set the retrieved author as the author of a new book

# # or in one line...
# my_book = Book.objects.create(title="Little Women", author=Author.objects.get(id=2))

# some_book = Book.objects.get(id=5)

# some_book.author	# returns the Author instance associated with this book

# some_book.author.name		# return the name of the author of this book
# some_book.author.id		# returns the id of the author of this book


# #FIND ALL BOOKS BY AUTHOR ID=2
# this_author = Author.objects.get(id=2)
# books = Book.objects.filter(author=this_author)

# # one-line version:
# books = Book.objects.filter(author=Author.objects.get(id=2))
