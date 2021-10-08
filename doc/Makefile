# Minimal makefile for Sphinx documentation
#

# You can set these variables from the command line, and also
# from the environment for the first two.
SPHINXOPTS    ?=
SPHINXBUILD   ?= sphinx-build
SOURCEDIR      = source
BUILDDIR       = build
BUILDDIRDEV    = build/html
BUILDDIRSTABLE = build/html_stable

# Put it first so that "make" without argument is like "make help".
help:
	@$(SPHINXBUILD) -M help "$(SOURCEDIR)" "$(BUILDDIR)" $(SPHINXOPTS) $(O)

.PHONY: help Makefile

# Catch-all target: route all unknown targets to Sphinx using the new
# "make mode" option.  $(O) is meant as a shortcut for $(SPHINXOPTS).
%: Makefile
	@$(SPHINXBUILD) -M $@ "$(SOURCEDIR)" "$(BUILDDIRDEV)" $(SPHINXOPTS) $(O)

html-strict:
	$(SPHINXBUILD) -W -T -n -b html $(SOURCEDIR) $(BUILDDIRDEV) $(SPHINXOPTS)
	@echo
	@echo "Build finished. The HTML pages are in _build/html."

html:
	$(SPHINXBUILD) -T -n -b html $(SOURCEDIR) $(BUILDDIRDEV) $(SPHINXOPTS)
	@echo
	@echo "Build finished. The HTML pages are in _build/html."

html_dev-noplot:
	$(SPHINXBUILD) -D plot_gallery=0 -b html $(SOURCEDIR) $(BUILDDIRDEV) $(SPHINXOPTS)
	@echo
	@echo "Build finished. The HTML pages are in _build/html."

html_dev-pattern:
	$(SPHINXBUILD) -D sphinx_gallery_conf.filename_pattern=$(PATTERN) -D sphinx_gallery_conf.run_stale_examples=True -b html $(SOURCEDIR) $(BUILDDIRDEV) $(SPHINXOPTS)
	@echo
	@echo "Build finished. The HTML pages are in build/html"

clean:
	-rm -rf $(BUILDDIR)/*
	-rm -rf $(SOURCEDIR)/auto_examples/

install:
	rm -rf $(BUILDDIRDEV)/doctrees $(BUILDDIR)/toy_pkg.github.io
	git clone --no-checkout --depth 1 git@github.com:NicolasGensollen/toy_pkg.github.io.git $(BUILDDIR)/toy_pkg.github.io
	rm -Rf $(BUILDDIR)/toy_pkg.github.io/stable;
	mkdir $(BUILDDIR)/toy_pkg.github.io/stable;
	make html
	cd $(BUILDDIR) && \
	cp -r html/* toy_pkg.github.io/stable/ && \
	cd toy_pkg.github.io && \
	git add -A && \
	git commit -a -m 'Make install' && \
	git push
