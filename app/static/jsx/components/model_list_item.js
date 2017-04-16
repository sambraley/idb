
class ModelListItem extends React.Component {
	constructor(props) {
		super(props);
		var base_url = "/" + this.props.model.model_type + "s/";
		var link = base_url + this.props.model.pid;
		this.state = {
			style: {
						width: '400px',
						height: '400px'
					},
			image_url: "/undefined",
			link: link
		}
		var image_url = "/api/v1" + base_url + this.props.model.pid + "/image";
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
			<div className="col-lg-4 col-md-6 col-sm-12 text-center model-list-item">
				<a href={this.state.link}>
					<img className="img-thumbnail about-image" style={this.state.style} src={this.state.image_url} />
					<h3>{this.props.model.name}</h3>
				</a>
			</div> 
			);
	}
};


export default ModelListItem;