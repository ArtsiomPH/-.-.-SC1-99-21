from django.db import models

class User(models.Model):
    login = models.CharField(max_length=30, verbose_name='Логин')
    password = models.CharField(max_length=50, verbose_name='Пароль')
    class Meta:
        verbose_name_plural = 'Пользователи'
        verbose_name = 'Пользователь'
        ordering = ['login']
    def __str__(self):
        return self.login
