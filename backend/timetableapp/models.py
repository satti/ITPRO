from django.db import models

class Subjects(models.Model):
    y = [('I-Year','I-year'),('II-Year','II-year'),('III-Year','III-year'),('IV-Year','IV-year')]
    year = models.CharField(choices=y,blank=True,max_length=100)
    s = [('I-Semester','I-semester'),('II-Semester','II-sem'),('III-Semester','III-sem'),('IV-Semester','IV-sem'),
         ('V-Semester','V-sem'),('VI-Semester','VI-sem'),('VII-Semester','VII-sem'),('VIII-Semester','VIII-sem')]
    sem = models.CharField(choices=s,blank=True,max_length=100)
    subject_code = models.CharField(max_length=150,blank=True)
    subject_name = models.CharField(max_length=150,blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.subject_name

    class Meta:
        ordering = ['-updated','-created']