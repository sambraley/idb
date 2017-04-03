import CarouselItem from './carouselItem.jsx'
import "isomorphic-fetch"

class Carousel extends React.Component {
		constructor(props) {
			super(props);
			this.urls = [];
			this.urls.push(parseJSON("testing"));
		}
		parseJSON(json) {
			// TODO
			return "/static/images/space_background.jpg";
		}
    render() {
        return (
				  <div id="react-carousel" className="carousel-inner" role="listbox">
				    <CarouselItem url={this.urls[0]} message="Welcome to the final frontier!!!" class="active"/>
				    <CarouselItem url={this.urls[0]} message="2" class=""/>
				    <CarouselItem url={this.urls[0]} message="3" class=""/>
				  </div>
				);
    }
}

export default Carousel;