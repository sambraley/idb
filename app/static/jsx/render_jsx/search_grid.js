import NavBar from './../components/nav_bar';
import ModelList from './../components/models_list';
import ModelTitle from './../components/model_title';
import Pages from './../components/pages';
import "isomorphic-fetch";

class App extends React.Component {
	constructor (props) {
		super(props);
		var dict = {};
		dict['page'] = 1;
		var href = window.location.href;
		if (href.indexOf('?') >= 0 && href.indexOf('&') >= 0){
			var parameters = window.location.href.split('?')[1].split('&');
			for (var i = 0; i < parameters.length; i += 1) {
				var key = parameters[i].split('=')[0];
				var value = parameters[i].split('=')[1];
				dict[key] = value;
			}
		}
		else if (href.indexOf('?') >= 0){
			var parameters = window.location.href.split('?')[1];
			var key = parameters.split('=')[0];
			var value = parameters.split('=')[1];
			dict[key] = value;
		}
		this.state = { 
			models: [],
			total_pages: 1,
			current_page: Number(dict['page']),
			loaded: false,
			search: dict['q']
		};
		this.getModels();
	}	

	getModels() {
		var url = "/api/v1/search?page=" + this.state.current_page + "&results_per_page=6&q=" + this.state.search;
		fetch(url)
	      .then((response) => response.json())
	      .then((responseJson) => {
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
	redirect() {
		var url = "/search?page=" + this.state.current_page + "&q=" + this.state.search;
		window.location = url;
	}

	changePage(page) {
		this.state['current_page'] = page;
		this.redirect();
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
						<div className="col-md-12 text-center">
							<Pages 
								current_page={this.state.current_page}
								total_pages={this.state.total_pages} 
								onPageSelect={this.changePage.bind(this)} />
						</div>
					</div>
					<ModelList 
						models={this.state.models}
						page={this.current_page}
						search={this.state.search} />
					<div key="pages" className="col-md-12 text-center">
						<Pages 
							current_page={this.state.current_page}
							total_pages={this.state.total_pages} 
							onPageSelect={this.changePage.bind(this)} />
					</div>
				</div>
			);
	}
}


ReactDOM.render(
  <App />, document.querySelector('.content-container')
);