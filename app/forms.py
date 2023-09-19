from django import forms
from .models import CustomerOrders


class CustomerOrdersForm(forms.ModelForm):
    state = forms.ChoiceField(
        choices=[('Andhra Pradesh','Andhra Pradesh')],
        required=True,
        widget=forms.Select(attrs={'class': 'form-control'}),
        initial='Andhra Pradesh'
    )
    country = forms.ChoiceField(
        choices=[('India','India')],
        required=True,
        widget=forms.Select(attrs={'class': 'form-control'}),
        initial='India'
    )
    district = forms.ChoiceField(
        choices=[('Eluru','Eluru')],
        required=True,
        widget=forms.Select(attrs={'class': 'form-control'}),
        initial='Eluru'
    )
    mandal = forms.ChoiceField(
        choices=[('Eluru','Eluru')],
        required=True,
        widget=forms.Select(attrs={'class': 'form-control'}),
        initial='Eluru'
    )
    village = forms.ChoiceField(
        choices=[('Eluru','Eluru')],
        required=True,
        widget=forms.Select(attrs={'class': 'form-control'}),
        initial='Eluru'
    )
    class Meta:
        model = CustomerOrders
        fields = '__all__'  # Include all fields in the form


