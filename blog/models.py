from django.db import models

class Blog(models.Model):
    title = models.CharField(max_length=200) #문자열 데이터를 타이틀을 나타냄
    pub_date  = models.DateTimeField('date published') #날짜 및 시간
    body = models.TextField()  #문자열

    def __str__(self):
        return self.title 

    def numlimit(self):
        return self.body[:100] #body의 글자수를 100개를 상한선으로 리턴
# Create your models here.
