# Dutch class materials — task runner.
#
# This is a personal teaching archive, not a software project. The Makefile
# only wraps the repetitive regenerate steps (docx export, email generation)
# and a consistency check, so the new-quarter runbook can say "make docx"
# instead of pasting pandoc loops. See docs/new-quarter.md.

PANDOC := pandoc
PYTHON := python3

# Each entry maps a source markdown directory to its docx output directory.
# Adding a new handout category? Add a line here and a target below.
HANDOUT_SRC   := $(wildcard handouts/s*.md)
TEST_SRC      := $(wildcard handouts/tests/*.md)
TEACHER_SRC   := $(wildcard handouts/teacher/*.md)
STUDENTQ_SRC  := $(wildcard handouts/teacher/student-questions/*.md)
REF_SRC       := $(wildcard handouts/references/reference-*.md)

.DEFAULT_GOAL := help

.PHONY: help docx docx-handouts docx-tests docx-teacher docx-studentq docx-refs emails check clean-docx

help: ## Show this help
	@echo "Dutch class materials — available targets:"
	@grep -E '^[a-zA-Z_-]+:.*## ' $(MAKEFILE_LIST) \
		| awk -F':.*## ' '{printf "  \033[36m%-16s\033[0m %s\n", $$1, $$2}'

docx: docx-handouts docx-tests docx-teacher docx-studentq docx-refs ## Regenerate every docx (gitignored output)

docx-handouts: ## Session handouts -> handouts/docx/
	@mkdir -p handouts/docx
	@$(foreach f,$(HANDOUT_SRC),$(PANDOC) "$(f)" -o "handouts/docx/$(notdir $(f:.md=.docx))" &&) true
	@echo "  handouts: $(words $(HANDOUT_SRC)) file(s)"

docx-tests: ## Tests -> handouts/docx/tests/
	@mkdir -p handouts/docx/tests
	@$(foreach f,$(TEST_SRC),$(PANDOC) "$(f)" -o "handouts/docx/tests/$(notdir $(f:.md=.docx))" &&) true
	@echo "  tests: $(words $(TEST_SRC)) file(s)"

docx-teacher: ## Teacher materials -> handouts/docx/teacher/
	@mkdir -p handouts/docx/teacher
	@$(foreach f,$(TEACHER_SRC),$(PANDOC) "$(f)" -o "handouts/docx/teacher/$(notdir $(f:.md=.docx))" &&) true
	@echo "  teacher: $(words $(TEACHER_SRC)) file(s)"

docx-studentq: ## Student-question sheets -> handouts/docx/teacher/student-questions/
	@mkdir -p handouts/docx/teacher/student-questions
	@$(foreach f,$(STUDENTQ_SRC),$(PANDOC) "$(f)" -o "handouts/docx/teacher/student-questions/$(notdir $(f:.md=.docx))" &&) true
	@echo "  student-questions: $(words $(STUDENTQ_SRC)) file(s)"

docx-refs: ## Reference sheets -> handouts/docx/references/
	@mkdir -p handouts/docx/references
	@$(foreach f,$(REF_SRC),$(PANDOC) "$(f)" -o "handouts/docx/references/$(notdir $(f:.md=.docx))" &&) true
	@echo "  references: $(words $(REF_SRC)) file(s)"

emails: ## Regenerate pre-class emails from emails/_generate.py
	$(PYTHON) emails/_generate.py

check: ## Check email/schedule date drift and handout/README rename drift
	@$(PYTHON) scripts/check_consistency.py

clean-docx: ## Remove all generated docx (they are gitignored)
	rm -rf handouts/docx/*.docx handouts/docx/tests handouts/docx/teacher handouts/docx/references
