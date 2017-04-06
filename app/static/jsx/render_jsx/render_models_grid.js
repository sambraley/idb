import NavBar from './../components/nav_bar';
import ModelList from './../components/models_list';
import ModelTitle from './../components/model_title';
import DropDown from './../components/drop_down';
import Pages from './../components/pages.js';

const exts = {"planets": "Planets", "galaxies": "Galaxies", "satellites": "Satellites", "stars": "Stars", };
const modelType = window.location.href.split('/')[3];
const baseUrl = window.location.href.split('/')[2];
const apiExt = "/api/v1/" + modelType + "?page=1&results_per_page=9";
const url = "http://" + baseUrl + apiExt;


class App extends React.Component {
	constructor (props) {
		super(props);

		this.state = { 
			models: [],
			title: exts[modelType],
			total_pages: 1,
			current_page: 1
		};
		
	}	

	componentDidMount() {
		if (this.current_page !== undefined) {
			const apiExt = "/api/v1/" + modelType + "?page=" + this.current_page + "&results_per_page=9";
		}
		else {
			const apiExt = "/api/v1/" + modelType + "?page=1&results_per_page=9";
		}
		const url = "http://" + baseUrl + apiExt;
		fetch(url)
	      .then((response) => response.json())
	      .then((responseJson) => {
	        this.setState({ 
	        	models: responseJson.objects,
	        	total_pages: responseJson.total_pages,
	        	current_page: responseJson.page,
	        })
		    })
		    .catch((error) => {
		        console.error(error);
	      	})
	}

	getModels(current_page) {
		console.log("in the getModels () ");
		this.setState({current_page: current_page})
		console.log(current_page);
		const apiExt = "/api/v1/" + modelType + "?page=" + current_page + "&results_per_page=9";
		const url = "http://" + baseUrl + apiExt;
		fetch(url)
	      .then((response) => response.json())
	      .then((responseJson) => {
	      	console.log(responseJson.objects);
	        this.setState({ 
	        	models: responseJson.objects,
	        	total_pages: responseJson.total_pages,
	        	current_page: responseJson.page,
	        })
		    })
		    .catch((error) => {
		        console.error(error);
	      	})
	}
	
	render () {
		return (
			<div id="main-div">
				<div id="nav-bar-div">	
					<NavBar />
				</div>
				<div className="container model-container">
					<ModelTitle title={this.state.title} />
					<div className="row"> 
						<DropDown />
					</div>
					<ModelList 
						models={this.state.models}
						page={this.current_page} />
					<Pages 
						current_page={this.state.current_page}
						total_pages={this.state.total_pages} 
						onPageSelect={this.getModels.bind(this)} />
				</div>
			</div>
			);
	}
}


ReactDOM.render(
  <App />, document.querySelector('.container')
);

