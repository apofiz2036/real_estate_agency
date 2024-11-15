from django.contrib import admin

from .models import Flat, Complaints, Owner


class OwnerInLine(admin.TabularInline):
    model = Owner.flats.through
    raw_id_fields = ('owner',)
    fields = ('owner',)


@admin.register(Flat)
class FlatAdmin(admin.ModelAdmin):
    search_fields = ['town', 'address']
    readonly_fields = ['created_at']
    list_display = ('address', 'price', 'new_building', 'construction_year')
    list_editable = ['new_building']
    list_filter = ('new_building', 'rooms_number', 'has_balcony')
    raw_id_fields = ('likes',)
    inlines = [OwnerInLine,]


@admin.register(Complaints)
class ComplaintsAdmin(admin.ModelAdmin):
    raw_id_fields = ('address',)


@admin.register(Owner)
class OwnerAdmin(admin.ModelAdmin):
    list_display = ('owner', 'phone_number', 'pure_phone')
    raw_id_fields = ('flats',)
