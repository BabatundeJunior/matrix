# from django.contrib.auth.models import User
# from django.db import models
#
# from core.models import Course
#
#
# # Create your models here.
#
# class UserProfile(models.Model):
#     user = models.OneToOneField(User, on_delete=models.CASCADE)
#     is_instructor = models.BooleanField(default=False)
#     is_premium = models.BooleanField(default=False)
#     bio = models.TextField(blank=True)
#     profile_picture = models.ImageField(upload_to='profile_pics/', blank=True)
#
#     def __str__(self):
#         return self.user.username
#
#
# # class Enrollment(models.Model):
# #     user = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name='enrollments')
# #     course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='enrollments')
# #     date_enrolled = models.DateTimeField(auto_now_add=True)
# #
# #     class Meta:
# #         unique_together = ('user', 'course')
# #
# #     def __str__(self):
# #         return f"{self.user.user.username} enrolled in {self.course.title}"
# #
# #
# # class Progress(models.Model):
# #     from core.models import Lesson
# #     user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
# #     lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE)
# #     completed = models.BooleanField(default=False)
# #     date_completed = models.DateTimeField(blank=True, null=True)
# #
# #     def __str__(self):
# #         return f"{self.user.user.username} - {self.lesson.title} progress"
#
#
# class Subscription(models.Model):
#     user = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name='subscriptions')
#     start_date = models.DateTimeField(auto_now_add=True)
#     end_date = models.DateTimeField(null=True, blank=True)  # if offering time-limited subscriptions
#
#     def __str__(self):
#         return f"{self.user.user.username} - Subscription"
#
#
