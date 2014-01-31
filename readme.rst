JSLoad
======

Example:

    {% jsload "/widgets/receipt.js" 183.92 %}

JSLoad will take care of getting just the right ``<script>`` includes into the
HEAD of your template using the hideous ``${JS}`` sigil that you must include in
a base template somewhere.

django settings
---------------
* ``OKONOMI_STATIC_URL`` set this to whatever makes sense for your django project.
* ``OKONOMI_STATIC_PATH`` set this to whatever makes sense for your django project.
* ``OKONOMI_HTML_PATH_TEMPLATE`` defaults to ``<script type="text/javascript" src="%s"></script>\n``
* ``OKONOMI_HTML_URL_TEMPLATE`` defaults to ``<script type="text/javascript" src="%s"></script>\n``

Requirements
============

Locally hosted media
--------------------

* ${JS} sigil in HEAD or somewhere::

    {% jsrequire /formchecking.js %}

* add ``/formchecking.js`` to ``set()`` in context

... (repeat in various templates) ...

* middleware:
    * generate key from what is in the set()
    * not cached?
        * read all the js files, concat, cache

    * insert ``<script src="/js/cache_key"></script>`` for ``${JS}``


Remote hosted media
-------------------

* ``${JS}`` sigil in HEAD or somewhere::

    {% jsrequire https://ajax.googleapis.com/ajax/libs/jquery/1.6.4/jquery.js %}

* add url to set() in context

... (repeat in various templates) ...

* middleware:
    * insert ``<script src="url"></script>`` for each remote include

------------------------

Derek Anderson <derek.anderson@coxinc.com>  
Dan Cobb <dan.cobb@coxinc.com>  
for Cox Media Group Technology  
License: MIT
