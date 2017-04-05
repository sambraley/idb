import NavBar from './../components/nav_bar';
import ModelList from './../components/models_list';
import ModelTitle from './../components/model_title';
import DropDown from './../components/drop_down';

const stars = [
	{
		"dec": 26.426662,
		"galaxy_pid": 143,
		"diameter": 1892304.0000000002,
		"temperature": 6065,
		"ra": 271.537705,
		"name": "HAT-P-31",
		"mass": 1.22,
		"pid": 1
	},
	{
		"dec": 6.563726,
		"galaxy_pid": 143,
		"diameter": 1300959.0,
		"temperature": 6112,
		"ra": 175.90838,
		"name": "WASP-85 A",
		"mass": 1.09,
		"pid": 2
	},
	{
		"dec": 16.421759,
		"galaxy_pid": 143,
		"diameter": 161402.4,
		"temperature": 2300,
		"ra": 325.122159,
		"name": "2MASS J21402931+1625183 A",
		"mass": 0.08,
		"pid": 3
	}
]

class App extends React.Component {
	constructor (props) {
		super(props);

		this.state = { 
			models: stars,
			title: "Stars"
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

