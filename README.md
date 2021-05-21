# blog_evlovfit

A Blog site implemented using Python/Django(MVT structure).
It contains a list of blogs posted by users. Only registered users can meddle with the options in the site, though anyone can still view the blogs.

Features:
1. A user(anonymous) need not register or login to:
                *View all the blogs or a single blog in the site
                *View all the comments for a blog
                
2. A user needs to register and login to thier account to:
                *Post a blog
                *Edit/Update a blog
                *Delete a blog
                *Post a comment
                *Delete a comment and
                *Everything a anonymous user can do

*At first it was going to be an accountless site but in real life scenario it wont work well. So accounts are a must
*Anonymous can still view the blog, without an account 'cause in real some might get attracted and create an account. (you never know ;) )

Installation and Running the server:

 * Create a virtual environment.
 * git clone https://github.com/JackPersie/blog_evlovfit.git
 
 ** Install Requirements **
  * pip install -r requirements.txt
  * python manage.py makemigrations
  * python manage.py migrate
** Running the server **
 * python manage.py runserver
 App will be running locally (http://127.0.0.1:8000/)
 
By the way, thank you for this oppurtunity :D
