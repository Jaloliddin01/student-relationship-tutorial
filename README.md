# student_relationship

This is a simple Django project that demonstrates how to create a one-to-one relationship between two models.

## Database schema

1.Student

| Column Name | Data Type | Description |
| :--- | :--- | :--- |
| id | integer | Primary key |
| first\_name | string |  Student first name |
| last\_name | string | Student last name |

2.Contact

| Column Name | Data Type | Description |
| :--- | :--- | :--- |
| id | integer | Primary key |
| phone | string | Student phone number |
| email | string | Student email address |

3.Address

| Column Name | Data Type | Description |
| :--- | :--- | :--- |
| id | integer | Primary key |
| street | string | Student street address |
| city | string | Student city |
| country | string | Student country |

## Django Models

```python

class Student(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)

    def __str__(self):
        return self.first_name + ' ' + self.last_name

class Contact(models.Model):
    phone = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    student = models.OneToOneField(Student, on_delete=models.CASCADE)

    def __str__(self):
        return self.phone + ' ' + self.email

class Address(models.Model):
    street = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    country = models.CharField(max_length=50)
    student = models.OneToOneField(Student, on_delete=models.CASCADE)

    def __str__(self):
        return self.street + ' ' + self.city + ' ' + self.country

```

## Getting data from a one-to-one relationship

```python

student = Student.objects.get(id=1)
contact = student.contact
address = student.address

```

## Creating a one-to-one relationship
