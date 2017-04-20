import SearchList from './../components/search_list.jsx';
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
			model_results: false,
			and: [],
			and_results: false,
			or: [],
			or_results: false,
			total_pages: 1,
			current_page: Number(dict['page']),
			loaded: false,
			search: dict['q']
		};
		this.getModels();
	}	

	getModels() {
		var url = "/api/v1/search?page=" + this.state.current_page + "&results_per_page=10&q=" + this.state.search;
		fetch(url)
	      .then((response) => response.json())
	      .then((responseJson) => {
	        console.log(responseJson);
	        if (responseJson.objects === undefined) {	
		        this.setState({ 
		        	models: [],
		        	and: responseJson.AND,
		      		or: responseJson.OR,
		        	total_pages: responseJson.total_pages,
		        	current_page: responseJson.page,
		        	loaded: true
		        });
	        }
	        else {
	        	this.setState({ 
		        	models: responseJson.objects,
		        	and: [],
		      		or: [],
		        	total_pages: responseJson.total_pages,
		        	current_page: responseJson.page,
		        	loaded: true
		        });
	        }
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
		if (this.state.models.length + this.state.or.length + this.state.and.length<= 0 ) {
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
					<div className="col-md-offset-3 col-md-6 col-xs-offset-3 col-sm-offset-3 col-sm-6 col-xs-6">
						{this.state.models.length > 0 &&
					        <SearchList 
					        	models={this.state.models}
					        	search={this.state.search} />
					    }
					    {this.state.and.length > 0 &&
					    	<div>
						        <h3 className="text-center">And Search Results</h3>
						        <SearchList 
						        	models={this.state.and}
						        	search={this.state.search} />
						    </div>
					    }
					    {this.state.or.length > 0 &&
					    	<div>
					        	<h3 className="text-center">Or Search Results</h3>
					        	<SearchList 
					        		models={this.state.or}
					        		search={this.state.search} />
					        </div>
					    }
				    </div>
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