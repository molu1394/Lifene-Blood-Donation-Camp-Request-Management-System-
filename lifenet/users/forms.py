from django import forms
from .models import DonorProfile, PatientProfile, BloodBankProfile, StaffProfile,AdminProfile,OrganizationProfile

class DonorProfileForm(forms.ModelForm):
    class Meta:
        model = DonorProfile
        fields = ["first_name","last_name","dob", "gender", "blood_group", "address", "mobile_number","ready_to_donate","profile_pic"]
        widgets = {
            "first_name": forms.TextInput(attrs={'class': 'form-control','required': True}),
            "last_name": forms.TextInput(attrs={'class': 'form-control','required': True}),
            "dob": forms.DateInput(attrs={'type': 'date', 'class': 'form-control','required': True}),
            "gender": forms.Select(attrs={'class': 'form-select custom-dropdown','required': True,'id':'dp'}),
            "blood_group": forms.Select(attrs={'class': 'form-select custom-dropdown','required': True,'id':'dp'}),
            "address": forms.TextInput(attrs={'class': 'form-control','required': True,"autocomplete": "address"}),
            "mobile_number": forms.TextInput(attrs={'class': 'form-control','required': True}),
            "ready_to_donate": forms.CheckboxInput(attrs={'class': 'form-check-input','required': True}),
            "profile_pic": forms.FileInput(attrs={"class": "form-control"})
        }
    def clean_dob(self):
        dob = self.cleaned_data.get("dob")
        if not dob:
            raise forms.ValidationError("Date of birth is required.")
        return dob

class PatientProfileForm(forms.ModelForm):
    class Meta:
        model = PatientProfile
        fields = ["first_name","last_name","blood_group_req","mobile_number","address","profile_pic"]
        widgets = {
            "first_name": forms.TextInput(attrs={'class': 'form-control','required': True}),
            "last_name": forms.TextInput(attrs={'class': 'form-control','required': True}),
            "blood_group_req": forms.Select(attrs={'class': 'form-select','required': True}),
            "mobile_number": forms.TextInput(attrs={'class': 'form-control','required': True}),
            "address": forms.TextInput(attrs={'class': 'form-control', 'required': True,"autocomplete": "address"}),
            "profile_pic": forms.FileInput(attrs={'class': 'form-control'}),
        }


class BloodBankProfileForm(forms.ModelForm):
    class Meta:
        model = BloodBankProfile
        fields = ["bloodbank_name", "mobile_number", "address", "authorize_number"]
        widgets = {
            "bloodbank_name": forms.TextInput(attrs={'class': 'form-control','required': True}),
            "mobile_number": forms.TextInput(attrs={'class': 'form-control','required': True}),
            "address": forms.TextInput(attrs={'class': 'form-control','required': True,"autocomplete": "address"}),
            "authorize_number": forms.TextInput(attrs={'class': 'form-control','required': True}),
        }

class OrganizationProfileForm(forms.ModelForm):
    class Meta:
        model = OrganizationProfile
        fields = ["organization_name", "organization_type", "mobile_number", "authorize_number"]
        widgets = {
            "organization_name": forms.TextInput(attrs={'class': 'form-control','required': True}),
            "organization_type": forms.TextInput(attrs={'class': 'form-control','required': True}),
            "mobile_number": forms.TextInput(attrs={'class': 'form-control','required': True}),
            "authorize_number": forms.TextInput(attrs={'class': 'form-control','required': True}),
        }

class StaffProfileForm(forms.ModelForm):
    class Meta:
        model = StaffProfile
        fields = ["first_name","last_name","mobile_number","bloodbank_name","profile_pic"]
        widgets = {
            "first_name": forms.TextInput(attrs={'class': 'form-control','required': True}),
            "last_name": forms.TextInput(attrs={'class': 'form-control','required': True}),
            "mobile_number": forms.TextInput(attrs={'class': 'form-control','required': True}),
            "bloodbank_name": forms.Select(attrs={'class': 'form-control','required': True}),
            "profile_pic": forms.FileInput(attrs={'class': 'form-control'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["bloodbank_name"].queryset = BloodBankProfile.objects.filter(approval_status__iexact="approved")

class AdminProfileForm(forms.ModelForm):
    class Meta:
        model = AdminProfile
        fields = ["first_name", "last_name"]
        widgets = {
            "first_name": forms.TextInput(attrs={'class': 'form-control','required': True}),
            "last_name": forms.TextInput(attrs={'class': 'form-control','required': True}),
        }