from django.db import models


class Copy(models.Model):
    book_title = models.CharField(max_length=255, null=False)
    active_loan = models.BooleanField(default=False)

    book = models.ForeignKey(
        "books.Book", on_delete=models.CASCADE, related_name="copy"
    )
