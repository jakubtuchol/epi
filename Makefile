SRC = src
TEST = test
TEST_CMD = py.test

.PHONY: test clean

install:
	pip install -rrequirements.txt

test:
	$(TEST_CMD)

clean:
	-rm -rf $(SRC)/*.pyc
	-rm -rf $(TEST)/*.pyc
	-rm -rf .cache/
	-rm -rf test/__pycache__
