Installation
============

For developers, installation is very easy. First, check to verify you are
running Python 2.7.::

    python -V

Next, verify pip is installed.::

    pip -V

Lastly, check to make sure you have git installed.::

    git --version

Cloning the repo and running the dev server is just as easy.::

    git clone https://github.com/nickatnight/tivix-assignment.git && cd tivix-assignment
    pip install -r requirements.txt
    fab deploy_local

Running fab_deploy will run the test suite, open a webpage summarzing the code
coverage, and start the dev server.

Dependencies
------------

* Django >= 1.8.13
* Pillow >= 3.2.0
* Fabric >= 1.11.1
* django-crispy-forms >= 1.6.0
* coverage >= 4.0.3


Configuration
-------------

Add ``"blog"`` to you project's ``INSTALLED_APPS`` setting::

    INSTALLED_APPS = (
        ...
        'blog',
        ...
    )

Add associated URLS::

    url_patterns = patterns('',
        ...,
        url(r'^blog/', include("blog.urls", namespace='t-blog'))
    )

Note: We give a namespace to avoid url conflicts with other apps using the same
named url.


Everything is now set!
