from django.contrib.auth import get_user_model
from django.db import models


class Author(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=40)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

    class Meta:
        verbose_name = 'Author'
        verbose_name_plural = 'Authors'


class Tag(models.Model):
    word = models.CharField(max_length=35)
    slug = models.CharField(max_length=50)

    def __str__(self):
        return self.word

    class Meta:
        verbose_name = 'Tag'
        verbose_name_plural = 'Tags'


class Book(models.Model):
    title = models.CharField(max_length=40)
    cover = models.ImageField(upload_to='book-covers', blank=True)
    tags = models.ManyToManyField(Tag, related_name='books')
    authors = models.ManyToManyField(Author, related_name='books')
    publication_date = models.DateField()

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Book'
        verbose_name_plural = 'Books'


class Borrow(models.Model):
    user = models.OneToOneField(get_user_model(), on_delete=models.PROTECT)
    borrow_date = models.DateField()
    returned_date = models.DateField(blank=True, null=True)
    book = models.ForeignKey(Book, on_delete=models.PROTECT)

    class Meta:
        verbose_name = 'Borrow'
        verbose_name_plural = 'Borrows'

    def __str__(self):
        return f'{self.user}_{self.borrow_date}'