import NavBar from './../components/nav_bar';
import ModelList from './../components/models_list';
import ModelTitle from './../components/model_title';
import DropDown from './../components/drop_down';
import Pages from './../components/pages.js';

const exts = {"planets": "Planets", "galaxies": "Galaxies", "satellites": "Satellites", "stars": "Stars", };
console.log(window.location.href);

class App extends React.Component {
	constructor (props) {
		super(props);

		this.state = { 
			models: [],
			title: exts[window.location.href.split('/')[3]],
			total_pages: 1,
			current_page: 1
		};
		
		this.getModels(this.state.current_page);
	}	

	getModels(current_page) {
		const modelType = window.location.href.split('/')[3];
		const baseUrl = window.location.href.split('/')[2];
		this.setState({current_page: current_page})
		const apiExt = "/api/v1/" + modelType + "?page=" + current_page + "&results_per_page=9";
		const url = "http://" + baseUrl + apiExt;
		console.log(url);
		fetch(url)
	      .then((response) => response.json())
	      .then((responseJson) => {
	      	console.log("I'm back with some values");
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
				<div className="container-fluid model-container">
					<ModelTitle title={this.state.title} />
					<div className="row"> 
						<div className="col-md-3 text-left sort-filter-button">
							<DropDown />
						</div>
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
					<div className="col-md-12 text-right">
						<Pages 
							current_page={this.state.current_page}
							total_pages={this.state.total_pages} 
							onPageSelect={this.getModels.bind(this)} />
					</div>
				</div>
			</div>
			);
	}
}


ReactDOM.render(
  <App />, document.querySelector('.container')
);

