from django.db import models


class Category(models.Model):
    """Profile status update"""

    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Library(models.Model):

    name = models.CharField(max_length=100)
    price = models.DecimalField(decimal_places=2, max_digits=3)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        """Return the model as a string."""

        return self.name
