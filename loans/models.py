from django.db import models


class Loan(models.Model):
    return_date = models.DateTimeField()

    copy = models.ForeignKey(
        "copies.Copy", on_delete=models.CASCADE, related_name="loan"
    )
    user = models.ForeignKey(
        "users.User", on_delete=models.CASCADE, related_name="loan"
    )
