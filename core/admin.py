from django.contrib import admin

from .models import Course, Module, Lesson, Quiz, Question, Choice, Enrollment, Progress, Subscription

# Register your models here.

admin.site.register(Course)
admin.site.register(Module)
admin.site.register(Lesson)
admin.site.register(Quiz)
admin.site.register(Question)
admin.site.register(Choice)
admin.site.register(Enrollment)
admin.site.register(Progress)
admin.site.register(Subscription)
