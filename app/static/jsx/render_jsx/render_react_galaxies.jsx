import NavBar from './../components/nav_bar';
import ModelList from './../components/models_list';
import ModelTitle from './../components/model_title';
import DropDown from './../components/drop_down';

const galaxies = [
	{
		"dec": 37.884811,
		"size": 1.227,
		"redshift": 0.027192,
		"ra": 317.819183,
		"name": "UGC 11693",
		"pid": 1,
		"morph_type": "Spiral"
	},
	{
		"dec": 37.583397,
		"size": 1.29,
		"redshift": 0.025928,
		"ra": 320.125275,
		"name": "UGC 11726",
		"pid": 2,
		"morph_type": "Spiral"
	},
	{
		"dec": 41.272003,
		"size": 1.717,
		"redshift": 0.015007,
		"ra": 326.49365,
		"name": "UGC 11808",
		"pid": 3,
		"morph_type": "Spiral"
	}
]

class App extends React.Component {
	constructor (props) {
		super(props);

		this.state = { 
			models: galaxies,
			title: "Galaxies"
		};
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

