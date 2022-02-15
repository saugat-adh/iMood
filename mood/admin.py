from django.contrib import admin
from .models import Mood, ReasonsTag, FeelingsTag

# Register your models here.


admin.site.register(Mood)
admin.site.register(ReasonsTag)
admin.site.register(FeelingsTag)

