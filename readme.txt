Simple Book API - to list books, book chapters and chapter content,
as well as create, update and delete a single book.



Created By "Amira Elkholy"

On: Thursday, 22/06/2017





urls:

'http://localhost:8000/books/' 		=> method: 'GET' 	=> list all books

'http://localhost:8000/books/{book_id}' 	=> method: 'GET' 	=> display single book details

'http://localhost:8000/books/{book_id}' 	=> method: 'PUT' 	=> update single book details

'http://localhost:8000/books/{book_id}' 	=> method: 'DELETE' 	=> delete single book



'http://localhost:8000/books/{book_id}/chapters' 		=> method: 'GET' 	=> display all chapters of a single book

'http://localhost:8000/books/{book_id}/chapters/{chapter_id}' 	=> method: 'GET' 	=> display a single book chapters






=========== NOTE ===========

The project contains its own virtual environment - running Python3.6, Django 1.11, and mysql database


which you can activate by opening project directory in terminal and typing:
 
$    source env/bin/activate



and deactivate by typing:

$    deactivate




++++++++++++++++++++++++++++






=========== Dependencies ===========

you need to have 'django-mysql' and 'mysqlclient' installed to be able to run and connect to mysql database through django:



$    pip install mysqlclient

$    pip install django-mysql




++++++++++++++++++++++++++++
