class Satellite_Img extends React.Component {
	constructor(props) {
		super(props);
		this.state = {
			image_url: "undefined"
		};
		var base_url = "/" + window.location.href.split('/')[3] + "/" + window.location.href.split('/')[4].split('?')[0];
		var image_url = "/api/v1" + base_url + "/image";
		fetch(image_url)
	    .then((response) => response.json())
	    .then((responseJson) => {
	        this.setState({ 
	        	image_url: responseJson.img_url
	        })
		})
		.catch((error) => {console.log(error)})
		this.default = this.default.bind(this);
	}

	default() {
		this.setState({
			image_url: '/static/images/satellite_default.jpg'
		})
	}

    render() {
        return (
					<img className="img-thumbnail" style={{width: '400px', height: '400px'}} src={this.state.image_url} onError={this.default}/> 
				);
    }
}

export default Satellite_Img;