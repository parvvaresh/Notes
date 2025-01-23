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
class Author(models.Model):
    name = models.CharField(max_length=100)

class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)

```

- Example of many-to-many relationship:
A student can have several classes and a class can have several students:

```
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

