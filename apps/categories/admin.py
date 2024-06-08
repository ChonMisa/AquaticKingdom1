from django.contrib import admin
from mptt.admin import DraggableMPTTAdmin

from apps.categories.models import FishCategory


admin.site.register(
    FishCategory,
    DraggableMPTTAdmin,
    list_display=(
        'tree_actions',
        'indented_title',
    ),
    list_display_links=(
        'indented_title',
    ),
)
