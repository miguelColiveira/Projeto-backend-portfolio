from rest_framework.generics import ListAPIView, CreateAPIView
from books_follow.models import BookFollow
from copies.models import Copy
from users.models import User
from books.models import Book
from books_follow.serializers import BookFollowSerializer

from rest_framework_simplejwt.authentication import JWTAuthentication
from django.core.mail import send_mail
from django.conf import settings

from django.shortcuts import get_object_or_404


class BookFollowView(ListAPIView):
    authentication_classes = [JWTAuthentication]

    queryset = BookFollow.objects.all()
    serializer_class = BookFollowSerializer


class BookFollowViewCreate(CreateAPIView):
    authentication_classes = [JWTAuthentication]

    queryset = BookFollow
    serializer_class = BookFollowSerializer

    def perform_create(self, serializer):
        copy_id = self.kwargs["copy_id"]
        copy = Copy.objects.get(id=copy_id)

        idBook = copy.book_id
        book = get_object_or_404(Book, id=idBook)

        username = self.request.user
        user = get_object_or_404(User, username=username)

        if copy.active_loan:
            message_sendEmail = (
                f"Livro {book.title} - não esta disponível, aguarde retorno."
            )

        subjectstr = "O livro foi adicionado em favoritos!"
        recipient_liststr = [user.email]
        messagestr = message_sendEmail

        send_mail(
            subject=subjectstr,
            recipient_list=recipient_liststr,
            message=messagestr,
            from_email=settings.EMAIL_HOST_USER,
            fail_silently=False,
        )

        serializer.save(user=self.request.user, copy=copy)
