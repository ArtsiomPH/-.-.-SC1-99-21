from rest_framework import serializers
# from rest_framework.renderers import JSONRenderer

from start_page.models import Medcine, Synonyms


class MedcineSerializer(serializers.ModelSerializer):
    class Meta:
        model = Medcine
        fields = ("pk", "international_name", "general_url_name", "general_info", "general_documentation")


class SynonymsSerializer(serializers.ModelSerializer):
    medcine = serializers.CharField()

    class Meta:
        model = Synonyms
        fields = ('pk', 'comm_name', 'url_name', 'medcine')

# class MedcineSerializer(serializers.Serializer):
#     pk = serializers.IntegerField(read_only=True)
#     international_name = serializers.CharField(max_length=300)
#     general_url_name = serializers.CharField(max_length=50)
#     general_info = serializers.CharField()
#     formula = serializers.ImageField(read_only=True)
#     pub_date = serializers.DateTimeField(read_only=True)
#     pub_update = serializers.DateTimeField(read_only=True)
#     general_documentation = serializers.URLField(read_only=True)
#
#     def create(self, validated_data):
#         return Medcine.objects.create(**validated_data)
#
#     def update(self, instance, validated_data):
#         instance.international_name = validated_data.get('international_name', instance.international_name)
#         instance.general_url_name = validated_data.get('general_url_name', instance.general_url_name)
#         instance.general_info = validated_data.get('general_info', instance.general_info)
#         instance.formula = validated_data.get('formula', instance.formula)
#         instance.pub_date = validated_data.get('pub_date', instance.pub_date)
#         instance.pub_update = validated_data.get('pub_update', instance.pub_update)
#         instance.general_documentation = validated_data.get('general_documentation', instance.general_documentation)
#         instance.save()
#         return instance

# def encode():
#     model = MedcineModel('diclophenac', 'нельзя')
#     model_sr = MedcineSerializer(model)
#     json = JSONRenderer().render(model_sr.data)
