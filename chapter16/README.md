Security
========

If you learn only one thing from this chapter, let it be this:

    Never – under any circumstances – trust data from the browser.

Django’s security features

Cross site scripting (XSS) protection
-------------------------------------

XSS attacks allow a user to inject client side scripts into the
browsers of other users.

Django templates escape specific characters which are particularly
dangerous to HTML.

Cross site request forgery (CSRF) protection
--------------------------------------------

CSRF attacks allow a malicious user to execute actions using the
credentials of another user without that user’s knowledge or consent.

Django has built-in protection against most types of CSRF attacks,
providing you have enabled and used it where appropriate.

SQL injection protection
------------------------

SQL injection is a type of attack where a malicious user is able
to execute arbitrary SQL code on a database. This can result in
records being deleted or data leakage.

By using Django’s querysets, the resulting SQL will be properly
escaped by the underlying database driver.

Clickjacking protection
-----------------------

Clickjacking is a type of attack where a malicious site wraps another
site in a frame. This attack can result in an unsuspecting user being
tricked into performing unintended actions on the target site.

Django contains clickjacking protection in the form of the X-Frame-Options
middleware which in a supporting browser can prevent a site from being
rendered inside a frame.

SSL/HTTPS
---------

It is always better for security.

Host header validation
----------------------

ALLOWED_HOSTS

User-uploaded content
---------------------

Consider serving static files from a cloud service or CDN to avoid some
of these issues.

- If your site accepts file uploads, it is strongly advised that you limit
  these uploads in your Web server configuration to a reasonable size in
  order to prevent denial of service (DOS) attacks.

- If you are serving your own static files, be sure that handlers like
  Apache’s mod_php, which would execute static files as code, are disabled.

- Django’s media upload handling poses some vulnerabilities when that media
  is served in ways that do not follow security best practices. Specifically,
  an HTML file can be uploaded as an image if that file contains a valid PNG
  header followed by malicious HTML. This file will pass verification of the
  libraries that Django uses for ImageField image processing (PIL or Pillow).
  When this file is subsequently displayed to a user, it may be displayed as
  HTML depending on the type and configuration of your web server.

        No bulletproof technical solution exists at the framework level to
        safely validate all user uploaded file content, however, there are
        some other steps you can take to mitigate these attacks:

        - One class of attacks can be prevented by always serving user
          uploaded content from a distinct top-level or second-level domain.
          This prevents any exploit blocked by same-origin policy protections
          such as cross site scripting.

        - Beyond this, applications may choose to define a whitelist of
          allowable file extensions for user uploaded files and configure the
          web server to only serve such files.
