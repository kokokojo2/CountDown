from django.contrib.auth import get_user_model


def create_countdown(form, user=None):
    """
    Creates new countdown object and and saves it to db.
    :param form: instance of CountdownForm
    :param user: user from request, default is None
    :return: countdown object if created successfully else None
    """

    if form.is_valid():
        countdown = form.save(commit=False)
        if isinstance(user, get_user_model()):
            countdown.user = user
        countdown.save()

        return countdown
