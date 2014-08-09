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

GZip middleware: Compresses content for browsers that understand GZip.

Conditional GET middleware

    If the response has a *ETag* or *Last-Modified* header, and the
    request has *If-None-Match* or *If-Modified-Since*, the response
    is replaced by an HttpResponseNotModified.

    Also sets the Date and Content-Length response-headers.

Locale middleware: Enables language selection based on data from the request.

X-Frame-Options middleware: Clickjacking Protection

Hooks and application order
---------------------------

![middleware.svg](https://docs.djangoproject.com/en/1.6/_images/middleware.svg)

process_request(request)

    It should return None or an HttpResponse object.

process_view(request, view_function, view_args, view_kwargs)

    It should return None or an HttpResponse object.

process_template_response(request, response)

    process_template_response() is called just after the view has
    finished executing, if the response instance has a render()
    method, indicating that it is a TemplateResponse or equivalent.

    It must return a response object that implements a render method.

process_response(request, response)

    Unlike the process_request() and process_view() methods, the
    process_response() method is always called, even if the
    process_request() and process_view() methods of the same middleware
    class were skipped (because an earlier middleware method returned an
    HttpResponse). In particular, this means that your process_response()
    method cannot rely on setup done in process_request().

    Finally, remember that during the response phase, middleware are
    applied in reverse order, from the bottom up. This means classes
    defined at the end of MIDDLEWARE_CLASSES will be run first.

process_exception(request, exception)

     when a view raises an exception.

     return either None or an HttpResponse object.

Example
-------