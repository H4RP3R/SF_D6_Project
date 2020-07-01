from django.db import models


class Passport(models.Model):
    entered = models.DateField()
    vaccination = models.BooleanField()
    cage_num = models.CharField(max_length=16)

    def __str__(self):
        if hasattr(self, 'cat'):
            return f'{self.cat} ({self.cage_num})'
        elif hasattr(self, 'dog'):
            return f'{self.dog} ({self.cage_num})'
        elif hasattr(self, 'animal'):
            return f'{self.animal} ({self.cage_num})'
        else:
            return 'blank'
