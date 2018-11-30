Questions
---------

The questions management is available under *Questions* in the management menu in the navigation bar. This page will be empty after a fresh RDMo installation. We suggest to **first import our domain model** and, if you like, our general questionaire. The corresponding XML-files are available at https://github.com/rdmorganiser/rdmo-catalog.

If there is at least one questionaire imported, it will be shown automatically. Other catalogs can be selected in the sidebar on the right-hand side afterwards.

.. figure:: ../_static/img/screens/questions.png
   :target: ../_static/img/screens/questions.png

   Screenshot of the questions management interface.

On the left-hand side is the main display of sections, questionsets, and questions for the current catalog. For sections and questionsets the title and the key is shown. For questions and question set the key and the key of the attribute they are connected to is shown. The order of the different elements is the same as in the structured interview shown to the user. On the right side of each elements panel, icons indicate ways to interact the element. The following options are available:

* **Add** (|add|) a new section, a new questionset, or a new question.
* **Update** (|update|) an element to change its properties.
* **Copy** (|copy|) a question or questionset. This will open the same modal as update. You can change some of the properties and save the elememt as a new one. This can save time when creating several similar questions.
* **Delete** (|delete|) an element and all of it's decendents (e.g. a question set and all the questions it contains). **This action cannot be undone!**

.. |add| image:: ../_static/img/icons/add.png
.. |update| image:: ../_static/img/icons/update.png
.. |copy| image:: ../_static/img/icons/copy.png
.. |delete| image:: ../_static/img/icons/delete.png

The sidebar on the right-hand side shows additional interface items:

* **Catalog** switches the view to a different Catalog.
* **Filter** filters the view according to a user given string. Only elements containg this string in their ``path`` will be shown.
* **Options** offers additional operations:

  * Update the details of the current catalog
  * Delete the current catalog
  * Create a new (empty) catalog
  * Create a new (empty) section
  * Create a new (empty) subsection
  * Create a new (empty) question set
  * Create a new (empty) question

* **Export** exports the current catalog to one of the displayed formats. While the text based formats are mainly for showing the full catalog, the XML export can be used to transfer this catalog to a different installation of RDMO.

The different elements of the questionaire have different properties to control their behavior. As descibed in :doc:`the introduction <index>`, all elements have an URI Prefix, a key, and an internal comment only to be seen by other managers of the RDMO installation. In addition, you can edit the parameters below:


Catalog
"""""""

Order
  Controls the position of the catalog in lists or in the interview.

Title (en)
  The English title for the catalog to be displayed to the user.

Title (de)
  The German title for the catalog to be displayed to the user.

Section
"""""""

Catalog
  The catalog this section belongs to. Changing the catalog will move the section to a different catalog. Therefore it will not be visible in the current view anymore.

Order
  Controls the position of the section in lists or in the interview.

Title (en)
  The English title for the section to be displayed to the user.

Title (de)
  The German title for the section to be displayed to the user.


Question sets
"""""""""""""

Tab General
  Section
    The section this question set belongs to. Changing the section will move the question set into another section.

  Order
    Controls the position of the question set in lists or in the interview.

  Attribute
    Indicates the attribute that the questionset is connected to. Only used, if **Is collection** is activated.

  Is collection
    Designates whether this question set allows for seperate answers for different sets (e.g. datasets, project partners).

Tab English


  Help
    The English help text for the question. The help text will be shown in grey to the user.

  Name
    The English name displayed for the sets, if **Is collection** is activated (e.g. dataset).

  Plural name
    English plural name displayed for the sets, if **Is collection** is activated (e.g. datasets).

*The "German" tab contains the same elements as the English one but obviously for German language content.*

Tab Conditions
  Conditions
    Displays the conditions of the question set. If **all** select ted Conditions evaluate negative, the question set is skipped in the Interview.


Questions
"""""""""

Tab General
  Question set
    The question set this question belongs to. Changing the question set will move the question into another question set.

  Order
    Controls the position of the question in lists or in the interview.

  Attribute
    The attribute from the domain model this question is connected to. The answers of the users will be connected to this attribute in the database and tasks and views reference answers using their attribute.

  Is collection
    Designates whether this question allows for multiple answers. In this case additional interface elements are added to the interview to add or remove answers.

  Widget type
    The type of widget for the question. The following widgets can be selected:

    * **Text** (a one line text field)
    * **Textarea** (a multi-line text field)
    * **Yes/No** (a set of radio buttons for "Yes" and "No")
    * **Checkboxes** (a set of check boxes, the connected attribute needs to be a collection)
    * **Radio Buttons** (a set of radio buttons, the connected attribute needs to have an option set)
    * **Select drop down** (a drop down menu, the connected attribute needs to have an option set)
    * **Range slider** (a horizontal slider, the connected attribute needs to have a range)
    * **Date picker** (a drop down element with a calender to select a date, the connected attribute needs to have the value type datetime)

  Value Type
    Type of value for this attribute. The following types can be selected:
    Text, URL, Integer, Float, Boolean, Datetime, Options

  Unit
    Unit for this attribute. The unit will be displayed in the different output features.

Tab English
  Text
    The English text for the question. The text will be shown in bold face to the user.

  Help
    The English help text for the question. The help text will be shown in grey to the user.

  Name
    The English name displayed for different answers when **Is collection** is selected (e.g. item).

  Plural name
    English plural name displayed for different answers when **Is collection** is selected (e.g. items).

*The "German" tab contains the same elements as the English one but obviously for German language content.*

Tab Option sets and conditions
  Option sets
    Displays the option sets of the question set. For the **Widget-Type** Checkboxes, Radio Buttons, and Select drop down the opption sets contain the possiple options for the answer.

  Conditions
    Displays the conditions of the question. This has currently no effect, but may be used in the future.

Tab Range
  Maximum
    Maximum value for the answer of this question, when using the **Widget-Type** Range-Slider.

  Minimum
    Minimum value for the answer of this question, when using the **Widget-Type** Range-Slider.

  Step
    Step in which the value of the answer can be incremented or decremented, when using the **Widget-Type** Range-Slider.
