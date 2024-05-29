from rest_framework import serializers

from index.models import SettingApp, Section1, Section2, Section3, Section4, Section5, Section6


class SettingAppSerializer(serializers.ModelSerializer):
    class Meta:
        model = SettingApp
        fields = ('id', 'title', 'description', 'favicon', 'logo', 'login_text', 'tel', 'mobile', 'address', 'email',
                  'about_text', 'footer_text', 'is_active')

    def create(self, validated_data):
        key = validated_data.pop('key')
        instance = super().create(validated_data)
        return instance


class Section1Serializer(serializers.ModelSerializer):

    class Meta:
        model = Section1
        fields = ('id', 'title', 'lid', 'description', 'image1', 'image2', 'film', 'img1', 'img2', 'img3',
                  'text1', 'text2', 'text3')


class Section2Serializer(serializers.ModelSerializer):

    class Meta:
        model = Section2
        fields = ('id', 'title', 'lid', 'description', 'image1', 'image2', 'image3', 'image4', 'icon1', 'icon2',
                  'text1', 'text2')


class Section3Serializer(serializers.ModelSerializer):

    class Meta:
        model = Section3
        fields = ('id', 'title', 'lid', 'footer')


class Section4Serializer(serializers.ModelSerializer):

    class Meta:
        model = Section4
        fields = ('id', 'title', 'lid', 'image', 'film', 'film', 'text_ok', 'icon_ok', 'num_ok', 'text_project',
                  'icon_project', 'num_project', 'text_tajrobe', 'icon_tajrobe', 'num_tajrobe', 'text_person',
                  'icon_person', 'num_person')


class Section5Serializer(serializers.ModelSerializer):

    class Meta:
        model = Section5
        fields = ('id', 'title', 'lid', 'footer')


class Section6Serializer(serializers.ModelSerializer):

    class Meta:
        model = Section6
        fields = ('id', 'title', 'lid', 'footer')


