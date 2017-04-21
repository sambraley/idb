var width = 1000,
    height = 600;
    

var projection = d3.geo.mercator()
    .center([0, 5 ])
    .scale(200)
    .rotate([-180,0])

var svg = d3.select("svg")
    .attr("width", width)
    .attr("height", height);

var path = d3.geo.path()
    .projection(projection);

var g = svg.append("g");

var all_concerts = [];
var venues = []
var max_size = 1;

// while(is_data){
function pull_concerts(page){

	$.getJSON("http://boswemianrhapsody.me/api/concerts?results_per_page=100&page="+page, function( data ) {
		all_concerts = all_concerts.concat(data.objects);
		if (data.total_pages !== page) {
		  	pull_concerts(page + 1);
		}
		else {
			console.log(all_concerts);
			processData();
		}
	});
}
pull_concerts(1);

// load and display the World
function processData() {
    
    for (i = 0; i < all_concerts.length; i++) {
        
        var venue_index = -1;
        
        for (j = 0; j < venues.length; j++) {
            if (venues[j].name == all_concerts[i].venue.name) {
                venue_index = j;
                break;
            }
        }
        
        if (venue_index != -1) {
            venues[venue_index].size += 1;
        } else {
            venue = all_concerts[i].venue;
            venue.size = 1
            venues[venues.length] = venue;
        }
    }
    
    for (i = 0; i < venues.length; i++) {
        if (venues[i].size > max_size) {
            max_size = venues[i].size;
        }
    }
    
    venues.sort(function (v1, v2){
       return v2.size - v1.size;
    });
    
    console.log(venues);
    
	d3.json("/static/csv/world-110m2.json", function(error, topology) {
        g.selectAll("path")
              .data(topojson.object(topology, topology.objects.countries)
                  .geometries)
            .enter()
              .append("path")
              .attr("d", path);
        
        g.selectAll("circle")
           .data(venues)
           .enter()
           .append("a")
                      .attr("xlink:href", function(d) {
                          return "https://www.google.com/search?q="+d.name;}
                      )
           .append("circle")
           .attr("cx", function(d) {
                   return projection([d.longitude, d.latitude])[0];
           })
           .attr("cy", function(d) {
                   return projection([d.longitude, d.latitude])[1];
           })
           .attr("r", function(d) {
                   return 20 * (d.size / max_size) > 7 ? 7 : 15 * (d.size / max_size);
           })
           .style("fill", "red")
           .attr("stroke","black")
           .attr("stroke-width", ".1");
	});
}

// zoom and pan
var zoom = d3.behavior.zoom()
    .on("zoom",function() {
        g.attr("transform","translate("+ 
            d3.event.translate.join(",")+")scale("+d3.event.scale+")");
        g.selectAll("path")  
            .attr("d", path.projection(projection));
        g.selectAll("circle")
            .attr("d", path.projection(projection)); 

  });

svg.call(zoom)