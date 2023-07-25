from django.urls import path

from .views import LoanView, LoanDetailView

urlpatterns = [
    path("copy/<copy_id>/loan", LoanView.as_view()),
    path("loans/", LoanDetailView.as_view()),
    # path("books/<book_id>/copy/<pk>", CopyDetailView.as_view()),
]
