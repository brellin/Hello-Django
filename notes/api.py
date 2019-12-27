from rest_framework import serializers, viewsets
from .models import PersonalNote, Note


class PersonalNoteSerializer(serializers.HyperlinkedModelSerializer):

    def create(self, validated_data):
        user = self.context['request'].user
        note = PersonalNote.objects.create(user=user, **validated_data)
        return note

    class Meta:
        model = PersonalNote
        fields = ('title', 'content')


class PersonalNoteViewSet(viewsets.ModelViewSet):

    def get_queryset(self):
        user = self.request.user
        return PersonalNote.objects.none() if user.is_anonymous else PersonalNote.objects.filter(user=user)

    serializer_class = PersonalNoteSerializer
    queryset = Note.objects.none()
