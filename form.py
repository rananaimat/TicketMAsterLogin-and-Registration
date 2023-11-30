from django import forms
from ticketMaster.models import TicketMaster

class TicketMasterForm(forms.ModelForm):

        class Meta:
            model = TicketMaster
            fields = '_all_'