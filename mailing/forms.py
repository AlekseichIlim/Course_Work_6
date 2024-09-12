from django.forms import ModelForm, BooleanField

from mailing.models import Dispatch, Client, Message


class StyleMixin:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            if isinstance(field, BooleanField):
                field.widget.attrs['class'] = 'form-check-input'
            else:
                field.widget.attrs['class'] = 'form-control'


class DispatchForm(ModelForm):
    class Meta:
        model = Dispatch
        exclude = ('next_sent_date_time', 'owner', )


class ClientForm(ModelForm):
    class Meta:
        model = Client
        exclude = ('owner', )


class MessageForm(ModelForm):
    class Meta:
        model = Message
        exclude = ('owner', )
