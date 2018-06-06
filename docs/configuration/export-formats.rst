Export formats
--------------

RDMO supports exports to certain formats using the excellent `pandoc <https://pandoc.org/>`_ converter. The list of formats to select can be customized by changing the ``EXPORT_FORMATS`` setting in your ``config/settings/local.py``.

.. code:: python

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

The different formats supported by pandoc can be found `on the pandoc homepage <https://pandoc.org/>`_.

For the export formats of .docx and .odt custom styles can be applied. This is achieved by defining reference documents in the ``config/settings/local.py``.

.. code:: python

    EXPORT_REFERENCE_DOCX='FULL PATH OF YOUR REFERENCE DOCX'
    EXPORT_REFERENCE_ODT='FULL PATH OF YOUR REFERENCE ODT'

The page style and different other format settings can be adjusted. Since pandoc is used for document conversion you can find an exhaustive list of supported settings at the `pandoc manual page <https://pandoc.org/MANUAL.html>`_ under the paragraph '--reference-doc'.
