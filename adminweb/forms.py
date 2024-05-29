from django import forms

from index.models import SettingApp, Section1, Section2, Section3, Section4, Section5, Section6


class SettingAppForm(forms.ModelForm):
    class Meta:
        model = SettingApp
        fields = ['title', 'description', 'favicon', 'logo', 'login_text', 'tel', 'mobile', 'address', 'email',
                  'about_text', 'footer_text', 'is_active']


class Section1Form(forms.ModelForm):
    class Meta:
        model = Section1
        fields = ['title', 'lid', 'description', 'image1', 'image2', 'film', 'img1', 'img2', 'img3',
                  'text1', 'text2', 'text3']


class Section2Form(forms.ModelForm):
    class Meta:
        model = Section2
        fields = ['title', 'lid', 'description', 'image1', 'image2', 'image3', 'image4', 'icon1', 'icon2',
                  'text1', 'text2']


class Section3Form(forms.ModelForm):
    class Meta:
        model = Section3
        fields = ['title', 'lid', 'footer']


class Section4Form(forms.ModelForm):
    class Meta:
        model = Section4
        fields = ['title', 'lid', 'image', 'film', 'text_ok', 'icon_ok', 'num_ok', 'text_project',
                  'icon_project', 'num_project', 'text_tajrobe', 'icon_tajrobe', 'num_tajrobe', 'text_person',
                  'icon_person', 'num_person']


class Section5Form(forms.ModelForm):
    class Meta:
        model = Section5
        fields = ['title', 'lid', 'footer']


class Section6Form(forms.ModelForm):
    class Meta:
        model = Section6
        fields = ['title', 'lid', 'footer']


