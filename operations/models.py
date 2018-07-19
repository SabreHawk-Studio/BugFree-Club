from datetime import datetime

from django.db import models

from users.models import UserProfile
from courses.models import Course,Lesson


class CourseUserAsk(models.Model):
    name = models.CharField(max_length=20, verbose_name='姓名')
    course_name = models.CharField(max_length=50, verbose_name='课程名')
    add_time = models.DateTimeField(default=datetime.now, verbose_name='添加时间')

    class Meta:
        verbose_name = '用户咨询'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class CourseComments(models.Model):
    # 课程评论
    user = models.ForeignKey(UserProfile, verbose_name='用户',on_delete=models.CASCADE)
    course = models.ForeignKey(Course, verbose_name='课程',on_delete=models.CASCADE)
    comments = models.CharField(max_length=200, verbose_name='评论')
    add_time = models.DateTimeField(default=datetime.now, verbose_name='评论添加时间')

    class Meta:
        verbose_name = '课程评论'
        verbose_name_plural = verbose_name

    def __str__(self):
        return '用户:%s 课程:%s' % (self.user, self.course)


class UserFavourite(models.Model):
    user = models.ForeignKey(UserProfile, verbose_name='用户',on_delete=models.CASCADE)
    fav_id = models.IntegerField(default=0, verbose_name='数据id')
    fav_type = models.IntegerField(choices=((1, '课程'), (2, '负责人')),default=0, verbose_name='收藏类型')
    add_time = models.DateTimeField(default=datetime.now, verbose_name='评论添加时间')

    class Meta:
        verbose_name = '用户收藏'
        verbose_name_plural = verbose_name


class UserMessage(models.Model):
    user = models.IntegerField(default=0, verbose_name='接受用户')
    message = models.CharField(max_length=500, verbose_name='消息内容')
    has_read = models.BooleanField(default=False, verbose_name='是否已读')
    add_time = models.DateTimeField(default=datetime.now, verbose_name='评论添加时间')

    class Meta:
        verbose_name = '用户消息'
        verbose_name_plural = verbose_name

    def __str__(self):
        return '%s: %s' % (self.user, self.message)

    def to_read(self):
        self.has_read = True
        self.save()


class UserCourse(models.Model):
    user = models.ForeignKey(UserProfile, verbose_name='用户',on_delete=models.CASCADE)
    course = models.ForeignKey(Course, verbose_name='课程',on_delete=models.CASCADE)
    add_time = models.DateTimeField(default=datetime.now, verbose_name='添加时间')

    class Meta:
        ordering = ['-add_time']
        verbose_name = '用户课程'
        verbose_name_plural = verbose_name

    def __str__(self):
        return '%s: %s' % (self.user, self.course)


class UserLesson(models.Model):
    user = models.ForeignKey(UserProfile, verbose_name='用户',on_delete=models.CASCADE)
    lesson = models.ForeignKey(Lesson, verbose_name='章节',on_delete=models.CASCADE)
    add_time = models.DateTimeField(default=datetime.now, verbose_name='添加时间')

    class Meta:
        ordering = ['-add_time']
        verbose_name = '用户章节'
        verbose_name_plural = verbose_name

    def __str__(self):
        return '%s: %s' % (self.user, self.lesson)