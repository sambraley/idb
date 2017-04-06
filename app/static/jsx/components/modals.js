
const Modals = () => {

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
				      			<div className="dropdown">
									<button className="btn dropdown-toggle" type="button" data-toggle="dropdown">Sort By  
								    <span className="caret"></span></button>
								    <ul className="dropdown-menu">
								    	<li className="dropdown-header">Ascending</li>
								      	<li className="dropdown-header">Descending</li>
								    </ul>
								</div>

				      		</div>
				      		
					      	<div className="modal-footer">
					        	<button type="button" className="btn btn-default" data-dismiss="modal">Close</button>
					      	</div>
		    			</div>
			  		</div>
				</div>
			</div>
			);

}

export default Modals;