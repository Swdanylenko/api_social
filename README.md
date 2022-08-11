# api_social
 Simple social network api

Usage:
pyhton manage.py makemigrations
python manage.py migrate
python manage.py runserver <ip:port>

URLs:
+user signup: 
<ip:port>/api/users/register
	POST:
	{
    "user": {
        "username": "username",
        "email": "user@email.com",
        "password": "passw1!s"
		}
	}

+user login:
<ip:port>/api/users/login
	POST:
	{
    "user": {
        "email": "user@email.com",
        "password": "passw1!s"
			}
	}
	
+get user activity:
<ip:port>/api/users
	GET using "token"

+get all posts:
<ip:port>/api/posts
	GET using "token"
	
+create post:
<ip:port>/api/posts/create
	POST using "token":
	{
        "title": "post title",
        "body": "post body"
    }
	
+vote/unvote:
<ip:port>/api/posts/vote
	POST using "token":
	{
		"vote":
		{
			"id": 1
		}
	}
	
+analitics:
<ip:port>/api/posts/analitics/
	GET with params: ?date_from=2022-08-10&date_to=2022-08-11