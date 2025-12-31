# Change Log
All notable changes to this project will be documented in this file.

## [v3.0] - 2025-12-31
### Added
- [Rest Framework](http://www.django-rest-framework.org/) & [Simple JWT](https://github.com/jazzband/djangorestframework-simplejwt) support.
- User register API.
- JSON Web Token (JWT) Authentication APIs.
- Post APIs for [CRUD](https://en.wikipedia.org/wiki/Create,_read,_update_and_delete) actions to access data.
- Comment APIs, supporting CRUD operations on both posts' comment & comments' reply

### Changed
- Major upgrade to Django 5.2 and Python 3
- Fix some small bugs related to compatibility.

## [v2.0] - 2016-07-31
### Added
- Markdown content support, including editing and rendering function.
- User account authentication support, including login, register & logout features.
- Custom comment system, support anonymous comments and single thread retrieval/deletion.

### Changed
- Forms styles improvement with Crispy-forms

### Removed
- Facebook commenting system.

## v1.0 - 2016-04-12
### Added
- Add, retrieve, update & delete posts for staff user.
- Responsive feature image for post
- Search post contents.
- Bootstrap styles implementation.
- Draft & publish date support.
- Facebook commenting system.
- Share post to Facebook friends.

[v2.0]: https://github.com/loafbaker/django_blog/compare/v1.0...v2.0