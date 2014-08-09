Middleware
==========

Middleware is a framework of hooks into Django’s request/response
processing. It’s a light, low-level “plugin” system for globally
altering Django’s input or output.

Middlewares we already known
----------------------------

Cache middleware

- UpdateCacheMiddleware
- FetchFromCacheMiddleware

“Common” middleware

- DISALLOWED_USER_AGENTS
- APPEND_SLASH and PREPEND_WWW
- USE_ETAGS: Not Modified
- BrokenLinkEmailsMiddleware: MANAGERS

Message middleware

Session middleware

Authentication middleware

CSRF protection middleware

Other built-in middlewares
--------------------------

GZip middleware

Conditional GET middleware

Locale middleware

X-Frame-Options middleware

Hooks and application order
---------------------------

![middleware.svg](https://docs.djangoproject.com/en/1.6/_images/middleware.svg)

process_request

process_view

process_exception

process_template_response

process_response

Example
-------