from django.db import models


class Book(models.Model):
    title = models.CharField(max_length=255, null=False)
    author = models.CharField(max_length=255, null=False)
    description = models.CharField(max_length=255, null=True)
    publisher = models.CharField(max_length=255, null=False)
    published_at = models.DateTimeField(auto_now_add=True)
    copies = models.IntegerField(null=False, default=0)

    user = models.ForeignKey(
        "users.User", on_delete=models.PROTECT, related_name="book"
    )
