SRC = src
TEST = test
TEST_CMD = py.test
LINT = pre-commit

.PHONY: test clean

install:
	pip install -rrequirements.txt
	$(LINT) install

lint:
	$(LINT) run --all-files

test:
	$(TEST_CMD)

verbose:
	$(TEST_CMD) -v

print:
	$(TEST_CMD) -s

nuke: clean
	-rm -rf ~/.pre-commit

clean:
	-rm -rf $(SRC)/*.pyc
	-rm -rf $(TEST)/*.pyc
	-rm -rf .cache/
	-rm -rf src/__pycache__
	-rm -rf test/__pycache__
