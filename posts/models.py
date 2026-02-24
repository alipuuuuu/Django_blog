import datetime
from django.utils import timezone
from django.db import models
from django.contrib import admin

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100, unique=True)
    parent = models.ForeignKey(
        "self",
        null=True, blank=True,
        related_name="children",
        on_delete=models.CASCADE,
    )

    class Meta:
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.name

class Post(models.Model):
    STATUS_CHOICES = [("draft", "Draft"), ("published", "Published")]

    title = models.CharField(max_length=100)
    content = models.TextField()
    description = models.CharField(max_length=200)

    category = models.ForeignKey(
        Category, null=True, blank=True,
        related_name="posts",
        on_delete=models.SET_NULL
    )

    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default="draft")
    published_at = models.DateTimeField(null=True, blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def publish(self):
        self.status = "published"
        if not self.published_at:
            self.published_at = timezone.now()
        self.save(update_fields=["status", "published_at"])

    def __str__(self):
        return self.title

    @admin.display(
        boolean=True,
        ordering="created_at",
        description="Published Recently?",
    )

    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=7) <= self.created_at <= now




