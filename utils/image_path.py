def fish_upload(instance, filename):
<<<<<<< HEAD
    return f'fish_images/{instance.fish.id}/{filename}'
=======
    return f'fish_images/{instance.id}/{filename}'
>>>>>>> d854b8553a1d6d01877f1613f9982a030fae1c77


def accessories(instance, filename):
    return f'accessor_images/{instance.id}/{filename}'


def upload_avatar_for_user(instance, filename):
    return f'upload_avatar_for_user/{instance.id}/{filename}'


def fish_food_images(instance, filename):
    return f'ffood_images/{instance.id}/{filename}'
