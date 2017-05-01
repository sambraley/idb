import itertools
from math import ceil
from flask_whooshee import whoosh
from database import Satellite, Planet, Star, Galaxy

def search(args):

    query = args.get('q')
    results_per_page = args.get('results_per_page', default=10)
    results_per_page = int(results_per_page)
    if results_per_page <= 0:
        results_per_page = 10

    page = args.get('page', default=1)
    page = int(page)
    if page <= 0:
        page = 1

    output = {}
    if ' ' in query:
        output = make_combined_output(query, results_per_page, page)
    else:
        output = make_simple_output(query, results_per_page, page)


    return output

def make_simple_output(query, results_per_page, page):
    results = make_query(query)

    output = {}

    num_results = len(results)
    total_pages = ceil(num_results / results_per_page)
    results = results[(page - 1) * results_per_page:page * results_per_page]
    results = [x.to_dict() for x in results]
    output["num_results"] = num_results
    output["page"] = page
    output["total_pages"] = total_pages
    output["objects"] = results

    return output

def make_combined_output(query, results_per_page, page):
    and_results = make_query(query, qparser=whoosh.qparser.AndGroup)
    or_results = make_query(query, exclude=and_results)

    total_and_results = len(and_results)
    num_results = total_and_results + len(or_results)
    total_pages = ceil(num_results / results_per_page)

    and_results = and_results[(page - 1) * results_per_page:page * results_per_page]
    num_and_to_display = len(and_results)
    if num_and_to_display < results_per_page:
        or_start = (page - 1) * results_per_page - total_and_results
        
        # Deal with mixed and/or results page fencepost problem
        num_or_to_display = results_per_page - num_and_to_display
        or_start = max(or_start, 0)

        or_results = or_results[or_start:num_or_to_display + or_start]

    else:
        or_results = []

    and_results = [x.to_dict() for x in and_results]
    or_results = [x.to_dict() for x in or_results]

    output = {}
    output["num_results"] = num_results
    output["page"] = page
    output["total_pages"] = total_pages
    output["AND"] = and_results
    output["OR"] = or_results

    return output


def make_query(query, qparser=whoosh.qparser.OrGroup, exclude=()):
    results = []
    if query:
        satellites = Satellite.query.whooshee_search(query, group=qparser)
        planets = Planet.query.whooshee_search(query, group=qparser)
        stars = Star.query.whooshee_search(query, group=qparser)
        galaxies = Galaxy.query.whooshee_search(query, group=qparser)
        results = [x for x in roundrobin(satellites.all(), planets.all(),
                                         stars.all(), galaxies.all()) if x not in exclude]

    return results


# Taken from the itertools recipes in the python documentation
# https://docs.python.org/3/library/itertools.html#itertools-recipes
def roundrobin(*iterables):
    "roundrobin('ABC', 'D', 'EF') --> A D E B F C"
    # Recipe credited to George Sakkis
    pending = len(iterables)
    nexts = itertools.cycle(iter(it).__next__ for it in iterables)
    while pending:
        try:
            for next in nexts:
                yield next()
        except StopIteration:
            pending -= 1
            nexts = itertools.cycle(itertools.islice(nexts, pending))
