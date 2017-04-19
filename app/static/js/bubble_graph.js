var svg = d3.select("svg.albums"),
    width = +svg.attr("width"),
    height = +svg.attr("height");

var format = d3.format(",d");

var color = d3.scaleOrdinal(d3.schemeCategory20c);

var pack = d3.pack()
    .size([width, height])
    .padding(1.5);

var all_artists = [];
var count = 0;

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
  var genre_to_num_albums = {};
  for(i = 0;i < all_artists.length;i+=1){
    if(genre_to_num_albums[all_artists[i].genre]){ //genre exists
      genre_to_num_albums[all_artists[i].genre] += all_artists[i].albums.length;
    }else{
      genre_to_num_albums[all_artists[i].genre] = all_artists[i].albums.length;  
    };
  }; 
  console.log(genre_to_num_albums); 
};


// , function(data) {
//   console.log("hi");
  // console.log("hi again");
  // console.log(data);
  // for(artist in data){
  //   console.log(artist.name);
  // }

  // var root = d3.hierarchy({children: classes})
  //     .sum(function(d) { return d.value; })
  //     .each(function(d) {
  //       if (id = d.data.id) {
  //         var id, i = id.lastIndexOf(".");
  //         d.id = id;
  //         d.package = id.slice(0, i);
  //         d.class = id.slice(i + 1);
  //       }
  //     });



  // var node = svg.selectAll(".node")
  //   .data(pack(root).leaves())
  //   .enter().append("g")
  //     .attr("class", "node")
  //     .attr("transform", function(d) { return "translate(" + d.x + "," + d.y + ")"; });

  // node.append("circle")
  //     .attr("id", function(d) { return d.id; })
  //     .attr("r", function(d) { return d.r; })
  //     .style("fill", function(d) { return color(d.package); });

  // node.append("clipPath")
  //     .attr("id", function(d) { return "clip-" + d.id; })
  //   .append("use")
  //     .attr("xlink:href", function(d) { return "#" + d.id; });

  // node.append("text")
  //     .attr("clip-path", function(d) { return "url(#clip-" + d.id + ")"; })
  //   .selectAll("tspan")
  //   .data(function(d) { return d.class.split(/(?=[A-Z][^A-Z])/g); })
  //   .enter().append("tspan")
  //     .attr("x", 0)
  //     .attr("y", function(d, i, nodes) { return 13 + (i - nodes.length / 2 - 0.5) * 10; })
  //     .text(function(d) { return d; });

  // node.append("title")
  //     .text(function(d) { return d.id + "\n" + format(d.value); });
