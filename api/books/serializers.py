from rest_framework import serializers
from books.models import Book, Chapter

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ('id','title', 'author_name', 'description', 'price')



class ChapterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Chapter
        fields = ('id', 'book_id', 'id','title', 'description')

class ChapterContentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Chapter
        fields = ('id', 'book_id', 'title', 'description', 'content')
