from django.db import models
from datetime import date
from django.contrib.auth.models import User


class Task(models.Model):
    PRIORITY_CHOICES = [
        ("Low", "Low"),
        ("Medium", "Medium"),
        ("High", "High"),
    ]

    CATEGORY_CHOICES = [
        ("Study", "Study"),
        ("Work", "Work"),
        ("Personal", "Personal"),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    description = models.TextField()
    is_completed = models.BooleanField(default=False)
    due_date = models.DateField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    priority_choices = models.CharField(
        max_length=10,
        choices=PRIORITY_CHOICES,
        default="Medium",
    )
    category_choices = models.CharField(
        max_length=10,
        choices=CATEGORY_CHOICES,
        default="Study",
    )

    @property
    def status(self):
        today = date.today()

        if self.is_completed:
            return "Completed"

        if not self.due_date:
            return "No Due Date"

        if self.due_date < today:
            return "Overdue"
        elif self.due_date == today:
            return "Due Today"
        else:
            return "Upcoming"

    def __str__(self):
        return self.title
