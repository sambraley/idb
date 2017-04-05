

class DropDown extends React.Component { 
	render() {
		return (
				<div className="sort-container col-sm-2" id="sort-toolbar-container">
	          		<select className="form-control" id="sort-dropdown" data-ui="sort-container">
	            		<option value="title" data-ui="sort-item">Sort By</option>
	           			<option value="title" data-ui="sort-item">A - Z</option>
	            		<option value="title_r" data-ui="sort-item">Z - A</option>
	         		</select>
    			</div>
			);
	}
};

export default DropDown;
