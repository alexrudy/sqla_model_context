==============================
Model Relative Context Manager
==============================


.. image:: https://img.shields.io/pypi/v/sqla_model_context.svg
        :target: https://pypi.python.org/pypi/sqla_model_context

.. image:: https://github.com/alexrudy/sqla_model_context/workflows/CI/badge.svg
        :target: https://github.com/alexrudy/sqla_model_context/workflows/CI/

.. image:: https://readthedocs.org/projects/sqla-model-context/badge/?version=latest
        :target: https://sqla-model-context.readthedocs.io/en/latest/?badge=latest
        :alt: Documentation Status




Context manager for default relationship values in SQLAlchemy


* Free software: MIT license
* Documentation: https://sqla-model-context.readthedocs.io.

This is primarily a way to ensure that common relationships (e.g. user_id on lots of user generated content) are easy
to set via the SQLAlchemy context. It works well in concert with flask_login, where it allows you to leverage flask_login's
`current_user` to set a default relationship value. See the examples directory for a small usage example.


Credits
-------

This package was created with Cookiecutter_ and the `audreyr/cookiecutter-pypackage`_ project template.

.. _Cookiecutter: https://github.com/audreyr/cookiecutter
.. _`audreyr/cookiecutter-pypackage`: https://github.com/audreyr/cookiecutter-pypackage
