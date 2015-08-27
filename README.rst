=========================
Mako Templates for Python
=========================

:Version: |version|
:Travis CI: |travis|
:Appveyor: |appveyor|

.. |version| image:: https://img.shields.io/pypi/v/Mako.png
        :target: https://pypi.python.org/pypi/Mako

.. |travis| image:: https://img.shields.io/travis/zzzeek/mako.png
        :target: https://travis-ci.org/zzzeek/mako

.. |appveyor| image:: https://img.shields.io/appveyor/ci/zzzeek/mako.png
        :target: https://ci.appveyor.com/project/zzzeek/mako/branch/master

     
Mako is a template library written in Python. It provides a familiar, non-XML 
syntax which compiles into Python modules for maximum performance. Mako's 
syntax and API borrows from the best ideas of many others, including Django
templates, Cheetah, Myghty, and Genshi. Conceptually, Mako is an embedded 
Python (i.e. Python Server Page) language, which refines the familiar ideas
of componentized layout and inheritance to produce one of the most 
straightforward and flexible models available, while also maintaining close 
ties to Python calling and scoping semantics.

Nutshell
========

::

    <%inherit file="base.html"/>
    <%
        rows = [[v for v in range(0,10)] for row in range(0,10)]
    %>
    <table>
        % for row in rows:
            ${makerow(row)}
        % endfor
    </table>

    <%def name="makerow(row)">
        <tr>
        % for name in row:
            <td>${name}</td>\
        % endfor
        </tr>
    </%def>

Philosophy
===========

Python is a great scripting language. Don't reinvent the wheel...your templates can handle it !

Documentation
==============

See documentation for Mako at http://www.makotemplates.org/docs/

License
========

Mako is licensed under an MIT-style license (see LICENSE).
Other incorporated projects may be licensed under different licenses.
All licenses allow for non-commercial and commercial use.
