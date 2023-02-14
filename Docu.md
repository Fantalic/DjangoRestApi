# Pipenv 

is a tool that aims to bring the best of all packaging worlds (bundler, composer, npm, cargo, yarn, etc.) to the Python world. 
Windows is a first-class citizen, in our world.

It automatically creates and manages a virtualenv for your projects, as well as adds/removes packages from your Pipfile as you install/uninstall packages. 
It also generates the ever-important Pipfile.lock, which is used to produce deterministic builds.

Pipenv is primarily meant to provide users and developers of applications with an easy method to setup a working environment. 
For the distinction between libraries and applications and the usage of setup.py vs Pipfile to define dependencies, see ☤ Pipfile vs setup.py.


# Django Rest Framework - Serializers

A serializer in Django Rest Framework is a way to convert complex data types, such as Django models, into Python data types that can then be easily rendered into JSON or other content types. Serializers allow complex data such as querysets and model instances to be converted to native Python datatypes that can then be easily rendered into JSON, XML or other content types. These data types are typically more flexible and easier to work with than the Django models themselves, and can be used to perform various tasks such as validation, error handling, and more.

In the `serializers.py` file, you define a serializer class for each model you want to serialize. The serializer class defines the fields to be serialized and the validation rules for each field. The fields are defined using classes such as `CharField`, `EmailField`, and `DateTimeField`, which correspond to different types of data such as strings, emails, and dates. The validation rules are defined using methods such as `validate_<field_name>`, where you can perform custom validation logic for each field.

Once the serializer class has been defined, you can use it in your views to perform various tasks such as validating incoming data, converting data between the internal Django models and the external Python data types, and more. The serializer class can also be used to output the data in a specific format, such as JSON or XML, which makes it easier to consume the data in other applications.


# WSGI
WSGI allows Python web applications to be executed by a variety of web servers, such as Apache, Nginx, and Gunicorn. This standardization makes it easier to develop and deploy Python web applications, as it abstracts the underlying web server and allows the application to run on any server that supports the WSGI specification.

# MIDDLEWARE

The django.middleware.csrf.CsrfViewMiddleware is included in the MIDDLEWARE setting to provide protection against Cross-Site Request Forgery (CSRF) attacks.

CSRF attacks are a type of security vulnerability that occurs when a malicious website sends a request to your website using the credentials of an authenticated user. This allows the attacker to perform actions on your website on behalf of the user without their knowledge.

Django provides a built-in protection against CSRF attacks by including a unique token in the form data or header of each request made to the website. The CsrfViewMiddleware then checks this token on each incoming request to ensure that it matches the expected token. If the token does not match, the request is blocked, and an error is returned to the user.

In most cases, it is recommended to include the CsrfViewMiddleware in your MIDDLEWARE setting to protect your website from CSRF attacks. However, if you have a REST API that only accepts requests made by other applications and not by web browsers, you may choose to remove this middleware.

# ViewSets

Django REST framework allows you to combine the logic for a set of related views in a single class, called a ViewSet. In other frameworks you may also find conceptually similar implementations named something like 'Resources' or 'Controllers'.

A ViewSet class is simply a type of class-based View, that does not provide any method handlers such as .get() or .post(), and instead provides actions such as .list() and .create().

The method handlers for a ViewSet are only bound to the corresponding actions at the point of finalizing the view, using the .as_view() method.

Typically, rather than explicitly registering the views in a viewset in the urlconf, you'll register the viewset with a router class, that automatically determines the urlconf for you.