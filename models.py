from tortoise.models import Model
from tortoise.fields import IntField,CharField
from tortoise import fields

class Publish(Model):
    name = fields.CharField(max_length=120,verbose_name="出版社名称")
    email = fields.CharField(max_length=120,verbose_name="出版社邮箱")

class Author(Model):
    name = fields.CharField(max_length=120,verbose_name="作者")
    age = fields.IntField(verbose_name="年龄")

class Book(Model):
    title = fields.CharField(max_length=120,verbose_name="书名")
    price = fields.IntField(verbose_name="价格")
    img_url= fields.CharField(max_length=250,null=True,verbose_name="")
    bread = fields.IntField(verbose_name="阅读量")
    bcomment = fields.IntField(verbose_name="评论数")
    publishs = fields.ForeignKeyField('models.Publish',related_name='books')
    authors = fields.ManyToManyField('models.Author',related_name='books',description="作者")