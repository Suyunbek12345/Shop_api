from django.core.mail import send_mail


def send_confirmation_email(user, code):
    full_link = f'http://localhost:8000/api/v1/accounts/activate/{code}/'
    send_mail(
        'Здравствуйте активируйте ваш аккаунт!',
        f'Чтобы активировать ваш аккаунт нужно перейти по ссылке: {full_link}',
        'pp8286500@gmail.com',
        [user],
        fail_silently=False

    )

def send_notification(user, order_id, price):
    email = user.email
    send_mail(
        'Уведомление о создании заказа!',
        f'''Вы создали заказ №{order_id}, ожидайте звонка!\nПолная стоимость вашего заказа {price}.\nСпасибо за то что  выбрали нас!''',
        'from@example.com''',
        [email],
        fail_silently=False,

    )

def send_code_password_rest(user):
    code = user.activation_code
    email = user.email
    send_mail(
        'Письмо с кодом для сброса пароля!',
        f'Ваш код для того чтобы восстановить пароль: {code}\n Никому не передавайте этот код!'
        'from@example.com',
        [email,],
        fail_silently=False
    )
