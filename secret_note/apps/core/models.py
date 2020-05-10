import uuid
from django.db import models

class AppConfig(models.Model):
    session_name = models.CharField(
        max_length=255,
        default=None,
        null=True,
        blank=False
    )

    api_id = models.PositiveIntegerField(
        default=None,
        null=True,
        blank=False,
        help_text='getting from https://my.telegram.org/auth'
    )

    api_hash = models.CharField(
        max_length=255,
        default=None,
        null=True,
        blank=False,
        help_text='getting from https://my.telegram.org/auth'
    )

    is_active = models.BooleanField(
        default=False,
        null=True,
        blank=True,
        help_text='non active config is not working'
    )

    is_bot = models.BooleanField(
        default=None,
        null=True,
        blank=True,
        help_text='select if you want to use bot account for this config'
    )

    bot_token = models.CharField(
        max_length=255,
        default=None,
        null=True,
        blank=True,
        help_text='Required if you use a bot account'
    )

    timestamp = models.DateTimeField(
        auto_now=True
    )

class Message(models.Model):
    text = models.TextField(
        default=None,
        null=True,
        blank=False
    )

    access_token = models.CharField(
        max_length=255,
        default=None,
        null=True,
        blank=True
    )

    is_viewed = models.BooleanField(
        default=False,
        null=True,
        blank=True
    )

    is_empty = models.BooleanField(
        default=True,
        null=True,
        blank=True
    )

    timestamp = models.DateTimeField(
        auto_now=True
    )

    def __str__(self):
        return "ID: {0}, Is viewed: {1}".format(self.id, self.is_viewed)

    def save(self, *args, **kwargs):
        if not self.access_token:
            self.access_token = "{0}:{1}".format(uuid.uuid1().hex, uuid.uuid4().hex)

        if self.text and self.text != '':
            self.is_empty = False

        if self.is_viewed:
            return self.delete()

        return super(Message, self).save(*args, **kwargs)

    class Meta:
        verbose_name = 'message'
        verbose_name_plural = 'messages'

