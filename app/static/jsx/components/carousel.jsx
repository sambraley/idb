import CarouselItem from './carouselItem.jsx';
import "isomorphic-fetch";
import moment from "../../bower_components/moment/moment.js";

var key = "We3gv991soU65ecdkUfJVTsZyl3ZjOiDZPQFlaAv";
var nasa_url = "https://api.nasa.gov/planetary/apod?api_key=" + key + "&date=";

class Carousel extends React.Component {
		constructor(props) {
			super(props);
			this.state = {
				"urls": []
			};
			var cur_date = moment();
			var url = nasa_url + cur_date.format("YYYY-MM-DD");
			fetch(url).then(r => r.json())
			.then(data => this.url_push(data, cur_date))
			.catch(e => console.log(e));
		}
		url_push(data, cur_date) {
			cur_date = cur_date.subtract(1, 'days');
			var url = nasa_url + cur_date.format("YYYY-MM-DD");
			if (data.hdurl !== undefined){
				this.state.urls.push(data.hdurl);
				this.forceUpdate();
			}
			if (this.state.urls.length < 5){
				fetch(url).then(r => r.json())
				.then(data => this.url_push(data, cur_date))
				.catch(e => console.log(e));
			}
		}
    render() {
        return (
        		  <div>
				  <div id="react-carousel" className="carousel-inner" role="listbox">
				    <CarouselItem url={this.state.urls[0]} class="active"/>
				    <CarouselItem url={this.state.urls[1]} class=""/>
				    <CarouselItem url={this.state.urls[2]} class=""/>
				    <CarouselItem url={this.state.urls[3]} class=""/>
				    <CarouselItem url={this.state.urls[4]} class=""/>
				  </div>
				  <div className="hidden">
				    <img src={this.state.urls[0]}/>
				    <img src={this.state.urls[1]}/>
				    <img src={this.state.urls[2]}/>
				    <img src={this.state.urls[3]}/>
				    <img src={this.state.urls[4]}/>
				  </div>
				  </div>
				);
    }
}

export default Carousel;