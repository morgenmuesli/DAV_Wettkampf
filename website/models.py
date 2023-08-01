from django.db import models

CATEGORY_CHOICES = [
    ("AT", "athlete"),
    ("TR", "trainer")
]


# Create your models here.
class Member(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    image = models.ImageField()
    birth_date = models.DateField()
    category = models.CharField(max_length=2, choices=CATEGORY_CHOICES)

    def is_trainer(self):
        if self.category == "TR":
            return True
        return False
