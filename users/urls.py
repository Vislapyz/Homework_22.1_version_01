from django.contrib.auth.views import LoginView, LogoutView, PasswordChangeDoneView, PasswordResetView, \
    PasswordResetDoneView, PasswordResetConfirmView, PasswordResetCompleteView
from django.urls import path, reverse_lazy

from blog import views
from users.apps import UsersConfig
from users.views import UserCreateView, email_verification, UserUpdateView

app_name = UsersConfig.name

urlpatterns = [
    path("login/", LoginView.as_view(template_name="users/login.html"), name="login"),
    path("logout/", LogoutView.as_view(), name="logout"),
    path("register/", UserCreateView.as_view(), name="register"),
    path("confirm-register/<str:token>/", email_verification, name="confirm_email"),
    path("profile/", UserUpdateView.as_view(), name="profile"),
    path(
        "password-change/", views.UserPasswordChange.as_view(), name="password-change"
    ),

    path(
        "password-change/done/",
        PasswordChangeDoneView.as_view(template_name="users/password_change_done.html"),
        name="password-change-done",
    ),

    path(
        "password-reset/",
        PasswordResetView.as_view(
            template_name="users/password_reset_form.html",
            email_template_name="users/password_reset_email.html",
            success_url=reverse_lazy("users:password_reset_done"),
        ),
        name="password_reset",
    ),
    # Путь для отображения результата отправки письма. Указываем template_name, так как мы переопределяем его
    path(
        "password-reset/done/",
        PasswordResetDoneView.as_view(template_name="users/password_reset_done.html"),
        name="password_reset_done",
    ),

    path(
        "password-reset/<uidb64>/<token>/",
        PasswordResetConfirmView.as_view(
            template_name="users/password_reset_confirm.html",
            success_url=reverse_lazy("users:password_reset_complete"),
        ),
        name="password_reset_confirm",
    ),

    path(
        "password-reset/complete/",
        PasswordResetCompleteView.as_view(
            template_name="users/password_reset_complete.html"
        ),
        name="password_reset_complete",
    ),

]
