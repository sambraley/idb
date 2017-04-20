var width = 1000,
    height = 1000;

var projection = d3.geo.mercator()
    .center([0, 5 ])
    .scale(200)
    .rotate([-180,0]);

var svg = d3.select("svg")
    .attr("width", width)
    .attr("height", height);

var path = d3.geo.path()
    .projection(projection);

var g = svg.append("g");

var is_data = true;
var all_concerts = [];
var i = 0;

// while(is_data){
function pull_concerts(page){

	$.getJSON( "http://boswemianrhapsody.me/api/concerts?results_per_page=100&page="+page, function( data ) {
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
	d3.json("/static/csv/world-110m2.json", function(error, topology) {
    g.selectAll("circle")
       .data(all_concerts)
       .enter()
       .append("a")
				  .attr("xlink:href", function(d) {
					  return "https://www.google.com/search?q="+d.venue.city;}
				  )
       .append("circle")
       .attr("cx", function(d) {
               return projection([d.venue.longitude, d.venue.latitude])[0];
       })
       .attr("cy", function(d) {
               return projection([d.venue.longitude, d.venue.latitude])[1];
       })
       .attr("r", 5)
       .style("fill", "red");


	g.selectAll("path")
	      .data(topojson.object(topology, topology.objects.countries)
	          .geometries)
	    .enter()
	      .append("path")
	      .attr("d", path)
	});
}

// zoom and pan
var zoom = d3.behavior.zoom()
    .on("zoom",function() {
        g.attr("transform","translate("+ 
            d3.event.translate.join(",")+")scale("+d3.event.scale+")");
        g.selectAll("circle")
            .attr("d", path.projection(projection));
        g.selectAll("path")  
            .attr("d", path.projection(projection)); 

  });

svg.call(zoom)