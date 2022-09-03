==================
Github API Crawler
==================


.. image:: https://img.shields.io/pypi/v/github_api_crawler.svg
        :target: https://pypi.python.org/pypi/github_api_crawler

.. image:: https://img.shields.io/travis/Carabinr/github-api-crawler.svg
        :target: https://travis-ci.com/Carabinr/github-api-crawler

.. image:: https://readthedocs.org/projects/github-api-crawler/badge/?version=latest
        :target: https://github-api-crawler.readthedocs.io/en/latest/?version=latest
        :alt: Documentation Status




A robust and scalable API client to crawl github politely and within the limits


* Free software: MIT license
* Documentation: https://github-api-crawler.readthedocs.io.


Features
--------

* Clustered crawling with redis as stateful cache (optional)
* Single crawler cache uses memory-only (no requirements)
* Easily more caching backends
* Graceful error handling with custom Exception classes
* Fully typed method calls for better return type and function param checking

Wishlist
--------

* Proxy rotation
* API Key rotation

Credits
-------

This package was created with Cookiecutter_ and the `audreyr/cookiecutter-pypackage`_ project template.

.. _Cookiecutter: https://github.com/audreyr/cookiecutter
.. _`audreyr/cookiecutter-pypackage`: https://github.com/audreyr/cookiecutter-pypackage
