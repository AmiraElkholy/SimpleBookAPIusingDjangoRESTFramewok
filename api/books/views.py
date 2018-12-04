from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from books.models import Book, Chapter
from books.serializers import BookSerializer, ChapterSerializer, ChapterContentSerializer



##########-------> BOOK VIEWS <-------##########

#list && add books
@api_view(['GET', 'POST'])
def book_list(request):
    if request.method == 'GET':
        books = Book.objects.all()
        serializer = BookSerializer(books, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = BookSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



# list , update & delete a single book..
@api_view(['GET', 'PUT', 'DELETE'])
def book_detail(request, book_id):
        try:
            book = Book.objects.get(id=book_id)
        except Book.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        if request.method == 'GET':
            serializer = BookSerializer(book)
            return Response(serializer.data)

        elif request.method == 'PUT':
            serializer = BookSerializer(book, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        elif request.method == 'DELETE':
            book.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)





##########-------> CHAPTER VIEWS <-------##########

# list specific book_chapters
@api_view(['GET'])
def book_chapters_list(request, book_id):
    if request.method == 'GET':
        try:
            book = Book.objects.get(id=book_id)
            chapters = book.chapter_set.all()
        except Book.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        serializer = ChapterSerializer(chapters, many=True)
        return Response(serializer.data)


#list single book_chapter content ..
@api_view(['GET'])
def book_chapter_content(request, book_id, chapter_id):
    if request.method == 'GET':
        try:
            book = Book.objects.get(id=book_id)
            chapters = book.chapter_set.all()
            chapter = chapters.get(id=chapter_id)
        except (Book.DoesNotExist, Chapter.DoesNotExist) as e:
            return Response(status=status.HTTP_404_NOT_FOUND)
        else:
            serializer = ChapterContentSerializer(chapter)
            return Response(serializer.data)






# note: have only added CRUD operations to books , but the same can be applied to book chapters
