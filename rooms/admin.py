from django.contrib import admin
from . import models

# Register your models here.
@admin.register(models.Room)
class RoomAdmin(admin.ModelAdmin):
    """ Room Admin Definition """

    list_display = (
        "name",
        "country",
        "city",
        "price",
        "guests",
        "beds",
        "bedrooms",
        "baths",
        "check_in",
        "check_out",
        "instant_book",
        "count_amenities",
    )

    def count_amenities(self, obj):
        # print(obj.amenities.all())
        return obj.amenities.count()

    count_amenities.short_description = "amenities"

    list_filter = (
        "instant_book",
        "host__superhost",
        "host__gender",
        "room_type",
        "amenities",
        "facilities",
        "house_rules",
        "city",
        "country"
    )
    search_fields = ("=city","^host__username")

    filter_horizontal = (
        "amenities",
        "facilities",
        "house_rules",
    )

    fieldsets = (
        (
            "Basic Info",{"fields": ("name", "description", "country", "address", "price")},
        ),
        (
            "Times",{"fields":("check_in","check_out","instant_book")},
        ),
        (
            "Spaces",{"fields":("guests", "beds", "bedrooms", "baths")}
        ),
        (
            "More About the Spaces",
            {
                "classes":("collapse",),
                "fields":("amenities","facilities","house_rules")
            },
        ),
        (
            "Last Details",{"fields":("host", )},
        )
    )

    ordering =('name', 'price')




@admin.register(models.RoomType, models.Facility, models.Amenity, models.HouseRule)
class ItemAdmin(admin.ModelAdmin):
    pass


@admin.register(models.Photo)
class PhotoAdmin(admin.ModelAdmin):
    """ Photo Admin Definition """
    pass
