from django.db import models


class Post(models.Model):
    post_title = models.CharField(blank=True, max_length=100)
    post_description = models.TextField(max_length=400)
    post_image = models.FileField(upload_to='img/')
    post_date = models.DateField(null=True, auto_now_add="True")

    def __str__(self):
        return self.post_title

    class Meta:
        verbose_name = 'Пост'
        verbose_name_plural = 'Посты'


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    author_name = models.CharField(blank=True, max_length=50)
    text = models.TextField(max_length=200)

    def __str__(self):
        return self.author_name

    class Meta:
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Коментарии'


class All_goods(models.Model):        # Таблица со всеми вущами
    title = models.CharField(max_length=50)
    category = models.CharField(max_length=10)
    description = models.TextField()
    price = models.IntegerField()
    date = models.DateField(auto_now_add="True")
    photo = models.ImageField(upload_to='img/')    # разобраться
    author = models.CharField(max_length=50)  # из таблицы с логинами

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'


# class Man_goods(models.Model):      # Таблица с вещами для мужчин
#     pass
#
#
# class Women_goods(models.Model):      # Таблица с вещами для женщин
#     pass
#
#
# class Child_goods(models.Model):      # Таблица с вещами для детей
#     pass
