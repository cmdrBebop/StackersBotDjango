from django.contrib import admin

from .forms import *
from .models import *



@admin.register(User)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('tg_id', 'first_name', 'second_name', 'telegram_username')
    list_display_links = ('tg_id', 'first_name', 'second_name')
    search_fields = ('tg_id', 'first_name', 'second_name', 'telegram_username')
    form = UserForm


@admin.register(Subscribe)
class SubscribeAdmin(admin.ModelAdmin):
    list_display = ('user', 'hackathon_subscribe', 'lecture_subscribe', 'meet_up_subscribe', 'vacancy_subscribe')
    list_display_links = ('user', 'hackathon_subscribe', 'lecture_subscribe', 'meet_up_subscribe', 'vacancy_subscribe')
    list_filter = ('hackathon_subscribe', 'lecture_subscribe', 'meet_up_subscribe', 'vacancy_subscribe')
    form = SubscribeForm

@admin.register(EventType)
class EventTypeAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')
    list_display_links = ('id', 'title')
    form = EventTypeForm

@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'event_date', 'type_of_event', 'post_about_event')
    list_display_links = ('id', 'title', 'event_date', 'type_of_event', 'post_about_event')
    form = EventForm

@admin.register(UserEvent)
class UserEventAdmin(admin.ModelAdmin):
    list_display = ('user', 'event')
    list_display_links = ('user', 'event')
    form = UserEventForm

@admin.register(Stack)
class StackAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')
    list_display_links = ('id', 'title')
    form = StackForm


@admin.register(UserStack)
class UserStackAdmin(admin.ModelAdmin):
    list_display = ('user',)
    list_display_links = ('user',)
    filter_horizontal = ['stack']
    form = UserStackForm

@admin.register(EventStack)
class EventStackAdmin(admin.ModelAdmin):
    list_display = ('event',)
    list_display_links = ('event',)
    list_filter = ('stack',)
    filter_horizontal = ['stack']
    form = EventStackForm

@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    list_display = ('id', 'profile', 'text', 'created_at')
    list_display_links = ('id', 'profile', 'text', 'created_at')

