from django.db import models
from django.utils import timezone


class Book_loans(models.Model):
    STATUS_CHOICES = [
        ("Not Returned","Not Returned"),
        ("Returned", "Returned")
    ]

    started_at = models.DateTimeField(auto_now_add=True)
    finished_at = models.DateTimeField(blank=True, null=True)
    status = models.CharField(
        max_length=15,choices=STATUS_CHOICES,default="Not Returned"
    )
    user = models.ForeignKey("users.User", on_delete=models.CASCADE)
    copie = models.ForeignKey("copies.Copies", on_delete=models.CASCADE)

    def edit_finished_at(self):
        self.finished_at = timezone.now()
        self.save()

    def __str__(self) -> str:
        return f"<following {self.id} = {self.user_id}]>"

class Copies(models.Model):
    is_avaible = models.BooleanField()
    last_loan = models.DateTimeField(auto_now_add=True)
    book = models.ForeignKey("books.Book", on_delete=models.CASCADE, related_name="copies")

    def __str__(self) -> str:
        return f"<Copie {self.id} = {self.is_avaible}]>"