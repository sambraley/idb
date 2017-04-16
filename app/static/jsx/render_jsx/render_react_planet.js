import NavBar from './../components/nav_bar';
import ModelInfo from './../components/model_info';
import "isomorphic-fetch";

/* window.location.href */
console.log(window.location.href);
console.log(window.location.hostname);
const modelType = window.location.href.split('/')[3];
const planet_id = window.location.href.split("/")[4];
console.log("got planet_id: " + planet_id);
const apiExt = "/api/v1/" + modelType + "/" + planet_id;
const url = apiExt;


class App extends React.Component {
	constructor (props) {
		super(props);


		this.state = { 
			id: planet_id,
			model: null
		};
	
		
		
	}	

	getModel(id) {
		fetch(url)
	      .then((response) => response.json())
	      .then((responseJson) => {
	        this.setState({ 
	        	
	        })
		    })
		    .catch((error) => {
		        console.error(error);
	      	})

	}


	
	render () {
		return (
			<div>
				<div>	
					<NavBar />
				</div>
				<div className="container model-container">
					<ModelInfo model={this.state.model} />
				</div>
			</div>
			);
	}
}


ReactDOM.render(
  <App />, document.querySelector('.container')
);
