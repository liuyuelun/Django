from django.db import models

# Create your models here.
class Book(models.Model):
    title = models.CharField("书名",max_length=50,default='',unique=True)
    pub = models.CharField('出版社',max_length=100,default='')
    price = models.DecimalField("价格",max_digits=7,decimal_places=2)
    info = models.CharField("描述",max_length=100,default='')
    market_price = models.DecimalField("零售价",max_digits=7,decimal_places=2,default=0.0)
    class Meta:
        db_table = 'book'
    def __str__(self):
        return "%s_%s_%s_%s"%(self.title,self.pub,self.price,self.market_price)
class Author(models.Model):
    name = models.CharField('姓名',max_length=11,unique=True)
    age = models.IntegerField('年龄',default=1)
    email = models.EmailField('邮箱',max_length=50,null=True)
    class Meta:
        db_table = 'author'

