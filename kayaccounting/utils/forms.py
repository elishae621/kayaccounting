from django import forms

class MyErrorList(forms.utils.ErrorList):
    def __init__(self, initlist=None, error_class="invalid-feedback"):
        super().__init__(initlist=initlist, error_class=error_class)


class MyBaseForm(forms.Form):
    def __init__(self, *args, **kwargs):
        kwargs_new = {**kwargs, 
        'error_class': MyErrorList,
        'label_suffix': ''}
        super().__init__(*args, **kwargs_new) 



class MyBaseModelForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        kwargs_new = {**kwargs, 
        'error_class': MyErrorList,
        'label_suffix': ''}
        super().__init__(*args, **kwargs_new) 
