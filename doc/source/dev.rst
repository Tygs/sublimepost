Setup a CI instance
===================

We use `BuildBot <http://buildbot.net>`_ as CI tool, but since it’s only
python2.7 compatible and SublimePost requires python3.5, you need a separate
virtualenv.

For example, there is the commands required to install and deploy a Buildbot
instance on a Linux workspace:

::

    git clone git://github.com/Tygs/sublimepost.git
    python3.5 -m venv -p python2.7 sublimepost-ci-venv
    source sublimepost-ci-venv/bin/activate
    cd sublimepost/tests/ci/
    pip install -r requirements.txt
    buildbot start master
    buildslave start slave

Now open a web browser to `<http://localhost:8010>`_.

Build documentation
===================

::
    git clone git://github.com/Tygs/sublimepost.git
    python3.5 -m venv sublimepost-doc-venv
    source sublimepost-doc-venv/bin/activate
    pip install sphinx
    cd sublimepost/doc
    sphinx-build -b html source build

Run tests
=========

::
    git clone git://github.com/Tygs/sublimepost.git
    python3.5 -m venv sublimepost-doc-venv
    source sublimepost-doc-venv/bin/activate
    pip install .[dev]
    tox



Style Guide
=============

 - Python: PEP8 (https://www.python.org/dev/peps/pep-0008/)
 - JS: Google (http://google-styleguide.googlecode.com/svn/trunk/javascriptguide.xml)