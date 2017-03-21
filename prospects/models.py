from __future__ import unicode_literals
from django.db import models

class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.question_text

    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text

class Chance(models.Model):
    Company_Name = models.CharField(max_length=200)
    Company_Location = models.CharField(max_length=200)
    Last_Contact_Date = models.DateTimeField('last contact')
    Contact_Name = models.CharField(max_length=200)
    Contact_Email = models.EmailField(max_length=200)
    Contact_PhoneNumber= models.CharField(max_length=12)
    Job_Keywords = models.CharField(max_length=200)

    def __str__(self):
        return self.Company_Name


