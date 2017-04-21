import selectOption from './select_options';

const attrs = {
	"planets": ["diameter", "gravity", "mass"],
	"galaxies": ["size"],
	"stars": ["mass", "diameter"],
	"satellites": ["year_launched"]
};
const ops = ["<", "<=", ">", ">=", "!="];
const compareTo = {
	"planets": [1.0],
	"galaxies": [1.0],
	"stars": [1.0],
	"satellites": [2012]
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
		var v3 = 1;
		console.log("inside handle change 2 " + event.target.value);
		if (this.state.modelType == "satellites") {
			v3 = parseInt(event.target.value);
		}
		console.log(v3);
		this.setState({
			value3: v3
		});
	}		

	render () {
		console.log(this.state.modelType);
		if (this.state.modelType === "planets"){
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
													<option value="diameter">Diameter</option>
												  	<option value="gravity">Gravity</option>
												  	<option value="mass">Mass</option>
												</select>
											</label>
											<label>Operation: 
												<select className="form-control"  onChange={this.onHandleChange2} >
											 		<option value="<">Less Than</option>
												  	<option value="<=">Less Than or Equal To</option>
												  	<option value=">">Greater Than</option>
												  	<option value=">=">Greater Than or Equal To</option>
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
		if (this.state.modelType === "galaxies") {
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
												  <option value="size">Size</option>
												</select>
											</label>
											<label>Operation: 
												<select className="form-control"  onChange={this.onHandleChange2} >
												  <option value="<">Less Than</option>
												  <option value="<=">Less Than or Equal To</option>
												  <option value=">">Greater Than</option>
												  <option value=">=">Greater Than or Equal To</option>
												  <option value="!=">Not Equal To</option>
												</select>
											</label>
											<label>Compare To: 
												<select className="form-control"  onChange={this.onHandleChange3} >
												  <option value="milkyway">Milky Way</option>
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
		if (this.state.modelType === "stars") {
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
												  <option value="mass">Mass</option>
												  <option value="diameter">Diameter</option>
												</select>
											</label>
											<label>Operation: 
												<select className="form-control"  onChange={this.onHandleChange2} >
												  <option value="<">Less Than</option>
												  <option value="<=">Less Than or Equal To</option>
												  <option value=">">Greater Than</option>
												  <option value=">=">Greater Than or Equal To</option>
												  <option value="!=">Not Equal To</option>
												</select>
											</label>
											<label>Compare To: 
												<select className="form-control"  onChange={this.onHandleChange3} >
												  <option value="sun">The Sun</option>
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
		if (this.state.modelType === "satellites") {
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
												  <option value="year_launched">Launch Year</option>
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
												  <option value="2012">2012</option>
												  <option value="2013">2013</option>
												  <option value="2014">2014</option>
												  <option value="2015">2015</option>
												  <option value="2016">2016</option>
												  <option value="2017">2017</option>
												  <option value="2018">2018</option>
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

}

export default Modals;