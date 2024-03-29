import NavBar from './../components/nav_bar';
import ModelList from './../components/models_list';
import ModelTitle from './../components/model_title';
import DropDown from './../components/drop_down';
import Pages from './../components/pages';
import Modals from './../components/modals';
import "isomorphic-fetch";

const exts  = {"planets": "Planets", "galaxies": "Galaxies", "satellites": "Satellites", "stars": "Stars", };
const label = {"name": "Name" , "temperature": "Temperature", "diameter": "Diameter", 
					"gravity": "Gravity", "mass": "Mass", "size": "Size", "agency": "Agency",
					"mission_type": "Mission Type", "year_launched": "Launch Year", "Sorted By": "Sorted By"};
var modelType = window.location.href.split('/')[3];

class App extends React.Component {
	constructor (props) {
		super(props);
		var dict = {};
		dict['page'] = 1;
		dict['sorted'] = false;
		dict['attr'] = "Sorted By"
		dict['filtered'] = false;
		var href = window.location.href;
		if (href.indexOf('?') >= 0 && href.indexOf('&') >= 0){
			var parameters = window.location.href.split('?')[1].split('&');
			for (var i = 0; i < parameters.length; i += 1) {
				var e = parameters[i].indexOf('=');
				var l = parameters[i].length;
				var key = parameters[i].substring(0,e);
				var value = parameters[i].substring(e+1,l);
				dict[key] = value;
			}
			modelType = modelType.split('?')[0];
		}
		else if (href.indexOf('?') >= 0){
			var parameters = window.location.href.split('?')[1];
			var e = parameters.indexOf('=');
			var l = parameters.length;
			var key = parameters.substring(0,e);
			var value = parameters.substring(e+1,l);
			dict[key] = value;
			modelType = modelType.split('?')[0];
		}
		this.state = { 
			models: [],
			title: exts[modelType],
			total_pages: 1,
			current_page: Number(dict['page']),
			modelType: modelType,
			sort_title: label[dict['attr']],
			sorted: dict['sorted'],
			current_sort_attr: dict['attr'],
			current_sort_dir: dict['dir'], 
			isFiltered: dict['filtered'],
			current_filter_v1: dict['v1'],
			current_filter_v2: dict['v2'],
			current_filter_v3: dict['v3'],
			loaded: false
		};
		this.getModels();
	}	

	getModels() {
		var url = "/api/v1/" + this.state.modelType + "?page=" + this.state.current_page + "&results_per_page=6";
		if (this.state.sorted) {
			url += "&q={%22order_by%22:[{%22field%22:%22" + this.state.current_sort_attr + "%22,%22direction%22:%22" + this.state.current_sort_dir + "%22}]}";
		}
		if (this.state.isFiltered) {
			url += "&q={%22filters%22:[{%22name%22:%22" + this.state.current_filter_v1 + "%22,%22op%22:%22" + this.state.current_filter_v2 + "%22,%22val%22:" + this.state.current_filter_v3 + "}]}";
		}
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
		var url = "/" + this.state.modelType + "?page=" + this.state.current_page;
		if (this.state.sorted) {
			url += "&sorted=" + this.state.sorted + "&attr=" + this.state.current_sort_attr + "&dir=" + this.state.current_sort_dir;
		}
		if (this.state.isFiltered) {
			url += "&filtered=" + this.state.isFiltered;
			url += "&v1=" + this.state.current_filter_v1;
			url += "&v2=" + this.state.current_filter_v2;
			url += "&v3=" + this.state.current_filter_v3;
		}
		window.location = url;
	}

	changePage(page) {
		this.state['current_page'] = page;
		this.redirect();
	}

	sortBy(attr, dir) {
		this.state.sorted = true;
		this.state.isFiltered = false;
		this.state.current_sort_attr = attr;
		this.state.current_sort_dir = dir;
		this.state.current_page = 1;
		this.redirect();
	}

	filterBy(v1, v2, v3) {
		this.state.isFiltered = true;
		this.state.sorted = false;
		this.state.current_filter_v1 = v1;
		this.state.current_filter_v2 = v2;
		this.state.current_filter_v3 = v3;
		this.state.current_page = 1;
		this.redirect();
	}

	
	render () {
		if (!this.state.loaded) {
			return (
					<h1 className="text-center">Loading {this.state.title}</h1>
				);
		}
		if (this.state.models.length <= 0) {
			return (
					<h1 className="text-center">No Results Found</h1>
				);
		}
		return (
			<div className="model-container">
				<ModelTitle title={this.state.title} />
				<div className="row"> 
					<div className="col-md-4 col-sm-3">
					</div>
					<div className="col-sm-3 col-md-2 text-center sort-filter-button">
						<DropDown 
							sort_title={this.state.sort_title}
							modelType={this.state.modelType}
							sortBy={this.sortBy.bind(this)} />
					</div>
					<div className="col-sm-3 col-md-2 text-center sort-filter-button">
						<Modals
							modelType={this.state.modelType} 
							filterBy={this.filterBy.bind(this)} />
					</div>
					<div className="col-md-4 col-sm-3">
					</div>
				</div>
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
					page={this.current_page} />
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

