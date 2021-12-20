from django.db import models

# Create your models here.

rating = (
    (1, 1),
    (2, 2),
    (3, 3),
    (4, 4),
    (5, 5),
)


class ReviewModel(models.Model):
    full_name = models.CharField(max_length=255)
    email = models.EmailField()
    picture = models.ImageField(upload_to='reviewer')
    rating = models.IntegerField(verbose_name='Rating', blank=False, choices=rating)
    comment = models.TextField(verbose_name='Comment', blank=True)
    review_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.full_name} - {self.rating}'
