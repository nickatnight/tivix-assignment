Installation
============

For contributors, installation is very easy. First, check to verify you are
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

Running ``fab deploy_local`` will run the test suite, open a webpage summarzing the code
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

Add ``"blog"`` and ``"crispy_forms"`` to your project's ``INSTALLED_APPS`` setting::

    INSTALLED_APPS = (
        ...
        'crispy_forms',
        'blog',
        ...
    )

Add associated URLS::

    url_patterns = patterns('',
        ...,
        url(r'^blog/', include("blog.urls", namespace='t-blog'))
    )

.. note:: We give a namespace to avoid url conflicts with other apps using the same named urls.


Everything is now set!

Development
-----------

Working with a team of developers to improve this application? If your team is
on Slack, you can easily add your webhook url and channel name to the fabfile.
Once ``fab deploy_local`` is ran, the user will be prompted to push to GitHub.
After entering the desired commit message, your code will be pushed and a
customized message will be sent to your message board. Just make sure to
uncomment the ``slacker(msg)`` routine in the fabfile::

    def git_sum(msg):
        # Textbook git commands
        local('git add .')
        local('git commit -m "'+msg+'"')
        local('git push origin master')

        slacker(msg) <----- Uncomment

