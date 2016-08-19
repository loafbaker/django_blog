# Change Log
All notable changes to this project will be documented in this file.

## [Unreleased]
### Added
- [Rest Framework](http://www.django-rest-framework.org/) & [Rest Framework JWT](https://github.com/GetBlimp/django-rest-framework-jwt) support.
- User register API.
- JSON Web Token (JWT) Authentication APIs.
- Post APIs for [CRUD](https://en.wikipedia.org/wiki/Create,_read,_update_and_delete) actions to access data.
- Comment APIs, supporting CRUD operations on both posts' comment & comments' reply

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