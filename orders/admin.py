from django.contrib import admin
from . import models

admin.site.register([models.Order, models.Pizza, models.Customer])
