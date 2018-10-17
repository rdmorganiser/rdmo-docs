Domain
------

The domain model can be managed under *Domain* in the management menu in the navigation bar.

.. figure:: ../_static/img/screens/domain.png
   :target: ../_static/img/screens/domain.png

   Screenshot of the domain management interface.

After the installation of RDMO the domain is initially empty. Please import our domain available at https://github.com/rdmorganiser/rdmo-catalog . Afterwards you can extend the domain, but the domain is the core data model which guarantess interoperability and cooperativity amongst diverse RDMO instances and it is always the starting point to create questionaires.


On the left-hand side is the main display of all the attributes available in this installation of RDMO. The attributes display their path and if they are configured to be a collection. On the right side of each elements panel, icons indicate ways to interact the element. The following options are available:

* **Add** (|add|) a new attribute.
* **Update** (|update|) an attribute to change its properties.
* **Delete** (|delete|) an attribute and all of it's decendents. **The action will remove the attribute and all the attributes below. This action cannot be undone!**

.. |add| image:: ../_static/img/icons/add.png
.. |update| image:: ../_static/img/icons/update.png
.. |delete| image:: ../_static/img/icons/delete.png

The sidebar on the right-hand side shows additional interface items:

* **Filter** filters the view according to a user given string. Only elements containing this string in their path will be shown.
* **Options** offers additional operations:

  * Create a new (empty) attribute

* **Export** exports the current catalog to one of the displayed formats. While the textual formats are mainly for presentation purposes, the XML export can be used to transfer the domain model to a different installation of RDMO.

The different elements of the domain model have different properties to control their behavior. As descibed in :doc:`the introduction <index>`, all elements have an URI Prefix, a key, and an internal comment only to be seen by other managers of the RDMO installation. In addition, you can edit the parameters below:

Attribute
"""""""""
An Attribute can be value or parent.

If it is parent in the domain model changing it will move this parent and all of it's decendents to a different branch of the domain model tree. A question set connected to a parent attribute will show interface elements to create new sets of answers. All attributes in the tree below a collection attribute adopt this behavior, so that questions about the same set can be spread over several question sets on separate pages of the interview.

Both types hold an information set which consists of different atoms.

URI Prefix
    identifies the entity who created this element

Key
    is the internal identifier for this element

Comment
    internal comment to share information to be seen by users with access to the management backend

Parent attribute
    indicates the parent attribute
