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
    COVERAGE := coverage
    PYDOC    := pydoc3.5
    AUTOPEP8 := autopep8
endif

.pylintrc:
	$(PYLINT) --ignored-modules=flask_sqlalchemy --generated-members=commit,query,add,delete \
		--disable=locally-disabled --reports=no --generate-rcfile > $@

IDB.html: app/models.py
	cd app; $(PYDOC) -w models; mv models.html ../IDB1.html

IDB.log:
	git log > IDB1.log

RunIDB: app/idb.py .pylintrc
	-$(PYLINT) app/idb.py
	cd app; \
	$(PYTHON) idb.py

install:
	$(PIP) install -r app/requirements.txt
	npm install

TestIDB.tmp: app/models.py app/test.py .pylintrc
	-$(PYLINT) app/test.py
	-$(PYLINT) app/models.py
	-$(COVERAGE) run app/test.py >  TestIDB.tmp 2>&1  
	-$(COVERAGE) report -m                      >> TestIDB.tmp 
	-cat TestIDB.tmp

build:
	sh compile.sh

check: IDB.log 
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
	rm -rf node_modules

config:
	git config -l

format:
	$(AUTOPEP8) -i app/idb.py
	$(AUTOPEP8) -i app/test.py
	$(AUTOPEP8) -i app/models.py

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

#
# Data Creation and Compilation
#



  