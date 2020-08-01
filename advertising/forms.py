from django.forms import ModelForm


from .models import Platforms

class PlatformForm(ModelForm):
    class Meta:
        model = Platforms

        fields = [
            'facebook', 
            'instagram',
            'google', 
            'budget', 
            'budgetperiod',
            'extrainfo'
        ]