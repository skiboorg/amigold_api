from django.contrib import admin
from .models import *

from .models import *
from nested_inline.admin import NestedStackedInline, NestedModelAdmin


class ItemInline(NestedStackedInline):
    model = OrderItem
    extra = 0

class OrderAdmin(NestedModelAdmin):
    model = Order
    inlines = [ItemInline]


admin.site.register(Order, OrderAdmin)
