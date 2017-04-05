import NavBar from './../components/nav_bar';
import ModelList from './../components/models_list';
import ModelTitle from './../components/model_title';
import DropDown from './../components/drop_down';

const satellites = [
	{
		"agency": "Indian Space Research Organization",
		"star_pid": 271,
		"year_launched": 2013,
		"info_url": "https://en.wikipedia.org/wiki/SARAL",
		"planet_pid": 299,
		"name": "SARAL",
		"mission_type": "Planetary Science",
		"galaxy_pid": 143,
		"pid": 1,
		"image": "https://upload.wikimedia.org/wikipedia/en/4/41/Flag_of_India.svg"
	},
	{
		"agency": "Russian Federal Space Agency (ROSCOSMOS)",
		"star_pid": 271,
		"year_launched": 2013,
		"info_url": "https://en.wikipedia.org/wiki/Resurs-P_No.1",
		"planet_pid": 299,
		"name": "Resurs-P No.1",
		"mission_type": "Earth Science",
		"galaxy_pid": 143,
		"pid": 2,
		"image": "https://upload.wikimedia.org/wikipedia/commons/d/d6/RocketSunIcon.svg"
	},
	{
		"agency": "China National Space Administration",
		"star_pid": 271,
		"year_launched": 2013,
		"info_url": "https://en.wikipedia.org/wiki/CBERS-3",
		"planet_pid": 299,
		"name": "CBERS-3",
		"mission_type": "Earth Science",
		"galaxy_pid": 143,
		"pid": 3,
		"image": "satellite.png"
	}
]


class App extends React.Component {
	constructor (props) {
		super(props);

		this.state = { 
			models: satellites,
			title: "Satellites"
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

