from django.db import models

MAX_LENGTH_USER_NAME = 100
MAX_LENGTH_STATUS_NAME = 50
MAX_LENGTH_CATEGORY_TITLE = 50


class User(models.Model):
    name = models.CharField('Имя', max_length=MAX_LENGTH_USER_NAME)
    email = models.EmailField('Email', unique=True)

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'

    def __str__(self):
        return f'User: {self.name}'


class UserProfile(models.Model):
    bio = models.TextField('О себе', blank=True)
    birth_date = models.DateField('Дата рождения', blank=True, null=True)
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        related_name='profile',
        verbose_name='Пользователь'
    )

    class Meta:
        verbose_name = 'Профиль пользователя'
        verbose_name_plural = 'Профили пользователей'

    def __str__(self):
        return f'Profile of {self.user}'


class Status(models.Model):
    name = models.CharField('Название', max_length=MAX_LENGTH_STATUS_NAME)
    is_final = models.BooleanField('Финальный', default=False)

    class Meta:
        verbose_name = 'Статус'
        verbose_name_plural = 'Статусы'

    def __str__(self):
        return self.name


class Category(models.Model):
    title = models.CharField('Заголовок', max_length=MAX_LENGTH_CATEGORY_TITLE)
    description = models.TextField('Описание', blank=True)

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.title


class Note(models.Model):
    text = models.TextField('Текст')
    created_at = models.DateTimeField('Дата создания', auto_now_add=True)
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='notes',
        verbose_name='Автор'
    )
    status = models.ForeignKey(
        Status,
        on_delete=models.SET_NULL,
        null=True,
        related_name='notes',
        verbose_name='Статус'
    )
    category = models.ManyToManyField(
        Category,
        related_name='notes',
        blank=True,
        verbose_name='Категории'
    )

    class Meta:
        verbose_name = 'Заметка'
        verbose_name_plural = 'Заметки'

    def __str__(self):
        return self.text[:20] + '...'
