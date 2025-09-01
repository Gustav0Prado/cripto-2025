SOURCES := main.py aes.py rlyeh.py
STAMP := .mypyc.stamp

.PHONY: all clean install
all: $(STAMP)

$(STAMP): $(SOURCES)
	python3 -m mypyc $(SOURCES)
	touch $@

install:
	python3 -m pip install -U 'mypy[mypyc]'

clean:
	rm -rf $(STAMP) *.so *.txt build/ .mypy_cache/ __pycache__/