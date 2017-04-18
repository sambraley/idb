import itertools
from math import ceil
from flask_whooshee import whoosh
from database import Satellite, Planet, Star, Galaxy

def search(args):

    q = args.get('q')

    results_per_page = args.get('results_per_page', default=10)
    results_per_page = int(results_per_page)
    if results_per_page <= 0:
        results_per_page = 10

    page = args.get('page', default=1)
    page = int(page)
    if page <= 0:
        page = 1

    qparser = whoosh.qparser.OrGroup
    if args.get('junction') == 'AND':
        qparser = whoosh.qparser.AndGroup

    output = {}
    results = []
    if q:
        satellites = Satellite.query.whooshee_search(q, group=qparser)
        planets = Planet.query.whooshee_search(q, group=qparser)
        stars = Star.query.whooshee_search(q, group=qparser)
        galaxies = Galaxy.query.whooshee_search(q, group=qparser)
        results = [x for x in roundrobin(satellites.all(), planets.all(), stars.all(), galaxies.all())]


    num_results = len(results)
    total_pages = ceil(len(results) / results_per_page)
    results = results[(page - 1) * results_per_page:page * results_per_page]
    results = [x.to_dict() for x in results]
    output["num_results"] = num_results
    output["page"] = page
    output["total_pages"] = total_pages
    output["objects"] = results

    return output

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
