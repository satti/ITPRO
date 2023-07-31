from django.db import models

class Subjects(models.Model):
    y = [('I-YEAR','I-year'),('II-YEAR','II-year'),('III-YEAR','III-year'),('IV-YEAR','IV-year')]
    year = models.CharField(choices=y,blank=True,max_length=100)
    s = [('I-SEM','I-sem'),('II-SEM','II-sem'),('III-SEM','III-sem'),('IV-SEM','IV-sem'),
         ('V-SEM','V-sem'),('VI-SEM','VI-sem'),('VII-SEM','VII-sem'),('VIII-SEM','VIII-sem')]
    sem = models.CharField(choices=s,blank=True,max_length=100)
    subject_name = models.CharField(max_length=150,blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.subject_name

