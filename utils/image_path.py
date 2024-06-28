def fish_upload(instance, filename):
    return f'fish_images/{instance.fish.id}/{filename}'


def accessories(instance, filename):
    return f'accessor_images/{instance.id}/{filename}'


def fish_food_images(instance, filename):
    return f'ffood_images/{instance.id}/{filename}'
