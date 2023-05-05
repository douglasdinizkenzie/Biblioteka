from django.db import models

class StatusChoices(models.TextChoices):
    BORROWED = 'Borrowed'
    RETURNED = 'Returned'
    DELAYED = 'Delayed'


class Book_loans(models.Model):
    started_at = models.DateTimeField(auto_now_add=True)
    finished_at = models.DateTimeField(null=True)
    status = models.CharField(
        max_length=10,
        choices=StatusChoices.choices,
        default=StatusChoices.BORROWED
    )
    user = models.ForeignKey("users.User", on_delete=models.CASCADE)
    copy = models.ForeignKey("copies.Copy", on_delete=models.CASCADE)

    def __str__(self) -> str:
        return f"<following {self.id} = {self.user_id}]>"


class Copy(models.Model):
    is_available = models.BooleanField(null=True, default=True)
    last_loan = models.DateTimeField(null=True)
    book = models.ForeignKey(
        "books.Book", on_delete=models.CASCADE, related_name="copies"
    )

    def __str__(self) -> str:
        return f"<Copy {self.id} = {self.is_available}]>"
