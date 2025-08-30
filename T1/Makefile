SOURCES := main.py aes.py rlyeh.py
STAMP := .mypyc.stamp

.PHONY: all clean
all: $(STAMP)

$(STAMP): $(SOURCES)
	python3 -m mypyc $(SOURCES)
	touch $@

clean:
	rm -f $(STAMP) *.so *.txt