from django.db import models
from django.db.models.signals import post_delete, pre_save
from django.dispatch import receiver
import os

# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=200)
    summary = models.CharField(max_length=300, blank=True)
    content = models.TextField()
    published_at = models.DateTimeField(auto_now_add=True)
    thumbnail = models.ImageField(upload_to="images/", blank=True, null=True)

    def __str__(self):
        return self.title
    
@receiver(post_delete, sender=Article)
def delete_article_thumbnail(sender, instance, **kwargs):
    if instance.thumbnail:
        if os.path.isfile(instance.thumbnail.path):
            os.remove(instance.thumbnail.path)

@receiver(pre_save, sender=Article)
def update_article_thumbnail(sender, instance, **kwargs):
    if not instance.pk:
        return # New article, no old image to check

    try:
        old_article = Article.objects.get(pk=instance.pk)
    except Article.DoesNotExist:
        return

    old_thumbnail = old_article.thumbnail
    new_thumbnail = instance.thumbnail

    if old_thumbnail and old_thumbnail != new_thumbnail:
        if os.path.isfile(old_thumbnail.path):
            os.remove(old_thumbnail.path)
    
    if os.path.isfile(old_thumbnail.path):
        os.remove(old_thumbnail.path)
