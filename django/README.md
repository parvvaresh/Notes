# models
The Model in Django is one of the most important components of the MVC (Model-View-Controller) or MTV (Model-Template-View) architecture. Models are responsible for managing data and defining the database structure. Let's explore this in more detail:

## What is a model?
A model in Django is a representation of data that allows you to define, store, retrieve, and perform various operations on data. Each model is defined as a Python class and a table is created in the database for it.

## Structure of a Model
Models are defined as classes, and each class represents a table. Each property of the class specifies a column in the table.

Simple example:

```
from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=100)  
    author = models.CharField(max_length=50)  
    published_date = models.DateField()       
    price = models.DecimalField(max_digits=10, decimal_places=2)  

    def __str__(self):
        return self.title


```
## Working with Models in the Database
You can use Django's Object Relationship Manager (ORM) to work with models.

### 1. Add data:

```
book = Book(title="Python Programming", author="John Doe", published_date="2023-01-01", price=49.99)
book.save()  
```
### 2. Reading data:


#### .All data
```
books = Book.objects.all()
```

#### .Filter Data

'''
books = Book.objects.filter(author="John Doe")

'''

### 3. Updata Data

'''
book = Book.objects.get(id=1)  
book.price = 59.99  
book.save()  
'''

### 4. Delete Data

```
book = Book.objects.get(id=1)
book.delete()
```
## Commonly used fields in models

Field | Usage  
---|---  
**CharField** | Used to store short strings (e.g., names or titles).  
**TextField** | Used to store long strings (e.g., descriptions).  
**IntegerField** | Used to store integers.  
**DecimalField** | Used to store decimal numbers (e.g., prices).  
**DateField** | Used to store dates.  
**DateTimeField** | Used to store both date and time.  
**BooleanField** | Used to store `True` or `False` values.  
**ForeignKey** | Used to create a one-to-many relationship with another model.  
**ManyToManyField** | Used to create a many-to-many relationship between models.  


## Creating relationships between models

Models can be related to each other and you can easily define relationships.


- Example of a One-to-Many relationship:
An author can have multiple books:

```

```