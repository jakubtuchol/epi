SRC = src
TEST = test
TEST_CMD = py.test

.PHONY: test clean

test:
	$(TEST_CMD)

clean:
	-rm -rf $(SRC)/*.pyc
	-rm -rf $(TEST)/*.pyc
