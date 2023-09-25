# Export and Import

RDMO offers export and import functions which are available in the right handed sidebar. The two categories offering the equally named functions do appear for every datatype (e.g. Questions, Domain, etc.). Note that these functions are context sensitive. If you for example use the `Export` or `Import` being in `Tasks` you can only ex- or import `Tasks`. This is especially important to know for the import, because it will fail and display an error if you pick an xml file that does not contain fitting content.

## Export

The export menu is displayed on the right-hand side of the screen. It consists of a list of the supported export formats which may vary depending on what page you are on. For information about how to configure the available export formats see [here](../configuration/export-formats).

## Import

As mentioned above, the import is context sensitive. It will only run if you select an xml file that fits to the page you are on and contains valid xml data. If the file is invalid or you accidentally picked a wrong document type, the parser will become aware of it and simply skip any import function. This will simply reload the page without any change of data.

You can select the file to import by clicking the `select xml file` text or by dragging and dropping your file onto the box containing the mentioned text.

A Project import will always create a new Project holding the imported data. *Note that for all other types (Options, Tasks, etc.) data already existing in your RDMO installation will be overwritten during an import.* The URI acts as identifier. If you import an element that equals the URI of an already existing one, the import will overwrite.
