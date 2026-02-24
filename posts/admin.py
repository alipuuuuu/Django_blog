from django.contrib import admin
from django.utils.html import format_html
from .models import Post


class PostAdmin(admin.ModelAdmin):

    readonly_fields = ("time_info",)

    fieldsets = [
        (None, {'fields': ['title', 'description', 'category', 'status', 'time_info', ]}),
        ("Content", {'fields': ['content'], "classes": ["collapse"]}),
    ]

    def time_info(self, obj):
        if not obj.pk:
            return "Not saved yet"
        return format_html(
            "<span style='color:#666;font-size:12px;'>"
            "Created: {} | Updated: {}"
            "</span>",
            obj.created_at.strftime("%Y-%m-%d %H:%M"),
            obj.updated_at.strftime("%Y-%m-%d %H:%M"),
        )

    time_info.short_description = " time "

    list_filter = ["created_at", "updated_at"]
    list_display = ('title', 'created_at', 'updated_at', 'status', 'was_published_recently')
    search_fields = ['title', 'content']

admin.site.register(Post, PostAdmin)