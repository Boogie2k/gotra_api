
from rest_framework import serializers
from .models import Snippet, Tags, subgoals

class TagsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tags
        fields = ['tag_text']

class SubgoalsSerializer(serializers.ModelSerializer):
    class Meta:
        model = subgoals
        fields = ['subgoals_text', 'isCompleted', 'creation_date']
        

class SnippetSerializer(serializers.ModelSerializer):
    subgoals=SubgoalsSerializer(many=True)
    tag = TagsSerializer(many=True)

    class Meta:
        model = Snippet
        fields = ['id', 'created', 'title', 'description', 'on_hold', 'not_started', 'completed', 'progress', 'start', 'end', 'tag','subgoals']
