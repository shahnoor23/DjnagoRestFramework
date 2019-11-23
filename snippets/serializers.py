from django.contrib.auth.models import User
from rest_framework import serializers
from snippets.models import Snippet

# 1st method to create a serializer class

""" 
class SnippetSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    title = serializers.CharField(
        required=False, allow_blank=True, max_length=100)
    code = serializers.CharField(style={'base_template': 'textarea.html'})

    def create(self, validated_data):
        """
# Create and return a new `Snippet` instance, given the validated data.
"""
        return Snippet.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """
# Update and return an existing `Snippet` instance, given the validated data.
"""
        instance.title = validated_data.get('title', instance.title)
        instance.code = validated_data.get('code', instance.code)
        instance.save()
        return instance
 """
##################################################
# 2nd method to create a serializer class

"""
class SnippetSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Snippet
        fields = ['id', 'title', 'code', 'owner']

# with owner


class UserSerializer(serializers.ModelSerializer):
    snippets = serializers.PrimaryKeyRelatedField(
        many=True, queryset=Snippet.objects.all())

    class Meta:
        model = User
        fields = ['id', 'username', 'snippets']
"""

# with HyperlinkModelSerializer


class SnippetSerializer(serializers.HyperlinkedModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Snippet
        fields = ['url', 'id', 'owner',
                  ]


class UserSerializer(serializers.HyperlinkedModelSerializer):
    snippets = serializers.HyperlinkedRelatedField(
        many=True, view_name='snippet-detail', read_only=True)

    class Meta:
        model = User
        fields = ['url', 'id', 'username', 'snippets']
