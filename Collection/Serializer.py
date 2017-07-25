from rest_framework import serializers

from Collection.models import Article, Reporter


class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = ('id', 'headline', 'pub_date', 'reporter')


class ReporterSerializer(serializers.ModelSerializer):
    articles = ArticleSerializer(many=True, read_only=True)

    class Meta:
        model = Reporter
        fields = ('id', 'first_name', 'last_name', 'email', 'articles')

    def validate(self, data):
        first_name = data['first_name']
        last_name = data['last_name']

        if not len(first_name) > 10:
            raise serializers.ValidationError("Please enter first name >10")

        if not len(last_name) > 10:
            raise serializers.ValidationError("Please enter last name >10")

        return data


class ReporterSerializer2(serializers.ModelSerializer):
    class Meta:
        model = Reporter
        fields = ('id', 'first_name', 'last_name', 'email')


class ArticleSerializer2(serializers.ModelSerializer):
    reporter = ReporterSerializer2(many=False, read_only=True)

    class Meta:
        model = Article
        fields = ('id', 'headline', 'pub_date', 'reporter')
