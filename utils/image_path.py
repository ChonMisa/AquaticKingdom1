def fish_upload(instance, filename):
    return f'fish_images/{instance.fish.id}/{filename}'


def accessories(instance, filename):
    return f'accessor_images/{instance.accessory.id}/{filename}'


def upload_avatar_for_user(instance, filename):
    return f'upload_avatar_for_user/{instance.avatar.id}/{filename}'


def fish_food_images(instance, filename):
    return f'ffood_images/{instance.ffood.id}/{filename}'
