from django.views.generic import ListView
from apps.categories.models import FishCategory


class FishCategoryListView(ListView):
    model = FishCategory
    template_name = ''

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        return context
