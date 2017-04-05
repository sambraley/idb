import NavBar from './../components/nav_bar';
import ModelInfo from './../components/model_info';

/* window.location.href */
console.log(window.location.href);
console.log(window.location.hostname);

const planets = [
	{
		"dec": 44.915352,
		"star_pid": 230,
		"diameter": 176735.008,
		"mass": 3.477136e+27,
		"orbital_period": 1.327347,
		"temperature": 1823,
		"ra": 188.266255,
		"galaxy_pid": 143,
		"name": "HAT-P-36 b",
		"gravity": 0.029718570060615346,
		"pid": 1
	},
	{
		"dec": 51.269138,
		"star_pid": 28,
		"diameter": 164710.316,
		"mass": 2.218762e+27,
		"orbital_period": 2.797436,
		"temperature": 1271,
		"ra": 284.296064,
		"galaxy_pid": 143,
		"name": "HAT-P-37 b",
		"gravity": 0.02183335709325446,
		"pid": 2
	},
	{
		"dec": 32.246151,
		"star_pid": 140,
		"diameter": 115353.15,
		"mass": 5.06766e+26,
		"orbital_period": 4.640382,
		"temperature": 1082,
		"ra": 35.383234,
		"galaxy_pid": 143,
		"name": "HAT-P-38 b",
		"gravity": 0.010167166878461332,
		"pid": 3
	},
	{
		"dec": 17.830082,
		"star_pid": 248,
		"diameter": 219660.362,
		"mass": 1.136902e+27,
		"orbital_period": 3.54387,
		"temperature": 1752,
		"ra": 113.758247,
		"galaxy_pid": 143,
		"name": "HAT-P-39 b",
		"gravity": 0.006290295385687977,
		"pid": 4
	},
	{
		"dec": 45.457378,
		"star_pid": 62,
		"diameter": 241892.06,
		"mass": 1.1672699999999999e+27,
		"orbital_period": 4.457243,
		"temperature": 1770,
		"ra": 335.512861,
		"galaxy_pid": 143,
		"name": "HAT-P-40 b",
		"gravity": 0.005325734316961424,
		"pid": 5
	},
	{
		"dec": 4.672421,
		"star_pid": 119,
		"diameter": 235600.07,
		"mass": 1.5184e+27,
		"orbital_period": 2.694047,
		"temperature": 1941,
		"ra": 297.322651,
		"galaxy_pid": 143,
		"name": "HAT-P-41 b",
		"gravity": 0.00730275556261142,
		"pid": 6
	},
	{
		"dec": 6.09723,
		"star_pid": 96,
		"diameter": 178972.16,
		"mass": 1.981512e+27,
		"orbital_period": 4.641878,
		"temperature": 1428,
		"ra": 135.344391,
		"galaxy_pid": 143,
		"name": "HAT-P-42 b",
		"gravity": 0.01651494558211872,
		"pid": 7
	},
]

class App extends React.Component {
	constructor (props) {
		super(props);

		var planet_id = window.location.href.split("/")[4];
		console.log("got planet_id: " + planet_id);

		this.state = { 
			model: planets[parseInt(planet_id) - 1]
		};
	
		
		// this.setState({ 
		// 	models: planets,
		// 	title: "Planets"
		// });
	
		// console.log(this.state.models);
		// console.log(this.state.title);
	}	

		// YTSearch({key: API_KEY, term: term}, (videos) => {
		// 	this.setState({ 
		// 		videos: videos,
		// 		selectedVideo: videos[0]
		// 	});
		// when key and vaule are the same name, setState({ videos });
	
	render () {
		return (
			<div>
				<div>	
					<NavBar />
				</div>
				<div className="container model-container">
					<ModelInfo model={this.state.model} />
				</div>
			</div>
			);
	}
}


ReactDOM.render(
  <App />, document.querySelector('.container')
);
