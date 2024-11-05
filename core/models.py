# from django.db import models
#
#
# # Create your models here.
#
# class Course(models.Model):
#     from authentication.models import UserProfile
#     title = models.CharField(max_length=255)
#     description = models.TextField()
#     instructor = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name='courses')
#     date_created = models.DateTimeField(auto_now_add=True)
#     access_level = models.CharField(max_length=20, choices=[('free', 'Free'), ('premium', 'Premium')], default='free')
#
#     def __str__(self):
#         return self.title
#
#
# class Module(models.Model):
#     course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='modules')
#     title = models.CharField(max_length=255)
#     description = models.TextField()
#     order = models.PositiveIntegerField()
#
#     class Meta:
#         ordering = ['order']
#
#     def __str__(self):
#         return f"{self.course.title} - {self.title}"
#
#
# class Lesson(models.Model):
#     module = models.ForeignKey(Module, on_delete=models.CASCADE, related_name='lessons')
#     title = models.CharField(max_length=255)
#     # videos = models
#     content = models.TextField()
#     order = models.PositiveIntegerField()
#
#     class Meta:
#         ordering = ['order']
#
#     def __str__(self):
#         return f"{self.module.title} - {self.title}"
#
#
# class Quiz(models.Model):
#     module = models.ForeignKey(Module, on_delete=models.CASCADE, related_name='quizzes')
#     title = models.CharField(max_length=255)
#     description = models.TextField(blank=True, null=True)
#
#     def __str__(self):
#         return f"{self.module.title} - Quiz: {self.title}"
#
#
# class Question(models.Model):
#     quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE, related_name='questions')
#     text = models.CharField(max_length=500)
#
#     def __str__(self):
#         return self.text
#
# class Choice(models.Model):
#     question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name='choices')
#     text = models.CharField(max_length=255)
#     is_correct = models.BooleanField(default=False)
#
#     def __str__(self):
#         return self.text
