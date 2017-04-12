import NavBar from './../components/nav_bar';
import ModelList from './../components/models_list';
import ModelTitle from './../components/model_title';
import DropDown from './../components/drop_down';
import Pages from './../components/pages';
import Modals from './../components/modals';
import "isomorphic-fetch";

const exts = {"planets": "Planets", "galaxies": "Galaxies", "satellites": "Satellites", "stars": "Stars", };
const modelType = window.location.href.split('/')[3];

class App extends React.Component {
	constructor (props) {
		super(props);

		this.state = { 
			models: [],
			title: exts[window.location.href.split('/')[3]],
			total_pages: 1,
			current_page: 1,
			modelType: modelType,
			sort_title: "Sort By",
			current_sort_attr: null,
			current_sort_dir: null, 
			isFiltered: false,
			current_filter_v1: null,
			current_filter_v2: null,
			current_filter_v3: null
		};
		
		this.getModels(this.state.current_page);
	}	

	getModels(page) {
		if (this.state.sort_title === "Sort By") {
			// console.log("pages are not sorted");

			const baseUrl = window.location.href.split('/')[2];
			const apiExt = "/api/v1/" + this.state.modelType + "?page=" + page + "&results_per_page=6";
			const url = "http://" + baseUrl + apiExt;
			// console.log(url);
			fetch(url)
		      .then((response) => response.json())
		      .then((responseJson) => {
		      	// console.log("I'm back with some values");
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
		else {
			// console.log("pages are sorted by " + this.state.sort_title);
			// console.log("using attr " + this.state.current_sort_attr);
			// console.log("by order " + this.state.current_sort_dir);
			this.sortBy(this.state.current_sort_attr, this.state.current_sort_dir, this.state.sort_title, page);
		}
	}

	sortBy(attr, dir, sort_title, page) {
		// ?q={"order_by":[{"field": <fieldname>, "direction": <directionname>}]}
		// console.log(attr, dir);
		const baseUrl = window.location.href.split('/')[2];
		const apiExt = "/api/v1/" + this.state.modelType + "?page=" + page + "&results_per_page=9&q={%22order_by%22:[{%22field%22:%22" + attr + "%22,%22direction%22:%22" + dir + "%22}]}";
		const url = "http://" + baseUrl + apiExt;
		// console.log(url);
		fetch(url)
	      .then((response) => response.json())
	      .then((responseJson) => {
	      	// console.log("Back from sorting call");
	        this.setState({ 
	        	models: responseJson.objects,
	        	total_pages: responseJson.total_pages,
	        	current_page: responseJson.page,
	        	sort_title: sort_title,
	        	current_sort_attr: attr,
	        	current_sort_dir: dir
	        })
		    })
		    .catch((error) => {
		        console.error(error);
	      	})
	}

	filterBy(v1, v2, v3, page) {
		// ?q={"filters":[{"name":"<fieldname>", "op":"<operator>", "value": <value>}]}
		const baseUrl = window.location.href.split('/')[2];
		const apiExt = "/api/v1/" + this.state.modelType + "?page=" + page + "&results_per_page=9&q={%22filters%22:[{%22name%22:%22" + v1 + "%22,%22op%22:%22" + v2 + "%22,%22val%22:" + 1 + "}]}";
		const url = "http://" + baseUrl + apiExt;
		fetch(url)
	      .then((response) => response.json())
	      .then((responseJson) => {
	      	console.log("return in filterBy func: v1: " + v1 + " v2: " + v2 + " v3: " + v3);
	        this.setState({ 
	        	models: responseJson.objects,
	        	total_pages: responseJson.total_pages,
	        	current_page: responseJson.page,
	        	isFiltered: true,
				current_filter_v1: v1,
				current_filter_v2: v2,
				current_filter_v3: v3
	        })
		    })
		    .catch((error) => {
		        console.error(error);
	      	})
	}

	
	render () {
		return (
			<div className="model-container">
				<ModelTitle title={this.state.title} />
				<div className="row"> 
					<div className="col-md-2 text-left sort-filter-button">
						<DropDown 
							sort_title={this.state.sort_title}
							modelType={this.state.modelType}
							sortBy={this.sortBy.bind(this)} />
					</div>
					<div className="col-md-1 text-left sort-filter-button">
						<Modals
							modelType={this.state.modelType} 
							filterBy={this.filterBy.bind(this)} />
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

