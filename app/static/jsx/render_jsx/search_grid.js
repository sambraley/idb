import NavBar from './../components/nav_bar';
import ModelList from './../components/models_list';
import ModelTitle from './../components/model_title';
import DropDown from './../components/drop_down';
import Pages from './../components/pages';
import Modals from './../components/modals';
import "isomorphic-fetch";

const exts = {"planets": "Planets", "galaxies": "Galaxies", "satellites": "Satellites", "stars": "Stars", };

class App extends React.Component {
	constructor (props) {
		super(props);

		this.state = { 
			models: [],
			total_pages: 1,
			current_page: 1,
			loaded: false
		};
		
		this.getModels(this.state.current_page);
	}	

	getModels(page) {
		const apiExt = "/api/v1/" + window.location.href.split("/")[3] + "&page=" + page + "&results_per_page=6";
		const url = apiExt;
		console.log(url);
		fetch(url)
	      .then((response) => response.json())
	      .then((responseJson) => {
	      	console.log(responseJson);
	        this.setState({ 
	        	models: responseJson.objects,
	        	total_pages: responseJson.total_pages,
	        	current_page: responseJson.page,
	        	loaded: true
	        })
		    })
		    .catch((error) => {
		        console.error(error);
	      	})
	}

	
	render () {
		if (!this.state.loaded) {
			return (
					<h1 className="text-center">Loading Search Results</h1>
				);
		}
		if (this.state.models.length <= 0) {
			return (
					<h1 className="text-center">No Results Found</h1>
				);
		}
		return (
				<div className="model-container">
					<ModelTitle title="Search Results" />
					<div className="row">
						<div className="col-md-9 text-right">
							<Pages 
								current_page={this.state.current_page}
								total_pages={this.state.total_pages} 
								onPageSelect={this.getModels.bind(this)} />
						</div>
					</div>
					<ModelList 
						models={this.state.models}
						page={this.current_page} />
					<div key="pages" className="col-md-12 text-right">
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
  <App />, document.querySelector('.content-container')
);