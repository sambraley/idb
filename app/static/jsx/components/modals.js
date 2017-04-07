import selectOption from './select_options';

const attrs = {
	"planets": ["mass", "diameter", "gravity", "temperature"],
	"galaxies": ["size"],
	"stars": ["name", "diameter", "temperature"],
	"satellites": ["name", "agency", "mission_type", "year_launched"]
};
const ops = ["<", "<=", ">", ">=", "==", "!="];
const compareTo = {
	"planets": ["Jupiter"],
	"galaxies": ["1"],
	"stars": ["name", "diameter", "temperature"],
	"satellites": ["name", "agency", "mission_type", "year_launched"]
};


class Modals extends React.Component {
	constructor (props) {
		super(props);

		this.state = { 
				modelType: this.props.modelType,
				filterBy: this.props.filterBy,
				value1: attrs[this.props.modelType][0],
				value2: ops[0],
				value3: compareTo[this.props.modelType][0]
			};

		this.onHandleChange1 = this.onHandleChange1.bind(this)	
		this.onHandleChange2 = this.onHandleChange2.bind(this)
		this.onHandleChange3 = this.onHandleChange3.bind(this)
	}

	onHandleChange1(event) {
		console.log("inside handle change 1 " + event.target.value);
		this.setState({
			value1: event.target.value
		});
	}
	onHandleChange2(event) {
		console.log("inside handle change 2 " + event.target.value);
		this.setState({
			value2: event.target.value
		});
	}
	onHandleChange3(event) {
		console.log("inside handle change 2 " + event.target.value);
		this.setState({
			value3: event.target.value
		});
	}		

	render () {
		return (
				<div>
	  				<button type="button" className="btn btn-primary" data-toggle="modal" data-target="#myModal" >Filter By</button>
	  				<div id="myModal" className="modal fade" role="dialog">
				  		<div className="modal-dialog">
				    		<div className="modal-content">
				      			<div className="modal-header">
					        		<button type="button" className="close" data-dismiss="modal">&times;</button>
					        		<h4 className="modal-title">Filtering</h4>
					      		</div>
					      		<div className="modal-body">
							      		<div className="form-group">
							      			<label>Attribute: 
								      			<select className="form-control" onChange={this.onHandleChange1} >
												  <option value="mass">Temperature</option>
												  <option value="diameter">Diameter</option>
												  <option value="gravity">Gravity</option>
												  <option value="temperature">Mass</option>
												</select>
											</label>
											<label>Operation: 
												<select className="form-control"  onChange={this.onHandleChange2} >
												  <option value="<">Less Than</option>
												  <option value="<=">Less Than or Equal To</option>
												  <option value=">">Greater Than</option>
												  <option value=">=">Greater Than or Equal To</option>
												  <option value="==">Equal To</option>
												  <option value="!=">Not Equal To</option>
												</select>
											</label>
											<label>Compare To: 
												<select className="form-control"  onChange={this.onHandleChange3} >
												  <option value="jupiter">Jupiter</option>
												</select>
											</label>
										</div>
					      		</div>
						      	<div className="modal-footer">
						      		<button type="button" className="btn btn-primary" data-dismiss="modal" onClick={() => this.state.filterBy(this.state.value1, this.state.value2, this.state.value3, 1)}>Submit</button>
						        	<button type="button" className="btn btn-default" data-dismiss="modal">Close</button>
						      	</div>
			    			</div>
				  		</div>
					</div>
				</div>
				);
	}

}

export default Modals;