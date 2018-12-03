# Export formats


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

The page style and different other format settings can be adjusted using reference documents. Since Pandoc is used for document conversion you can find an exhaustive list of supported settings on the [Pandoc manual page](https://pandoc.org/MANUAL.html) under the paragraph '--reference-doc'. Reference documents can be used for the export formats of `.docx` and `.odt`. This is achieved by defining reference documents in the `config/settings/local.py`. If these settings are not in your config default styles will be applied.

```python
EXPORT_REFERENCE_DOCX='FULL PATH OF YOUR REFERENCE DOCX'
EXPORT_REFERENCE_ODT='FULL PATH OF YOUR REFERENCE ODT'
```
