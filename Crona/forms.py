from django import forms
from Crona.models import  Subscribe

class EmailForm(forms.ModelForm):
    class Meta:
        model = Subscribe
        fields = ('email',)

    def __init__(self, *args, **kwargs):
        super(EmailForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_show_labels = False
        for fieldname in ['email',]:
            self.fields[fieldname].help_text = None
