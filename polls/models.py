import datetime

from django.db import models
from django.utils import timezone

# Each model in Django is represented as a class which is
# a subclass of django.db.models.Model class.


class Question(models.Model):
    # Use class variable to represent database field in the model
    question_text = models.CharField(max_length=200)

    # Use optional first positional argument to a Field to
    # designate a human-readable name instead of using machine-friendly name
    pub_date = models.DateTimeField('date published')

    def was_recently_published(self):
        now = timezone.now()
        return now >= self.pub_date >= now - datetime.timedelta(days=1)

    def __str__(self):
        return self.question_text


class Choice(models.Model):
    # Relationship is defined using ForeignKey. Here, each choice is
    # related to a single question. Supported relations are: 1-1 1-m n-m
    question = models.ForeignKey(Question, on_delete=models.CASCADE)

    # max_length argument is required for CharField
    choice_text = models.CharField(max_length=200)

    # and a default value
    votes = models.IntegerField(default=0)

    # and many other options

    def __str__(self):
        # Better way to represent the model when using
        # interactive shell commands. This representation
        # is also used throughout Django's automatically
        # generated admin.
        return self.choice_text
