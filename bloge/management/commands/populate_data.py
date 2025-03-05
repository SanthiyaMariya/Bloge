from django.core.management.base import BaseCommand
from bloge.models import Post,Category
import random

class Command(BaseCommand):

    help="this comamnd insert post data into database" 


    def handle(self, *args, **options):

     # delete all existing data
     #Post.objects.all().delete()
     
        
     post_titles = [
    "Mastering Django in 30 Days",
    "Top 10 Python Tips for Beginners",
    "How to Build a Personal Blog with Django",
    "Understanding Django Models and Migrations",
    "Best Practices for Django Project Structure",
    "Why Django is the Best Framework for Startups",
    "Creating Dynamic Web Pages with Django and JavaScript",
    "Integrating Django with REST APIs",
    "Securing Your Django Application: A Complete Guide",
    "Deploying Django Projects on Cloud Platforms"
]
     post_contents = [
    "Learn Django step by step in 30 days with practical examples and real-world projects. This comprehensive guide covers everything from setting up your development environment to deploying your application on cloud platforms, ensuring you gain hands-on experience throughout the journey.",
    "Discover the top 10 Python tips to write cleaner and more efficient code. Master techniques such as list comprehensions, lambda functions, and context managers that not only improve your Django applications but also enhance your overall coding skills for better maintainability.",
    "A complete guide on how to build and deploy your personal blog using Django. Learn to create models for posts and comments, design dynamic templates, implement user authentication, and deploy your blog to the cloud, making it accessible to the world.",
    "Understand Django Models and Migrations to manage your database effectively. This article covers the basics of Django ORM, creating complex queries, and maintaining database integrity, all while ensuring smooth schema changes with powerful migration tools.",
    "Organize your Django project like a pro with these best practices. Learn about the recommended folder structure, reusable apps, settings management, and strategies for maintaining clean and maintainable code in complex, large-scale applications.",
    "Explore why Django is a popular choice for startups and rapid development. Discover its built-in features like authentication, admin interface, and ORM, which help developers build secure, scalable, and maintainable web applications faster than ever before.",
    "Learn how to make dynamic and interactive web pages with Django and JavaScript. Understand how to use Django's template language with modern JavaScript frameworks like Vue.js and React to create seamless user experiences and highly interactive web applications.",
    "A beginner's guide to integrating Django with powerful REST APIs. Learn to build scalable APIs using Django REST Framework, implement authentication with JSON Web Tokens, and consume third-party APIs to extend your web application's functionality.",
    "Protect your Django application with these essential security practices. Explore Django's built-in security features like CSRF protection, SQL injection prevention, and secure password hashing, along with best practices for deploying securely in production environments.",
    "Step-by-step guide on deploying Django projects to cloud platforms. Learn to configure settings for different environments, use Docker for containerization, and deploy your application to platforms like Heroku, AWS, and DigitalOcean for scalable and reliable hosting."
]



     img_url=[

'https://picsum.photos/id/1/800/400',
'https://picsum.photos/id/2/800/400',
'https://picsum.photos/id/3/800/400',
'https://picsum.photos/id/4/800/400',
'https://picsum.photos/id/5/800/400',
'https://picsum.photos/id/6/800/400',
'https://picsum.photos/id/7/800/400',
'https://picsum.photos/id/8/800/400',
'https://picsum.photos/id/9/800/400',
'https://picsum.photos/id/10/800/400'
]

     categories=Category.objects.all()

     for p_title,p_content,p_img_url in zip(post_titles,post_contents,img_url):
        c_category=random.choice(categories)
        Post.objects.create(title=p_title,content=p_content,img_url=p_img_url,category=c_category)
       

     self.stdout.write(self.style.SUCCESS("the data is successfully updated")) 


             
