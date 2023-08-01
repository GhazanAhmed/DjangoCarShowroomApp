from django.contrib import admin
from .models import *

# Register your models here.


class StaffAdmin(admin.ModelAdmin):
    list_display = ('name', 'role', 'showroom')
    search_fields = ('name', 'role', 'showroom__name')

class ModelAdmin(admin.ModelAdmin):
    list_display = ('name', 'brand', 'get_engine_number', 'get_features')
    search_fields = ('name', 'brand__name', 'engine__engine_number')

    def get_engine_number(self, obj):
        return obj.engine.engine_number

    get_engine_number.short_description = 'Engine Number'

    def get_features(self, obj):
        return ", ".join([f.name for f in obj.features.all()])

    get_features.short_description = 'Features'

class CarAdmin(admin.ModelAdmin):
    list_display = ('chassis_number', 'model', 'get_brand')
    search_fields = ('chassis_number', 'model__name', 'model__brand__name')

    def get_brand(self, obj):
        return obj.model.brand.name

    get_brand.short_description = 'Brand'

class EngineAdmin(admin.ModelAdmin):
    list_display = ('name', 'specs', 'engine_number')
    search_fields = ('name', 'specs', 'engine_number')

admin.site.register(ShowRoom)
admin.site.register(Staff, StaffAdmin)
admin.site.register(Brand)
admin.site.register(Model, ModelAdmin)
admin.site.register(Engine, EngineAdmin)
admin.site.register(Feature)
admin.site.register(Car, CarAdmin)
