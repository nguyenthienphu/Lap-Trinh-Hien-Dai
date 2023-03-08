from rest_framework import serializers
from .models import Category, Course, Lesson, Tag


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name']


class CourseSerializer(serializers.ModelSerializer):
    image = serializers.SerializerMethodField(source='image')

    def get_image(self, course):
        if course.image:
            request = self.context.get('request')
            return request.build_absolute_uri('/static/%s' % course.image.name) if request else ''

    class Meta:
        model = Course
        fields = ['id', 'created_date', 'updated_date', 'active', 'subject', 'description', 'category_id', 'image']


class TagSerialized(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ['id', 'created_date', 'updated_date', 'active', 'name']


class LessonSerializer(serializers.ModelSerializer):
    image = serializers.SerializerMethodField(source='image')

    def get_image(self, lesson):
        if lesson.image:
            request = self.context.get('request')
            return request.build_absolute_uri('/static/%s' % lesson.image.name) if request else ''

    class Meta:
        model = Lesson
        fields = ['id', 'created_date', 'updated_date', 'active', 'subject', 'course_id', 'image']


class LessonDetailsSerializer(LessonSerializer):
    tags = TagSerialized(many=True)

    class Meta:
        model = LessonSerializer.Meta.model
        fields = LessonSerializer.Meta.fields + ['content', 'tags']




