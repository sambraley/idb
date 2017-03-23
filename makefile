.DEFAULT_GOAL := RunIDB

FILES :=                              \
    IDB1.html                         \
    IDB1.log                          \
    IDB1.pdf                          \
    app/idb.py                        \
    app/test.py                       \
    .travis.yml                       \

ifeq ($(shell uname), Darwin)          # Apple
    PYTHON   := python3.5
    PIP      := pip3.5
    PYLINT   := pylint
    COVERAGE := coverage-3.5
    PYDOC    := pydoc3.5
    AUTOPEP8 := autopep8
else ifeq ($(CI), true)                # Travis CI
    PYTHON   := python3.5
    PIP      := pip3.5
    PYLINT   := pylint
    COVERAGE := coverage-3.5
    PYDOC    := pydoc3.5
    AUTOPEP8 := autopep8
else ifeq ($(shell uname -p), unknown) # Docker
    PYTHON   := python3.5
    PIP      := pip3.5
    PYLINT   := pylint
    COVERAGE := coverage-3.5
    PYDOC    := pydoc3.5
    AUTOPEP8 := autopep8
else                                   # UTCS
    PYTHON   := python3
    PIP      := pip3
    PYLINT   := pylint
    COVERAGE := coverage-3.5
    PYDOC    := pydoc3.5
    AUTOPEP8 := autopep8
endif

.pylintrc:
	$(PYLINT) --disable=locally-disabled --reports=no --generate-rcfile > $@


IDB.html: app/idb.py
	pydoc3 -w app/idb.py

IDB.log:
	git log > IDB1.log

RunIDB: app/idb.py
	-$(PYLINT) app/idb.py
	$(PYTHON) app/idb.py

TestIDB.tmp: app/test.py .pylintrc
	-$(PYLINT) app/test.py
	$(COVERAGE) run    --branch test.py >  TestIDB.tmp 2>&1
	$(COVERAGE) report -m                      >> TestIDB.tmp
	cat TestIDB.tmp

check:
	@not_found=0;                                 \
    for i in $(FILES);                            \
    do                                            \
        if [ -e $$i ];                            \
        then                                      \
            echo "$$i found";                     \
        else                                      \
            echo "$$i NOT FOUND";                 \
            not_found=`expr "$$not_found" + "1"`; \
        fi                                        \
    done;                                         \
    if [ $$not_found -ne 0 ];                     \
    then                                          \
        echo "$$not_found failures";              \
        exit 1;                                   \
    fi;                                           \
    echo "success";

clean:
	rm -f  .coverage
	rm -f  .pylintrc
	rm -f  *.pyc
	rm -f  TestIDB.tmp
	rm -rf __pycache__

config:
	git config -l

format:
	$(AUTOPEP8) -i app/idb.py
	$(AUTOPEP8) -i app/test.py

status:
	make clean
	@echo
	git branch
	git remote -v
	git status

test: TestIDB.tmp
	ls -al
	make check

versions:
	which make
	make --version
	@echo
	which git
	git --version
	@echo
	which $(PYTHON)
	$(PYTHON) --version
	@echo
	which $(PIP)
	$(PIP) --version
	@echo
	which $(PYLINT)
	$(PYLINT) --version
	@echo
	which $(COVERAGE)
	$(COVERAGE) --version
	@echo
	-which $(PYDOC)
	-$(PYDOC) --version
	@echo
	which $(AUTOPEP8)
	$(AUTOPEP8) --version
	@echo
	$(PIP) list
