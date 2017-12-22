from django.contrib import admin
from .models import User, Problem, Level

admin.site.register(User)
admin.site.register(Level)
admin.site.register(Problem)


