import uuid
from django.db import models


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

