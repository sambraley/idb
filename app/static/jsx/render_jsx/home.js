import Carousel from '../carousel.jsx';

$('.carousel').carousel({
  interval: 1000 * 3
});

// var temp = document.createElement("div");
ReactDOM.render(
	<Carousel />,
	document.getElementById("space-carousel")
);
// var container = document.getElementById("space-carousel");
// container.replaceChild(temp.querySelector("#react-carousel"), document.getElementById("react-carousel"));
