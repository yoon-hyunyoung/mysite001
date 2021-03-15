from django.contrib import admin

from .models import Kleague2_2021_1r,Kleague2_2021_2r,Kleague1_2021_2r,Kleague1_2021_1r,Kleague1_2021_3r

# admin.site.register(Kleague1_2021_1r)
# admin.site.register(Kleague2_2021_1r) 
# admin.site.register(Kleague1_2021_2r)
# admin.site.register(Kleague2_2021_2r)
# admin.site.register(Kleague1_2021_3r)

@admin.register(Kleague1_2021_1r)
class Kleague1_2021_1rAdmin(admin.ModelAdmin):
    pass

@admin.register(Kleague1_2021_2r)
class Kleague1_2021_2rAdmin(admin.ModelAdmin):
    pass

@admin.register(Kleague1_2021_3r)
class Kleague1_2021_3rAdmin(admin.ModelAdmin):
    pass

@admin.register(Kleague2_2021_1r)
class Kleague2_2021_1rAdmin(admin.ModelAdmin):
    pass
@admin.register(Kleague2_2021_2r)
class Kleague2_2021_2rAdmin(admin.ModelAdmin):
    pass