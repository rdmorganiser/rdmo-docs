# Domain

The domain model can be managed under *Domain* in the management menu in the navigation bar.

After the installation of RDMO the domain is initially empty. **We suggest that all RDMO operators initially import the domain model provided by the RDMO project.** Using a common domain over all RDMO instances allows us to exchange questionaires, views and other content, and could lead to a common metadata application profile for data management planning. Our domain is available at https://github.com/rdmorganiser/rdmo-catalog. The domain is meant to be extendable, but the core data model enables interoperability and cooperativity amongst RDMO instances and it is a good starting point to create questionaires.

```eval_rst
.. figure:: ../_static/img/screens/domain.png
   :target: ../_static/img/screens/domain.png

   Screenshot of the domain management interface.
```

On the left-hand side is the main display of all the attributes available in this installation of RDMO. On the right side of each elements panel, icons indicate ways to interact the element. The following options are available:

* **Add** (![](/_static/img/icons/add.png)) a new attribute.
* **Update** (![](/_static/img/icons/update.png)) an attribute to change its properties.
* **Delete** (![](/_static/img/icons/delete.png)) an attribute and all of it's decendents. **The action will remove the attribute and all the attributes below. This action cannot be undone!**

The sidebar on the right-hand side shows additional interface items:

* **Filter** filters the view according to a user given string. Only elements containing this string in their path will be shown.
* **Options** offers additional operations:

  * Create a new (empty) attribute

* **Export** exports the current catalog to one of the displayed formats. While the textual formats are mainly for presentation purposes, the XML export can be used to transfer the domain model to a different installation of RDMO.

The different elements of the domain model have different properties to control their behavior. As descibed in [the introduction](/index.html), all elements have an URI Prefix, a key, and an internal comment only to be seen by other managers of the RDMO installation. In addition, you can edit the parameters below:

## Parameters

### Parent attribute
Indicates the parent attribute in the domain model.
