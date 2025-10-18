from django.db import models
# Create your models here.


class Artiles(models.Model):
    objects = None
    title = models.CharField('Название', max_length=50)
    anons = models.CharField('Анонс', max_length=250)
    full_text = models.TextField('Описание')
    date = models.DateTimeField('Дата публикации', blank=True, null=True)
    image = models.ImageField(upload_to='.media/images/', null=True, blank=True)



    def __str__(self):
        return self.title


    def get_absolute_url(self):
        return f'/news/{self.id}'



    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'


from django.contrib.auth.models import User

class Comment(models.Model):
    objects = None
    article = models.ForeignKey(Artiles, on_delete=models.CASCADE, related_name='comments')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField('Комментарий')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Комментарий от {self.user.username} к "{self.article.title}"'
