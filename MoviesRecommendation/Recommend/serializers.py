from rest_framework_mongoengine import serializers
from MoviesRecommendation.Recommend.models import Movies, Ratings, Links, Tags


class MoviesSerializer(serializers.DocumentSerializer):
    class Meta:
        model = Movies
        fields = '__all__'


class RatingsSerializer(serializers.DocumentSerializer):
    class Meta:
        model = Ratings
        fields = '__all__'

class LinksSerializer(serializers.DocumentSerializer):
    class Meta:
        model = Links
        fields = '__all__'

class TagsSerializer(serializers.DocumentSerializer):
    class Meta:
        model = Tags
        fields = '__all__'
