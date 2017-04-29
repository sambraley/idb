const attrs = {
	"planets": ["diameter", "gravity", "mass"],
	"galaxies": ["size"],
	"stars": ["mass", "diameter"],
	"satellites": ["year_launched"]
};
const units = {
	"planets": {"diameter": "X Jupiter's Diameter", "gravity": "X Jupiter's Gravity", "mass": "X Jupiter's Mass"},
	"galaxies": {"size": "Arcminutes"},
	"stars": {"mass": "Solar Mass", "diameter": "Solar Diameter"},
	"satellites": {"year_launched": "Earth Years"}
};
const label = {"name": "Name" , "temperature": "Temperature", "diameter": "Diameter", 
	"gravity": "Gravity", "mass": "Mass", "size": "Size", "agency": "Agency",
	"mission_type": "Mission Type", "year_launched": "Launch Year", 
	"<": "Less Than", "<=": "Less Than or Equal To", ">": "Greater Than", 
	">=": "Greater Than or Equal To", "==": "Equal To", "!=": "Not Equal To",
};
const ops = ["<", "<=", ">", ">=", "==", "!="];
const compareTo = {
	"planets": [1.0],
	"galaxies": [1.0],
	"stars": [1.0],
	"satellites": [2012]
};
const ref = {
	"planets": "Earth",
	"galaxies": "the Milky Way",
	"stars": "the Sun",
	"satellites": "Saral"
};
const values = {
	"planets": {"diameter": "0.09113015119223013", "gravity": "0.3788780184698508", "mass": "0.003146469968387777"},
	"galaxies": {"size": "360.0"},
	"stars": {"mass": "1.0", "diameter": "1.0"},
	"satellites": {"year_launched": "2013"}
};

class Modals extends React.Component {
	constructor (props) {
		super(props);

		this.state = { 
				modelType: this.props.modelType,
				filterBy: this.props.filterBy,
				attributes: attrs[this.props.modelType],
				value1: attrs[this.props.modelType][0],
				value2: ops[0],
				value3: compareTo[this.props.modelType][0]
			};

		this.onHandleChange1 = this.onHandleChange1.bind(this);	
		this.onHandleChange2 = this.onHandleChange2.bind(this);
		this.onHandleChange3 = this.onHandleChange3.bind(this);
		this.get_units       = this.get_units.bind(this);
		this.get_attributes  = this.get_attributes.bind(this);
		this.get_comparisons = this.get_comparisons.bind(this);
		this.get_description = this.get_description.bind(this);
	}
	get_units() {
		return units[this.state.modelType][this.state.value1];
	}
	get_attributes() {
		var attributes = this.state.attributes.map((a) =>
    		<option key={a} value={a}>{label[a]}</option>);
    return (<select className="form-control" onChange={this.onHandleChange1}>{attributes}</select>);
	}
	get_comparisons() {
		var comparisons = ops.map((o) =>
    		<option key={o} value={o}>{ops[o]}</option>);
    return (<select className="form-control" onChange={this.onHandleChange1}>{attributes}</select>);
	}
	get_description() {
		var description = "";
		description += "For reference " + ref[this.state.modelType];
		description += " has a " + label[this.state.value1] + " of ";
		description += values[this.state.modelType][this.state.value1] + " ";
		description += units[this.state.modelType][this.state.value1] + ".";
		return description;
	}
	onHandleChange1(event) {
		this.setState({
			value1: event.target.value
		});
	}
	onHandleChange2(event) {
		this.setState({
			value2: event.target.value
		});
	}
	onHandleChange3(event) {
		this.setState({
			value3: event.target.value.toString()
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
						      		{this.get_attributes()}
										</label>
										<br/>
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
										<br/>
										<label className="inline">Compare To: 
											<br/>
											<input className="filter-input" type="number" step="any" onChange={this.onHandleChange3} />
											<inline>{this.get_units()}</inline>
										</label>
										<br/>
										<p>{this.get_description()}</p>
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