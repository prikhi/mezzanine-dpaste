==========
MezzPaste
==========


MezzPaste is a `Mezzanine`_ app that integrates the Django pastebin `dpaste`_
into the Mezzanine framework.


Usage
======

First follow the `dpaste instructions`_ for integrating dpaste into an existing
Django project.

Then install this package using ``pip``::

    pip install mezzanine-mezz

Add the package to your ``INSTALLED_APPS``, above the ``dpaste`` app::

    INSTALLED_APPS = (
        # ...

        'mezzpaste',
        'dpaste',
    )

To enable syntax highlighting, generate a pygments CSS file and include it in
your ``base.html``::

    pygmentize -S default -f html -a highlight > pygments.css


If you want to include a link in a Navigation menu, create a RichTextPage in
Mezzanine with the same URL as the dpaste URL you added to urls.py.

For example, if you added ``('^pastes/', include('dpaste.urls'))`` to your base
``urls.py``, you would need to create a RichTextPage with the name ``Pastes``.
If instead you added ``('^foo/pastes/', include('dpaste.urls'))``, you would
create a ``Pastes`` page under a ``Foo`` page.

.. _dpaste: https://github.com/bartTC/dpaste
.. _dpaste instructions: http://dpaste.readthedocs.org/en/latest/integration.html
.. _Mezzanine: http://mezzanine.jupo.org/
