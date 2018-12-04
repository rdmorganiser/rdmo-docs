# Options

Options and option sets can be managed under *Options* in the management menu in the navigation bar.

![](../../_static/img/screens/options.png)
> *Screenshot of the options management interface*

On the left-hand side is the main display of all the option sets and options available in this installation of RDMO. Option sets show their key, while options show their path and their text. On the right side of each elements panel, icons indicate ways to interact the element. The following options are available:

* **Add** (![](../../_static/img/icons/add.png)) a new option to an option set.
* **Update** (![](../../_static/img/icons/update.png) an option set or option to change its properties.
* **Update conditions** (![](../../_static/img/icons/conditions.png)) of an option set. A question connected to an option set with one or more conditions, will not show the options of the set in the questionaire, if the condition is evaluated to be false. The conditions themselves are configured in [the conditions management](../../management/conditions.html).
* **Delete** (![](../../_static/img/icons/delete.png)) an option set or option and, in the case of an option set, all of it's options. **This action cannot be undone!**

The sidebar on the right shows additional interface items:

* **Filter** filters the view according to a user given string. Only elements containing this string in their path will be shown.
* **Options** offers additional operations:

  * Create a new (empty) option set
  * Create a new (empty) option

* **Export** exports the options sets to one of the displayed formats. While the textual formats are mainly for presentation purposes, the XML export can be used to transfer the options sets to a different installation of RDMO.

Option sets and options model have different properties to control their behavior. As descibed in [the introduction](../../index.html), all elements have an URI Prefix, a key, and an internal comment only to be seen by other managers of the RDMO installation. In addition, you can edit the parameters below:

## Parameters
### Option set

|Name|Explanation|
|-|-|
|Order|Controls the position of the option set in lists or in the<br>interview (if an attribute has more than one option set)|

### Option

|Name|Explanation|
|-|-|
|Option set|The option set this option belongs to. Changing the<br>option set will move the option to a different option set
|Order|Controls the position of the option in lists or in the interview
|Text (en)|The English text for the option to be displayed to the user
|Text (de)|The German text for the option to be displayed to the user
|Additional input|Designates whether an additional input is possible for this<br>option. In this case a text box is displayed to the radio button<br>or check box. Usually this is used for an option "Other".
