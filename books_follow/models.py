from django.db import models


class BookFollow(models.Model):
    copy = models.ForeignKey(
        "copies.Copy", on_delete=models.CASCADE, related_name="follow"
    )
    user = models.ForeignKey(
        "users.User", on_delete=models.CASCADE, related_name="follow"
    )
