from django import forms

class CreateNewListing(forms.Form):
    title = forms.CharField(label="Name", max_length=100)
    



# class Food(models.Model):
#     title = models.CharField(max_length=100)
#     description = models.TextField(max_length=10000)
#     expiration_date= models.DateTimeField('date published')
#     #created at or update at by default?
#     pub_date = models.DateTimeField('date published')
#     prepackaged = models.BooleanField(null=True, blank=True)
#     perishable = models.BooleanField(null=True, blank=True)
