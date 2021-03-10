from django.contrib import admin

from apps.landing.models import Content, Logo, AboutUs, AboutUsImage


admin.site.register(Logo)
admin.site.register(Content)
admin.site.register(AboutUs)
admin.site.register(AboutUsImage)
