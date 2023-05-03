from django.db import models


class Book_loans(models.Model):
    started_at = models.DateTimeField(auto_now_add=True)
    finished_at = models.DateTimeField()
    status = models.TextField()
    user = models.ForeignKey("users.User", on_delete=models.CASCADE)
    copie = models.ForeignKey("copies.Copies", on_delete=models.CASCADE)

    def __str__(self) -> str:
        return f"<following {self.id} = {self.user_id}]>"

class Copies(models.Model):
    is_avaible = models.BooleanField()
    last_loan = models.DateTimeField(auto_now_add=True)
    book = models.ForeignKey("books.Book", on_delete=models.CASCADE)

    def __str__(self) -> str:
        return f"<Copie {self.id} = {self.is_avaible}]>"