from django.contrib import admin
from message_board.models import Post


class PostAdmin(admin.ModelAdmin):
    pass
    
admin.site.register(Post, PostAdmin)
