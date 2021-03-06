django_blog
=================

A tutorial basic blog web-app based on the framework of Django 1.9.

Run successfully within Django 1.9.8 and Python 2.7.6

# Setup

Install all the required libraries

    pip install -r requirements.txt

(Optional) Delete demo post data

    rm blog.sqlite3
    python manage.py migrate

Create your own superuser account.

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

Ver.26   [Render Markdown](../../tree/15e8ae240417e0724409d6cff3d616d9b772ae99)

Ver.27   [Implement Django Pagedown for Stack Overflow style Markdown](../../tree/fa0a0822a14fb68f39f5bd068d8d2c394e75d221)

Ver.28   [Responsive Image Inside of Post Markdown Content](../../tree/f99ca0c02cdd7c54347a5b56776a8eb751ef80a4)

Ver.29   [Render & Truncate Markdown with Template Tags](../../tree/73fc57ee0b03d0cec708fc1360c846ce5c54d9e3)

Ver.30   [Dynamic Preview of Form Data](../../tree/7f99ccd0f8fc3aab198a8d23d387474ff6c2961b)

Ver.31   [Django Crispy Forms](../../tree/c3df445bdf21261c7ee8d2c750bba767013cf577)

Ver.32   [Bootstrap Input Groups](../../tree/157325f976b84a244c39083499c1897928367ac0)

Ver.33   [Django Generic Foreign Keys](../../tree/9794c621797f0e3093672bc428a65d67a05fbd00)

Ver.34   [Model Managers & Instance Methods](../../tree/ebca367d62a050405fcb212ea8ed1354373dee25)

Ver.35   [Create Comments](../../tree/a03c5f6c61e35e815d0cda515df2a7b4cf8f4448)

Ver.36   [Reply to Comments](../../tree/46fd0a25443b2345c6f82986b5e77e69e1b6dc13)

Ver.37   [jQuery fadeToggle for Comment Replies](../../tree/b0d140d8e51c28266bacf241430c96985df854af)

Ver.38   [Comment Thread](../../tree/977e0f1926a492127cab7b5686c074e56f02e891)

Ver.39   [Count Words & Blog Post Read Time](../../tree/cf62599c10df88a2abee34fd36421375dccb2cde)

Ver.40   [Delete View with Confirmation & Permissions](../../tree/19a3d1d39dd1f00e64efa7f7e279d2067e93d20d)

Ver.41   [User Login, Registration, Logout Form & View](../../tree/efc000552b379a7d6b98a689518bf6ea652d5562)

Ver.42   [User Login Required](../../tree/1104468a14963c0ca6b336f8e87b90a1f483ba68)

Ver.43   [Breadcrumb Navigation](../../tree/347ae24abe05b842de3ad12dcabdb8f420423536)

**Ver.44   [v2.0](../../tree/v2.0)** _(Stable Ver.)_

Ver.45   [REST framework Installation](../../tree/862e24450a82382b1e730bfdc155fe8fb5d6c30d)

Ver.46   [Post List API View](../../tree/35f71e67f224f793d9aeef4894a8699ec1295a93)

Ver.47   [Post Update & Delete API View](../../tree/7863e7ee62d32297351ef3f2fcb89a51b98b72f6)

Ver.48   [Post Create API View](../../tree/8415ff1a747a70caaca90914a0cd60494e9a6496)

Ver.49   [Filtering a Queryset in a ListAPIView](../../tree/2ac5f079b74a4767eb03bd6a04d3f0adbb162f7f)

Ver.50   [Pagination in a ListAPIView](../../tree/73ad4bee59528f481cd540d05efeb3c92d7c2c8a)

Ver.51   [Serializer Method Field](../../tree/d37e8a12733ae7edf6cf5a1e8b97c696e2f25ba4)

Ver.52   [Comment API View](../../tree/e83696e604f0f9661c5291089b9a3e424af70853)

Ver.53   [Comment Children & Reply Count](../../tree/3045be78a95a84f0cd089a6aceca698f99568992)

Ver.54   [Comments in Post Detail API View](../../tree/ad794a507205988ec27372077b1ceb5cc5e78dea)

Ver.55   [Comment Create Serializer Function](../../tree/f9e76f3e85ca833ac1cff1e39eb771cc8a1604a8)

Ver.56   [Comment Update & Delete in Detail API](../../tree/86aa9969646fbb394dd3838a1e1912537c78d777)

Ver.57   [Comment URL for Generic Foreign Key & Post API Permissions Update](../../tree/07d46913985588334740ea32a74f404d46299063)

Ver.58   [User Register API](../../tree/5f3a273d01f5810cdef4f06c1de74e6791d3f804)

Ver.59   [User Detail Serializer](../../tree/bea4d2fccc9b37c354b2067498389d43a8822eda)

Ver.60   [API Home View](../../tree/bea4d2fccc9b37c354b2067498389d43a8822eda)

Curr. Ver.   Django Rest Framework JWT Authentication