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
	        	image_url: responseJson.img_url,
	        })})
		.catch((error) => {console.error(error);})
	}
    render() {
        return (
					<img className="img-thumbnail" style={{width: '400px', height: '400px'}} src={this.state.image_url} onerror="if (this.src != '/static/images/satellite_default.jpg') this.src='/static/images/satellite_default.jpg';"/> 
				);
    }
}

export default Satellite_Img;