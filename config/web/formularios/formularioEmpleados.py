from django import forms

class FormularioRegistroEmpleados(forms.Form):

    DOCUMENTO=(
        (1, 'Cedula'),
        (2, 'NIT')
    )

    nombre = forms.CharField(
        widget=forms.TextInput(attrs={"class":"form-control mb-3"}),
        max_length=25,
        required=True
    )
    descripcion = forms.CharField(
        widget=forms.Textarea(attrs={"class":"form-control mb-3"}),
        max_length=50,
        required=True,
    )
    imagen_Perfil = forms.CharField(
        widget=forms.TextInput(attrs={"class":"form-control mb-3"}),
        max_length=200,
        required=True
    )
    Tipo_Documento = forms.ChoiceField(
        widget=forms.Select(attrs={"class":"form-control mb-3"}),
        choices=DOCUMENTO
    )
    Numero_Documento = forms.CharField(
        widget=forms.NumberInput(attrs={"class":"form-control mb-3"}),
        required=True,
    )
    


    