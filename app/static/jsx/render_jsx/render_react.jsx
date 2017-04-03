import NavBar from './../components/nav_bar';
import ModelList from './../components/models_list';
import ModelTitle from './../components/model_title';
import DropDown from './../components/drop_down';

class App extends React.Component {
	render () {
		return (
			<div>
				<div>	
					<NavBar />
				</div>
				<div class="container model-container">
					<ModelTitle />
					<div className="row"> 
						<DropDown />
					</div>
					<ModelList />
				</div>
			</div>
			);
	}
}


ReactDOM.render(
  <App />, document.querySelector('.container')
);

