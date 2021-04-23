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


def get_reaction_counters_dict(countdown_obj):
    """
    Gets an amount of user reaction of each type.
    :param countdown_obj: instance of Countdown
    :return: dict in a format {"*type_of_reaction*_number": int}
    """

    likes_number = countdown_obj.reactionset_set.filter(like=True).count()
    dislikes_number = countdown_obj.reactionset_set.filter(dislike=True).count()
    laugh_number = countdown_obj.reactionset_set.filter(laugh=True).count()
    cry_number = countdown_obj.reactionset_set.filter(cry=True).count()

    return {'likes_number': likes_number,
            'dislikes_number': dislikes_number,
            'laugh_number': laugh_number,
            'cry_number': cry_number}
