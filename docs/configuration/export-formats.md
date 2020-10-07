# Export Formats

RDMO supports exports to certain formats using the excellent [Pandoc](https://pandoc.org/) converter. The list of formats to select can be customized by changing the `EXPORT_FORMATS` setting in your `config/settings/local.py`.

```python
EXPORT_FORMATS = (
    ('pdf', _('PDF')),
    ('rtf', _('Rich Text Format')),
    ('odt', _('Open Office')),
    ('docx', _('Microsoft Office')),
    ('html', _('HTML')),
    ('markdown', _('Markdown')),
    ('mediawiki', _('mediawiki')),
    ('tex', _('LaTeX'))
)
```

The different formats supported by Pandoc can be found on the [Pandoc homepage](https://pandoc.org/).

## General Reference Documents

The page style and different other format settings can be adjusted using reference documents. Since Pandoc is used for document conversion you can find an exhaustive list of supported settings on the [Pandoc manual page](https://pandoc.org/MANUAL.html) under the paragraph '--reference-doc'. Reference documents can be used for the export formats of `.docx` and `.odt`. This is achieved by defining reference documents in the `config/settings/local.py`. If these settings are not in your config default styles will be applied.

```python
EXPORT_REFERENCE_DOCX = 'FULL PATH OF YOUR REFERENCE DOCX'
EXPORT_REFERENCE_ODT = 'FULL PATH OF YOUR REFERENCE ODT'
```

## View Specific Reference Documents

RDMO also allows to define reference documents depending on the view used to render the output. This can be achieved by adding one or both of the following dictionaries into the `local.py`. There is one dictionary per export document type. They basically consist of a key value store. The key is supposed to be the `view uri` and the value is the `path to the document`.

```python
EXPORT_REFERENCE_ODT_VIEWS = {
    'https://rdmorganiser.github.io/terms/views/horizon2020': 'FULL PATH OF YOUR REFERENCE ODT',
    'https://rdmorganiser.github.io/terms/views/dmponline': 'FULL PATH OF YOUR REFERENCE ODT'
}

EXPORT_REFERENCE_DOCX_VIEWS = {
    'https://rdmorganiser.github.io/terms/views/horizon2020': 'FULL PATH OF YOUR REFERENCE DOCX',
    'https://rdmorganiser.github.io/terms/views/dmponline': 'FULL PATH OF YOUR REFERENCE ODT'
}
```

Feel free to use all the above mentioned entries in your config. If you have multiple settings the following lookup logic applies.

The view dictionary has the highest priority. Its reference documents are taken first if they exist. If there are no reference documents for the specific view the general, reference document settings apply. If these or the files defined do not exist RDMO's default reference document will be taken.
