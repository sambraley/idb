.DEFAULT_GOAL := database

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


data:
		@mkdir data

scraped_data:
		@mkdir scraped_data

scraped_data/scraped_galaxies.json: scraped_data scrapers/scrape_galaxies.py
		@cd scrapers; \
		$(PYTHON) scrape_galaxies.py

scraped_data/scraped_stars.json: scraped_data scrapers/scrape_stars.py
		@cd scrapers; \
		$(PYTHON) scrape_stars.py

scraped_data/scraped_planets.json: scraped_data scrapers/scrape_planets.py
		@cd scrapers; \
		$(PYTHON) scrape_planets.py

scraped_data/scraped_satellites.json: scraped_data scrapers/scrape_satellites.py
		@cd scrapers; \
		$(PYTHON) scrape_satellites.py
	
database: scraped_data/scraped_galaxies.json scraped_data/scraped_stars.json scraped_data/scraped_planets.json scraped_data/scraped_satellites.json data
		@$(PYTHON) patch_json.py
		@$(PYTHON) url_patch.py