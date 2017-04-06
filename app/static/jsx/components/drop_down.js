import Attribute from "./dropdown-attrs";

const attrs = {
	"planets": ["name", "temperature", "diameter", "gravity", "mass"],
	"galaxies": ["name", "size"],
	"stars": ["name", "diameter", "temperature"],
	"satellites": ["name", "agency", "mission_type", "year_launched"]
}


const DropDown = ({modelType, sortBy, sort_title}) => { 
	const dir1 = "asc";
	const dir2 = "desc";
	const attrItem1 = attrs[modelType].map((attr) => {
		return <Attribute 
					attr={attr}
					sortBy={sortBy}
					dir={dir1}
					key={attr} /> 
	});
	const attrItem2 = attrs[modelType].map((attr) => {
		return <Attribute 
					attr={attr}
					sortBy={sortBy}
					dir={dir2}
					key={attr} /> 
	});
	return (
			<div className="dropdown">
				<button className="btn btn-primary dropdown-toggle" type="button" data-toggle="dropdown">{sort_title}  
			    <span className="caret"></span></button>
			    <ul className="dropdown-menu">
			    	<li className="dropdown-header">Ascending</li>
			      		{attrItem1}
			      	<li className="divider"></li>
			      	<li className="dropdown-header">Descending</li>
			      		{attrItem2}
			    </ul>
			</div>

		);
};



export default DropDown;
