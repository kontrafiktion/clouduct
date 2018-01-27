SUPPORTED_SHELLS := bash zsh

completion_files := $(foreach shell_name, ${SUPPORTED_SHELLS}, completion/${shell_name}.complete)



.PHONY: dist completion prepare-dist clean lint

# create a shell completion file for a given shell (see SUPPORTED_SHELLS)
completion/%.complete: bin/clouduct completion/
	PATH=$$PWD/bin:$$PATH _CLOUDUCT_COMPLETE=source-$* clouduct  > $@

clean:
	rm -rf completion
	rm -rf dist

dist: clean prepare-dist
	python setup.py sdist

lint:
	flake8 clouduct bin/clouduct

prepare-dist:  completion/ ${completion_files} lint

completion/:
	mkdir completion