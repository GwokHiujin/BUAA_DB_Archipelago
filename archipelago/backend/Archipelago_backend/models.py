from django.db import models


# Create your models here.
class Image(models.Model):
    img = models.FileField(upload_to='imgs')


class User(models.Model):
    user_id = models.CharField(max_length=255, primary_key=True)
    user_name = models.CharField(max_length=255)
    avatar = models.CharField(max_length=255, null=True)
    password = models.CharField(max_length=255)
    user_type = models.IntegerField()
    bio = models.TextField()


class Musician(models.Model):
    # musician_id = models.IntegerField() id is implicitly defined by django-orm
    user = models.ForeignKey('User', on_delete=models.CASCADE)
    musician_name = models.CharField(max_length=255)
    photo = models.CharField(max_length=255, null=True)
    nationality = models.TextField()
    location = models.TextField(null=True)
    theme = models.TextField(null=True)
    found_year = models.TextField(null=True)
    info = models.TextField(null=True)


class Album(models.Model):
    # album_id = models.IntegerField() id is implicitly defined by django-orm
    musician = models.ForeignKey('Musician', on_delete=models.CASCADE)
    album_name = models.CharField(max_length=255)
    album_price = models.IntegerField()
    album_producer = models.CharField(max_length=255)
    release_year = models.CharField(max_length=255, null=True)
    cover = models.CharField(max_length=255, null=True)
    type = models.IntegerField()
    source = models.CharField(max_length=255, null=True)
    sales_volume = models.IntegerField()


class MusicianMember(models.Model):
    musician = models.ForeignKey('Musician', on_delete=models.CASCADE)
    member_name = models.CharField(max_length=255)
    active_year = models.CharField(max_length=255, null=True)
    birthday = models.CharField(max_length=255, null=True)
    role = models.CharField(max_length=255, null=True)


class Tag(models.Model):
    tag_name = models.CharField(max_length=255)
    tag_type = models.CharField(max_length=255)
    popularity = models.IntegerField()

    class Meta:
        unique_together = ("tag_name", "tag_type")


class MusicianTag(models.Model):
    tag = models.ForeignKey('Tag', on_delete=models.CASCADE)
    musician = models.ForeignKey('Musician', on_delete=models.CASCADE)


class AlbumTag(models.Model):
    tag = models.ForeignKey('Tag', on_delete=models.CASCADE)
    album = models.ForeignKey('Album', on_delete=models.CASCADE)


class Song(models.Model):
    song_name = models.CharField(max_length=255)
    song_last = models.IntegerField()
    resource = models.CharField(max_length=255)
    album = models.ForeignKey('Album', on_delete=models.CASCADE)

    class Meta:
        unique_together = ("song_name", "album")


class Order(models.Model):
    consumer = models.ForeignKey('User', on_delete=models.CASCADE)
    album = models.ForeignKey('Album', on_delete=models.CASCADE)
    time = models.DateTimeField()


class Subscribe(models.Model):
    user = models.ForeignKey('User', on_delete=models.CASCADE)
    musician = models.ForeignKey('Musician', on_delete=models.CASCADE)
    time = models.DateTimeField()


class Comment(models.Model):
    user = models.ForeignKey('User', on_delete=models.CASCADE)
    album = models.ForeignKey('Album', on_delete=models.CASCADE)
    time = models.DateTimeField()
    content = models.TextField()