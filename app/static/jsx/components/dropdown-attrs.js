const label = {"name": "Name" , "temperature": "Temperature", "diameter": "Diameter", 
					"gravity": "Gravity", "mass": "Mass", "size": "Size", "agency": "Agency",
					"mission_type": "Mission Type", "year_launched": "Launch Year", "Sorted By": "Sorted By"};

const Attribute = ({attr, sortBy, dir}) => {

	return (
			<li onClick={() => sortBy(attr, dir)} ><a>{label[attr]}</a></li>
		);
}; 

export default Attribute;