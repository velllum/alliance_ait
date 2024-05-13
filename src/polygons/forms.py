from django import forms


class AddForm(forms.Form):
    name = forms.CharField(label='Наименование', widget=forms.TextInput(
        attrs={"class": "form-control form-control-sm", "placeholder": "Введите наименование"}))

    latitude = forms.DecimalField(label='Широта', min_value=-90, max_value=90, widget=forms.NumberInput(
        attrs={"class": "form-control form-control-sm", "placeholder": "Введите широту"}))

    longitude = forms.DecimalField(label='Долгота', min_value=-180, max_value=180, widget=forms.NumberInput(
        attrs={"class": "form-control form-control-sm", "placeholder": "Введите долготу"}))

    polygon = forms.CharField(label='Результат', widget=forms.Textarea(
        attrs={"class": "form-control form-control-sm", "style": "height: 70px"}), required=False, disabled=True)

