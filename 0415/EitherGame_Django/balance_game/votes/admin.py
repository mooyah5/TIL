from django.contrib import admin
from .models import Vote, Comment
# Register your models here.
class VoteAdmin(admin.ModelAdmin):
    list_display = ('pk', 'title', 'Issue_a', 'Issue_b',)

admin.site.register(Vote, VoteAdmin)
admin.site.register(Comment)