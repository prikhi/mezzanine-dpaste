==========
MezzPaste
==========


MezzPaste is a `Mezzanine`_ app that integrates the Django pastebin `dpaste`_
into the Mezzanine framework.


Usage
======

First install the package and dependencies using ``pip``::

    pip install mptt dpaste mezzanine-dpaste

Add the packages to your ``INSTALLED_APPS``, it is important to list
``mezzpaste`` above the ``dpaste`` app::

    INSTALLED_APPS = (
        # ...

        'mptt',
        'mezzpaste',
        'dpaste',
    )

Include the ``mezzpaste.urls`` in your Mezzanine project's ``urls.py``, above
the ``mezzanine.urls`` include::

    urlpatterns += patterns('',
        ("^pastes/", include('mezzpaste.urls'))
        ("^", include("mezzanine.urls")),
    )

Add a cron job to purge expired pastes::

    30 * * * * /path/to/virtualenv/bin/python /path/to/project/manage.py cleanup_snippets > /dev/null

To enable syntax highlighting, generate a pygments CSS file and include it in
your ``base.html``::

    pygmentize -S default -f html -a highlight > pygments.css

If you want to include a link in a Navigation menu, create a Page in Mezzanine
with the same URL as the mezzpaste URL you added to your project's ``urls.py``.

For additional configuration settings, see the `dpaste Documentation`_.

.. _dpaste: https://github.com/bartTC/dpaste
.. _dpaste Documentation: http://dpaste.readthedocs.org/en/latest/settings.html
.. _Mezzanine: http://mezzanine.jupo.org/
