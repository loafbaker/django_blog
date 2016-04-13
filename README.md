django_blog
=================

A tutorial basic blog web-app based on the framework of Django 1.9.

Run successfully within Django 1.9.4 and Python 2.7.6

# Setup

Install all the required libraries

    pip install -r requirements.txt

Rebuild database

    rm blog.sqlite3
    python manage.py migrate
    python manage.py createsuperuser

Alternative: In the case you want to keep demo data, then you just need to create your own superuser account.

    python manage.py createsuperuser

Collect static files

    python manage.py collectstatic

Run web server

    python manage.py runserver

Finally, you can view the web app with your local browser by accessing `http://localhost:8000/`.

Also, you can access the administration page by logging in with your superuser account within the interface `http://localhost:8000/admin/`.

# Minor Versions

Ver.1   [Install & Admin](../../tree/63967d94c2443d3665a435d4b1ad3448e8f59131)

Ver.2   [First App & Model](../../tree/1a0ff02f17824fe3b1a8435e18138b046669638f)

Ver.3   [Customize Admin](../../tree/1b29d70569a3b75e64c54017f59a59fcd0c26697)

Ver.4   [Mapping URLs to Views](../../tree/7c54a0413afe4d2453dfafa391a5150538395334)

Ver.5   [In App URLs](../../tree/139682c5ed8d7865cea562d87324ccb5d7a8d48c)

Ver.6   [Template Context](../../tree/fb632dbd65b798dee54969d13416088429674646)

Ver.7   [Get Post Item with Query](../../tree/18c35349ebe3d5245d3087306b0910e8220c28c2)

Ver.8   [URL Links & Get Absolute URL](../../tree/7461e9d1b2cdc1990609c933f6e30be49da7389c)

Ver.9   [ModelForm & Create View](../../tree/47ffb0dc24a921cb710e0dd842e20d5017a8d621)

Ver.10   [Instance Update View & Messages](../../tree/f504653a37208d0719de2b2191e74837a7545ab8)

Ver.11   [Delete View](../../tree/33c613e2d435bdbb0e6c375c926f2bfa3484c7c8)

Ver.12   [Template & Inheritance](../../tree/179e6e213c8526defa7127081f3059fa325ca4d6)

Ver.13   [Setup Static Files](../../tree/33026f355c2eb4ba6b983c45500557879dc75ea0)

Ver.14   [Implement Bootstrap](../../tree/19fb3f825bc6ebcdff09bcf6be31668cf9877e3b)

Ver.15   [Pagination by QuerySet](../../tree/065d89c838750121d06c2a9500826c1166db7d4a)

Ver.16   [File Uploads with FileField and ImageField](../../tree/65d3cb994ca1d30187697e32a611c934676ae639)

Ver.17   [SlugField](../../tree/b2a11513a3d3b32580aefac3fbdfa05a02005348)

Ver.18   [Social Share Links](../../tree/c5fc576d80b8fd3a9fe35c5433fbf53b0d2c25e8)

Ver.19   [Custom Template Tag](../../tree/31f250fee17d467ccf06c649020d75baa9a715c8)

Ver.20   [Basic User Permissions](../../tree/359afe0cb1475eaf3619ccaff70f9afbcbe5fbc4)

Ver.21   [Associate User to Post with a Foreign Key](../../tree/9738b44995eedff2fd46b4e155f4ed65622c3d26)

Ver.22   [Using Facebook Comments](../../tree/593f91ec10ae9e47c72ad47d9f4902859e568d90)

Ver.23   [Item Publish Date & Handling Drafts](../../tree/6f0f9d997765a69401426065bc4f40e113ad4747)

Ver.24   [Search Posts](../../tree/c58056ad61f8bbda7e0e02431b1277a46ec4722a)

**Ver.25   [v1.0](../../tree/v1.0)** _(Stable Ver.)_

Curr. Ver.   Render Markdown