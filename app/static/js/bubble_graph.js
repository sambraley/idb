// var svg = d3.select("svg"),
//     width = +svg.attr("width"),
//     height = +svg.attr("height");

// var format = d3.format(",d");

// var color = d3.scaleOrdinal(d3.schemeCategory20c);

// var pack = d3.pack()
//     .size([width, height])
//     .padding(1.5);

var diameter = 600;

var svg = d3.select('#graph').append('svg')
  .attr('width', diameter)
  .attr('height', diameter);

var bubble = d3.pack()
  .size([diameter, diameter])
  // .value(function(d) {return d.size;})
   // .sort(function(a, b) {
  //  return -(a.value - b.value)
  // }) 
  .padding(3);

var all_artists = [];
var count = 0;
var genre_to_num_albums = {};

for(var i = 1;i <= 2;i+=1){
  var url = "http://boswemianrhapsody.me/api/artists?results_per_page=100&page=" + i
  d3.json(url, function(data) {
  }).on("load", function(data) {
    console.log("loaded");
    console.log(data);
    for(x = 0;x < data.objects.length;x+=1){
      all_artists.push(data.objects[x]);
    }
    count += 1;
    if(count == 2){
      processData();
    };
  });
};

function processData(){
  console.log(all_artists.length);
  console.log(all_artists);
  for(i = 0;i < all_artists.length;i+=1){
    if(genre_to_num_albums[all_artists[i].genre]){ //genre exists
      genre_to_num_albums[all_artists[i].genre] += all_artists[i].albums.length;
    }else{
      genre_to_num_albums[all_artists[i].genre] = all_artists[i].albums.length;  
    };
  }; 
  console.log(genre_to_num_albums);
  bubbleChart(); 
};

function bubbleChart(){
 var nodes = bubble.nodes(processData(genre_to_num_albums))
            .filter(function(d) { return !d.children; }); // filter out the outer bubble
 
  var vis = svg.selectAll('circle')
          .data(nodes);
  
  vis.enter().append('circle')
      .attr('transform', function(d) { return 'translate(' + d.x + ',' + d.y + ')'; })
      .attr('r', function(d) { return d.r; })
      .attr('class', function(d) { return d.className; });
  
  function processData(data) {
    var obj = data;

    var newDataSet = [];

    for(var prop in obj) {
      newDataSet.push({name: prop, className: prop.toLowerCase(), size: obj[prop]});
    }
    return {children: newDataSet};
  }
};
