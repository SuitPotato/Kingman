from django.contrib import admin
from mainpage.models import Department, Utility, Important, Education, Restaurant, Attraction, LodgeCampRV

# Register your models here.
admin.site.register(Department)
admin.site.register(Utility)
admin.site.register(Important)
admin.site.register(Education)
admin.site.register(Restaurant)
admin.site.register(Attraction)
admin.site.register(LodgeCampRV)