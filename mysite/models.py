from django.db import models


class CreateUser(models.Model):
    Email = models.EmailField(max_length=100, default='')
    First_name = models.CharField(max_length=100, default='')
    Last_name = models.CharField(max_length=100, default='')
    Password = models.CharField(max_length=100, default='')
    Confirm_password = models.CharField(max_length=100, default='')

    def __str__(self):
        return  self.First_name

class Courses(models.Model):
    class Meta:
        verbose_name = 'Add Courses'
        verbose_name_plural = 'Add Courses'

    MICROSOFT = 'MOS'
    GRAPHIC = 'GD'
    SOUND = 'SM'
    WEBSITE = 'WD'
    ANIMATION = 'AP'
    VIDEO = 'VE'

    course_thumbnil_Image = models.ImageField()
    course_title = models.TextField()
    course_detail = models.TextField()
    course_author_image = models.ImageField()
    course_author_name = models.TextField()
    course_date = models.TextField()
    course_duration = models.TextField()
    COURSE_CATEGORY_CHOICES = (
        (MICROSOFT, 'Microsoft Office Suite'),
        (GRAPHIC, 'Graphic Design'),
        (SOUND, 'Sound & Music'),
        (WEBSITE, 'Web Site Development'),
        (ANIMATION, 'Animation Production'),
        (VIDEO, 'Video Editing'),
    )
    course_category = models.CharField(max_length=5,
                                      choices=COURSE_CATEGORY_CHOICES,
                                      default=MICROSOFT)

    def __str__(self):
        return self.course_title

class CoursesTopic(models.Model):

    class Meta:
        verbose_name = 'Course Topics'
        verbose_name_plural = 'Course Topics'

    BLUE = 'colorBlue mt-4'
    GREEN = 'colorGreen mt-4'
    PARPUL = 'colorparpup mt-4'
    ORANGE = 'colorOrange mt-4'
    PINK = 'colorpink mt-4'
    BROWN = 'colorbrown mt-4'

    course_thumbnil_Image = models.ImageField()
    course_title = models.TextField()
    course_detail = models.TextField()
    COLOR_CATEGORY_CHOICES = (
        (BLUE, 'BLUE'),
        (GREEN, 'GREEN'),
        (PARPUL, 'PARPUL'),
        (ORANGE, 'ORANGE'),
        (PINK, 'PINK'),
        (BROWN, 'BROWN'),
    )
    background_color = models.CharField(max_length=30,
                                       choices=COLOR_CATEGORY_CHOICES,
                                       default=BLUE)


    def __str__(self):
        return self.course_title