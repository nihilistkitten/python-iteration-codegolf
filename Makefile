.PHONY: test clean normal compressed score

all: normal score

score: test
	wc -c soln.py

test: soln.py test_soln.py
	poetry run python -m pytest

normal: normal.py
	cp normal.py soln.py

compressed: uncompressed.py encoder.py
	cat uncompressed.py | python3 encoder.py > soln.py

install:
	poetry install

clean:
	-rm -rf soln.py
