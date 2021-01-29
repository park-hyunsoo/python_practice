from django.contrib import admin
from django.utils.html import mark_safe
from . import models

# Register your models here.
class PhotoInline(admin.TabularInline):
    model = models.Photo

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
        "count_photos",
        "total_rating",
    )

    def count_amenities(self, obj):
        # print(obj.amenities.all())
        return obj.amenities.count()

    count_amenities.short_description = "amenities"
    
    def count_photos(self, obj):
        return obj.photos.count()

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
    
    raw_id_fields = ("host",)
    
    filter_horizontal = (
        "amenities",
        "facilities",
        "house_rules",
    )

    inlines = (PhotoInline, )
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

    def save_model(self, request, obj, form, change): 
        obj.user = request.user
        print(obj.user)
        super().save_model(request, obj, form, change)


@admin.register(models.RoomType, models.Facility, models.Amenity, models.HouseRule)
class ItemAdmin(admin.ModelAdmin):
    """ Item Admin Definition """
    list_display=(
        "name",
        "used_by"
    )
    def used_by(self, obj):
        return obj.rooms.count()


@admin.register(models.Photo)
class PhotoAdmin(admin.ModelAdmin):
    """ Photo Admin Definition """
    list_display = ('__str__', 'get_thumbnail')

    def get_thumbnail(self, obj):
        # print(obj.file)
        return mark_safe(f'<img width="50px" src="{obj.file.url}" />')

    get_thumbnail.short_description = "Thumbnail"