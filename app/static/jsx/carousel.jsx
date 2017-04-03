import CarouselItem from './carouselItem.jsx'
import "isomorphic-fetch"
import moment from "../bower_components/moment/moment.js"

var key = "We3gv991soU65ecdkUfJVTsZyl3ZjOiDZPQFlaAv";
var nasa_url = "https://api.nasa.gov/planetary/apod?api_key=" + key + "&date=";

class Carousel extends React.Component {
		constructor(props) {
			super(props);
			this.urls = [];
			this.state = {
				"urls": [],
			};
			var cur_date = moment();
			for (var i = 0; i < 5; i += 1) {
				var url = nasa_url + cur_date.format("YYYY-MM-DD");
				fetch(url).then(r => r.json())
			  .then(data => this.url_push(data))
			  .catch(e => console.log(e));
				cur_date = cur_date.subtract(1, 'days');
			}
		}
		url_push(data) {
			this.state.urls.push(data.hdurl);
			this.forceUpdate();
		}
    render() {
        return (
				  <div id="react-carousel" className="carousel-inner" role="listbox">
				    <CarouselItem url={this.state.urls[0]} class="active"/>
				    <CarouselItem url={this.state.urls[1]} class=""/>
				    <CarouselItem url={this.state.urls[2]} class=""/>
				    <CarouselItem url={this.state.urls[3]} class=""/>
				    <CarouselItem url={this.state.urls[4]} class=""/>
				  </div>
				);
    }
}

export default Carousel;