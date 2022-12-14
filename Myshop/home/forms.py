from django.db.models import Model
from django import forms
from .models import Size


class SizeForm(forms.Form):
    class Meta:
        model = Size
        fields = ('size')

# class SizeForm(forms.Form):
#     class Meta:
#         model = Size
#         fields = '__all__'
#
#         def __init__(self, *args, **kwargs):
#             super().__init__(*args, **kwargs)
#             self.fields['size'].queryset = Size.objects.none()
#
#             if 'size' in self.data:
#                 try:
#                     size_id = int(self.data.get('Size'))
#                     self.fields['size'].queryset = Size.objects.filter(size_id=size_id).order_by('name')
#                 except (ValueError, TypeError):
#                     pass  # invalid input from the client; ignore and fallback to empty City queryset
#             elif self.instance.pk:
#                 self.fields['size'].queryset = self.instance.size.city_set.order_by('name')
#
#
#     #
#     # def __init__(self):
#     # size = forms.CharField(label='Select size',
#     #                         widget=forms.Select(choices=SIZE_CHOICES))
#     #
#     # def clean(self):
#     #     cleaned_data = super().clean()
#     #     size = cleaned_data.get("size")
#
#
# class MyForm(forms.Form):
#     # create a dropdown with the choices "apple", "banana", and "cherry"
#     fruit = forms.ChoiceField(choices=["apple", "banana", "cherry"])
#
#     def clean(self):
#         cleaned_data = super().clean()
#         fruit = cleaned_data.get("fru