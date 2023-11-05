
from rest_framework import serializers
from .models import Snippet, Tags, Subgoals

class TagsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tags
        fields = ['tag_text']

class SubgoalsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subgoals
        fields = ['subgoals_text', 'isCompleted']
        

class SnippetSerializer(serializers.ModelSerializer):
    subgoals=SubgoalsSerializer(many=True)
    tag = TagsSerializer(many=True)

    class Meta:
        model = Snippet
    
        fields = ['id', 'created', 'title', 'description', 'on_hold', 'not_started', 'completed', 'progress','tag','subgoals']

    def create(self, validated_data):
        tags = validated_data.pop('tag')
        subgoal= validated_data.pop('subgoals')
        snippet = Snippet.objects.create(**validated_data)
        for tag in tags:
            Tags.objects.create(**tag, tag =snippet)
        
        for goal in subgoal:
            Subgoals.objects.create(**goal, subgoals=snippet)
        
        return snippet
        
    def update(self, instance, validated_data):
        tags_data = validated_data.pop('tag')
        subgoals_data = validated_data.pop('subgoals')

    # Update Snippet instance
        instance.title = validated_data.get('title', instance.title)
        instance.description = validated_data.get('description', instance.description)
    # Add other fields that need to be updated...

        instance.save()

    # Update Tags
        for tag_data in tags_data:
            tag_id = tag_data.get('id')
            if tag_id is not None:
                tag = instance.tag.get(id=tag_id)
                tag.name = tag_data.get('name', tag.name)
                tag.save()
            else:
        # Create a new Tag instance if 'id' is not provided
                Tags.objects.create(**tag_data, tag =instance)

    # Update Subgoals
        for subgoal_data in subgoals_data:
            subgoal_id = subgoal_data.get('id')
            if subgoal_id is not None:
                subgoal = instance.subgoals.get(id=subgoal_id)
                subgoal.name = subgoal_data.get('name', subgoal.name)
        # Add other fields that need to be updated...
                subgoal.save()
            else:
        # Create a new Subgoal instance if 'id' is not provided
                Subgoals.objects.create(**subgoal_data, subgoals=instance)

                return instance