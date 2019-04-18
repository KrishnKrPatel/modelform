from django import forms

class ProductForm(forms.Form):
    pid=forms.IntegerField()
    pname=forms.CharField(max_length=20)
    pcost=forms.DecimalField(max_digits=10,decimal_places=2)
    pmfdt=forms.DateField()
