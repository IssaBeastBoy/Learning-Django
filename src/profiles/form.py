from django import forms

from .models import Profile

class LoginForm (forms.ModelForm):    
    class Meta:
        model = Profile
        fields = [
            'Email',
            'Password',
        ]
        widgets ={
            "Password":forms.PasswordInput(),
        }
    def clean_Email(self):
        email = self.cleaned_data.get('Email')
        obj_number = Profile.objects.count()
        cur_obj = 1
        while (cur_obj < obj_number ):
            users = Profile.objects.get(id = cur_obj)
            if users.Email == email:
                return email
            cur_obj = cur_obj + 1
            if cur_obj == obj_number:
                raise forms.ValidationError("Invalid email address")
    def clean_Password(self):
        pwd = self.cleaned_data.get('Password')
        obj_number = Profile.objects.count()
        cur_obj = 1
        while (cur_obj < obj_number ):
            users = Profile.objects.get(id = cur_obj)
            if users.Password == pwd:
                return pwd
            cur_obj = cur_obj + 1
            if cur_obj == obj_number:
                raise forms.ValidationError("Incorrect password")

        

class New_user (forms.ModelForm):
    class Meta:
        model = Profile        
        fields = [
            'Name',
            'Surname',
            'Email',
            'Field',
            'Institution',
            'Interest',
            'Password',
        ]
        widgets ={
            "Password":forms.PasswordInput(),
        }
    def clean_Email(self):
        email = self.cleaned_data.get('Email')
        obj_number = Profile.objects.count()
        cur_obj = 1
        while (cur_obj < obj_number ):
            users = Profile.objects.get(id = cur_obj)
            if users.Email == email:
                raise forms.ValidationError("Email already in use")
            cur_obj = cur_obj + 1
            if cur_obj == obj_number:
                return email
                