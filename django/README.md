# models
The Model in Django is one of the most important components of the MVC (Model-View-Controller) or MTV (Model-Template-View) architecture. Models are responsible for managing data and defining the database structure. Let's explore this in more detail:

## What is a model?
A model in Django is a representation of data that allows you to define, store, retrieve, and perform various operations on data. Each model is defined as a Python class and a table is created in the database for it.

## Structure of a Model
Models are defined as classes, and each class represents a table. Each property of the class specifies a column in the table.

Simple example:

```python
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

```python
book = Book(title="Python Programming", author="John Doe", published_date="2023-01-01", price=49.99)
book.save()  
```
### 2. Reading data:


#### .All data
```python
books = Book.objects.all()
```

#### .Filter Data

'''python
books = Book.objects.filter(author="John Doe")

'''

### 3. Updata Data

'''python
book = Book.objects.get(id=1)  
book.price = 59.99  
book.save()  
'''

### 4. Delete Data

```python
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

```python
class Author(models.Model):
    name = models.CharField(max_length=100)

class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)

```

- Example of many-to-many relationship:
A student can have several classes and a class can have several students:

```python
class Student(models.Model):
    name = models.CharField(max_length=100)

class Class(models.Model):
    name = models.CharField(max_length=100)
    students = models.ManyToManyField(Student)


```

### **Migrations in Django**

**Migrations** in Django are a mechanism for managing and applying changes to the database schema. Whenever you create a new model or modify an existing one, you need to use migrations to apply those changes to the database.

---

### **Steps for Working with Migrations**

#### **1. Create Migration Files**
When you make changes to your models (like adding a new model or modifying a field), Django needs to be informed of these changes. You do this by running:

```bash
python manage.py makemigrations
```

- This command inspects your models and generates migration files in the `migrations` folder of your app.
- These files describe the changes that should be made to the database.

##### **Example:**
Suppose you add the following model to your app:
```python
class Author(models.Model):
    name = models.CharField(max_length=100)
```

After running `makemigrations`, Django will generate a migration file, like this:
```
Migrations for 'your_app_name':
  your_app_name/migrations/0001_initial.py
    - Create model Author
```

This migration file specifies that a new table `Author` needs to be created in the database.

---

#### **2. Apply Migrations to the Database**
Once the migration files are created, you apply them to the database with the following command:

```bash
python manage.py migrate
```

- This command reads the migration files and executes the necessary SQL commands to apply the changes to the database.

##### **Example:**
After running the `migrate` command:
- The `Author` table will be created in the database with a column for `id` (default primary key) and `name`.

---

### **Key Points About Migrations**

#### **1. Migrations Folder**
- Each app in Django has a `migrations` folder where migration files are stored.
- These files track the history of changes made to the database schema.

#### **2. Migration Files are Versioned**
- Migration files are numbered sequentially (e.g., `0001_initial.py`, `0002_auto.py`).
- The numbering ensures that migrations are applied in the correct order.

#### **3. Viewing Migration Status**
You can check the status of migrations using:

```bash
python manage.py showmigrations
```

**Example Output:**
```
[ ] 0001_initial
[X] 0002_add_new_field
```
- `[ ]`: The migration has not been applied.
- `[X]`: The migration has been applied.

#### **4. Rolling Back Migrations**
You can roll back to a specific migration version using:

```bash
python manage.py migrate your_app_name 0001
```

This will reverse all migrations applied after `0001`.

---

### **Typical Workflow**

1. **Define or Edit Models:**
   Modify your models in the `models.py` file.
   ```python
   class Book(models.Model):
       title = models.CharField(max_length=100)
   ```

2. **Create Migration Files:**
   Run `makemigrations` to create migration files.
   ```bash
   python manage.py makemigrations
   ```

3. **Apply Migrations:**
   Run `migrate` to apply the changes to the database.
   ```bash
   python manage.py migrate
   ```

---

### **Real-Life Example**

#### Step 1: Initial Model
Suppose you define a model like this:
```python
class Book(models.Model):
    title = models.CharField(max_length=100)
```

Run:
```bash
python manage.py makemigrations
python manage.py migrate
```
This creates the table `Book` in the database.

#### Step 2: Modify the Model
Later, you decide to add a new field:
```python
class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=50)  # New field
```

Run:
```bash
python manage.py makemigrations
python manage.py migrate
```

- A new migration file will be created to add the `author` field.
- After applying it, the `author` column will be added to the `Book` table in the database.

---

### **Why Migrations Are Important**

1. **Database Schema Management:** 
   Migrations ensure that your database schema is always synchronized with your models.
   
2. **Version Control:** 
   You can track changes to the schema and revert to earlier versions if needed.
   
3. **Automatic SQL Handling:** 
   Django generates and applies the necessary SQL commands, so you don’t need to write them manually.

---

### **Commands Summary**

| Command                                  | Purpose                                |
|------------------------------------------|----------------------------------------|
| `python manage.py makemigrations`        | Create migration files for model changes. |
| `python manage.py migrate`               | Apply migrations to the database.     |
| `python manage.py showmigrations`        | View migration status.                |
| `python manage.py migrate your_app_name 0001` | Roll back to a specific migration.    |






# Forms
Let me explain the difference between Model and Form in a simpler way with an example:


