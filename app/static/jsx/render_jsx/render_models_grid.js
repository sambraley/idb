import NavBar from './../components/nav_bar';
import ModelList from './../components/models_list';
import ModelTitle from './../components/model_title';
import DropDown from './../components/drop_down';

const exts = {"planets": "Planets", "galaxies": "Galaxies", "satellites": "Satellites", "stars": "Stars", };
const modelType = window.location.href.split('/')[3];
const baseUrl = window.location.href.split('/')[2];
const apiExt = "/api/v1/" + modelType + "?page=1&results_per_page=9";
const url = "https://" + baseUrl + apiExt;


class App extends React.Component {
	constructor (props) {
		super(props);

		this.state = { 
			models: [],
			title: exts[modelType]
		};
		
	}	

	componentDidMount() {
		fetch(url)
	      .then((response) => response.json())
	      .then((responseJson) => {
	        console.log(responseJson);
	        console.log(responseJson.num_results);
	        console.log(responseJson.objects);
	        console.log(responseJson.page);
	        console.log(responseJson.total_pages);
	        this.setState({ 
	        	models: responseJson.objects
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
					<ModelTitle title={this.state.title} />
					<div className="row"> 
						<DropDown />
					</div>
					<ModelList models={this.state.models} />
				</div>
			</div>
			);
	}
}


ReactDOM.render(
  <App />, document.querySelector('.container')
);

