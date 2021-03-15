from django.db import models

class Topic(models.Model):
    top_name = models.CharField(max_length = 265, unique=True)

    def __str__(self):
        return self.top_name
# topic,name, url
class Webpage(models.Model):
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    name = models.CharField(max_length=265,unique=True)
    url = models.URLField(unique=True)

    def __str__(self):
        return self.name
# name,date
class AccessRecord(models.Mode):
    name = models.ForeignKey(Webpage, on_delete=models.CASCADE)
    date = models.DateField()

    def __str__(self):
        return str(self.date)