## 1. Model:
A model in Django represents the structure of your database. The model specifies what kind of data is stored in the database and how the data is related to each other.

Model properties:
It is responsible for defining and storing data in the database.
It defines all the columns (fields) in the database tables.
Example:
Suppose you want to store information about blog posts on your site. To do this, you define a model:

```python
from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=200)  
    content = models.TextField()            
    created_at = models.DateTimeField(auto_now_add=True)  
```

This model tells you:

- Each post has a title (text with a maximum of 200 characters).
- Each post has content (longer text).
- The creation date (created_at) is automatically saved.


## 2. form
A form is a tool used to receive data from the user and validate this data. A form helps you make sure that the data the user enters is correct and valid.

Form Features:
Responsible for receiving and processing user input.
Receives data from the user and validates it (for example, checks that the email is valid).
The data can be sent to a database or processed in some other way.
Example:
A form to get information about a blog post:

```python
from django import forms

class PostForm(forms.Form):
    title = forms.CharField(max_length=200, label="عنوان")
    content = forms.CharField(widget=forms.Textarea, label="محتوا")
```
This form asks the user to:
- Enter a title.
- Write some content.


Here’s the table explaining the main differences between **Model** and **Form** in English:

| **Feature**          | **Model**                                     | **Form**                                     |
|-----------------------|-----------------------------------------------|----------------------------------------------|
| **Purpose**           | Defines the structure of data in the database | Captures and validates data from the user    |
| **Usage**             | For storing and managing data in the database | For rendering forms in HTML and processing user input |
| **Database Connection** | Direct (Model is directly tied to database tables) | Indirect (Form itself does not save data)    |

In Django, Form is one of the key components used to manage and validate user input. Forms are used in Django in two main ways: regular forms and model forms.


### 1. Forms:
These types of forms are manually defined and are used to process data that is not necessarily associated with a model.

Structure:
To create a form, you must use the forms.Form class. Each field in the form is defined as an attribute that specifies the data type and its properties.


```python
from django import forms

class ContactForm(forms.Form):
    name = forms.CharField(max_length=100, label='نام')
    email = forms.EmailField(label='ایمیل')
    message = forms.CharField(widget=forms.Textarea, label='پیام')
```

Description:
- CharField: For text data.
- EmailField: For email and its validation.
- widget: To specify the HTML input type (e.g. Textarea for long texts).

### 2. ModelForms:
These types of forms are used to create forms that are directly connected to database models. ModelForms make things much easier because you don't need to manually define fields and can extract fields directly from the model.

Structure:
To create a modelform, the forms.ModelForm class is used.

Let's say we have a model called Post:
```python
from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
```

You can create a modelform for this model:
```python
from django import forms
from .models import Post

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content']

```

# Views
In Django, Views are one of the main and key parts of the framework that are responsible for processing requests received from the user and returning the appropriate response to him. Views are actually a bridge between Models and Templates and manage the logic of the application.


## Types of Views in Django:
1. Function-based Views (FBV): 

    is a simple function in Python that takes an HttpRequest object as input and returns an HttpResponse object.
    This type of view is usually used for simple logic.

    ```python
    from django.http import HttpResponse

    def my_view(request):
        return HttpResponse("Hello, World!")
    ```


2. Class-based Views (CBV)
    In this type of view, classes are used instead of functions. This approach makes the code more structured and extensible.
    View-based classes inherit from the base View class, which is located in the django.views module.


    ```python
    from django.http import HttpResponse
    from django.views import View

    class MyView(View):
        def get(self, request):
            return HttpResponse("Hello, World!")
    ```

3. Generic Views
    Django provides a set of ready-made Generic Views that are used to perform common operations such as displaying a list, detailing an object, creating, updating, and deleting an object. These views reduce development time.
    ```python 
    from django.views.generic import ListView
    from .models import MyModel

    class MyModelListView(ListView):
        model = MyModel
        template_name = 'myapp/mymodel_list.html'

    ```



## How a View Works
Receives a request:
When a user requests a specific URL, Django first looks up the URL in the urls.py file and finds the corresponding View.

Processes logic:
The View (either a function or a class) executes the logic related to the request. This logic can include retrieving information from the database, validating data, or processing forms.

Returns the response:
Finally, the View returns a response (usually an HttpResponse or HTML page) to the user.



# Serializers
In Django, Serializers are tools for converting data between different types (such as database models and JSON or XML formats). In other words, a serializer converts data from complex model forms into transportable formats (such as JSON), and also converts input data into formats that can be used in models.


## Types of Serializers in Django

1. Basic Serializer: This type of serializer converts simple and primitive data into various formats. For example, it converts a list of data (such as a dictionary or a list) into JSON format or other formats.

Example:

```python
from rest_framework import serializers

class PersonSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=100)
    age = serializers.IntegerField()

```


2. ModelSerializer: This type of serializer is a faster and easier way to work with models. The ModelSerializer automatically serializes model fields, making it easier to convert data to and from Django models.


```python
from rest_framework import serializers
from .models import Person

class PersonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Person
        fields = ['name', 'age']   

```

## Main uses of Serializers
- Exchange data between client and server: Use formats like JSON to send and receive data.
- Data validation: To ensure the correctness of data before storing it in the database.
- Simplify API creation: Use ModelSerializer to quickly transform data and store it in the database.
- Additional features and capabilities
- Validation: You can add custom validations for data.