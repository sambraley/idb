
class Modals extends React.Component {
	constructor (props) {
		super(props);

		this.state = { 
				modelType: this.props.modelType,
				filterBy: this.props.filterBy,
				value1: null,
				value2: null,
				value3: null
			};
	}

	onHandleChange(event) {
		console.log("inside handle change " + event.target.value);
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
							      			<select className="form-control" value={this.state.value1} onChange={this.onHandleChange} >
											  <option value="Attribute">Attribute</option>
											  <option value="Attr1">Attr 1</option>
											  <option value="Attr2">Attr 2</option>
											</select>
											<select className="form-control" value={this.state.value2} onChange={this.onHandleChange} >
											  <option value="Attribute">Operation</option>
											  <option value=">">Greater Then</option>
											  <option value="<">Greater Then</option>
											</select>
											<select className="form-control" value={this.state.value3} onChange={this.onHandleChange} >
											  <option value="Attribute">Compare To</option>
											  <option value="Attr1">Jupiter</option>
											  <option value="Attr2">Earth</option>
											</select>
										</div>
					      		</div>
						      	<div className="modal-footer">
						      		<button type="button" className="btn btn-primary" data-dismiss="modal" onClick={() => this.state.filterBy()}>Submit</button>
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