from django.db import models


class Expense(models.Model):
    CATEGORY_CHOICES = [
        ("Food", "Food"),
        ("Travel", "Travel"),
        ("Utilities", "Utilities"),
    ]

    user = models.ForeignKey("user.User", on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    amount = models.PositiveIntegerField()
    date = models.DateField()
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES)

    def __str__(self):
        return f"{self.title} - {self.amount}"
