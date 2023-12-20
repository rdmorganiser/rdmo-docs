# Management user interface

Since Version 2.0, RDMO uses a general management interface. The page is accessible via the "Management" button in the navigation bar and will be empty after a fresh RDMO installation. We suggest to **first import our domain model** and, if you like, our general questionnaire. The corresponding XML-files that define the RDMO content are available and described at [rdmorganiser/rdmo-catalog](https://github.com/rdmorganiser/rdmo-catalog#rdmo-catalog).

![](../_static/img/screens/management.png)
> *Overview of the RDMO management interface*

Each content type in RDMO is referenced here as an element. Via the management interface an element can be selected and its available functions are displayed. The left-hand side shows the main display of the currently selected element. The panels represent individual items or entries for this element. On the right side in each panel, icons indicate ways to interact with this element. In general, the available interactions are listed below. However, some of the interactions are only available for specific elements.

* **Show a nested view** (![](../_static/img/icons/nested.png)) for the element and its related elements.
* **Edit** (![](../_static/img/icons/edit.png)) an element to change its properties.
* **Copy** (![](../_static/img/icons/copy.png)) an element.
* **Add** (![](../_static/img/icons/add.png)) a new (sub-)element to the element.
* **Toggle the availability** (![](../_static/img/icons/available.png)) of the element.
* **Lock/unlock** (![](../_static/img/icons/add.png)) the element.
* **Export** (![](../_static/img/icons/export.png)) an attribute and all of its descendants as XML.

At the top of the page, the items of an element can be filtered based on a **text string**, the **URI Prefix**. For multi site setups, the site and the sites which can edit the element can also be used as filters.

The sidebar on the right-hand side shows additional interface items:

* **Navigation** switches the type of element which is currently listed in the main parts.
* **Export** exports the current catalog to one of the displayed formats. While the textual formats are mainly for presentation purposes, the XML export can be used to transfer the domain model to a different instance of RDMO.
* **Import** can be used to import a RDMO import file with elements.
