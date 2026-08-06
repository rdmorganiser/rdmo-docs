# You can set these variables from the command line.
SPHINXOPTS    =
SPHINXBUILD   = sphinx-build
SPHINXPROJ    = rdmo-docs-en
SOURCEDIR     = docs
BUILDDIR      = _build

# Put it first so that "make" without argument is like "make help".
help:
	@$(SPHINXBUILD) -M help "$(SOURCEDIR)" "$(BUILDDIR)" $(SPHINXOPTS) $(O)

live:
	sphinx-autobuild --port 8001 -b html $(SPHINXOPTS) $(SOURCEDIR) $(BUILDDIR)/html

settings:
	python3 tools/generate_settings_reference.py

check-settings:
	python3 tools/generate_settings_reference.py --check

.PHONY: help live settings check-settings Makefile

# Catch-all target: route all unknown targets to Sphinx using the new
# "make mode" option.  $(O) is meant as a shortcut for $(SPHINXOPTS).
%: Makefile
	@$(SPHINXBUILD) -M $@ "$(SOURCEDIR)" "$(BUILDDIR)" $(SPHINXOPTS) $(O)
