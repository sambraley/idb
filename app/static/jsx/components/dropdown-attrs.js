const Attribute = ({attr, sortBy, dir}) => {
	const label = {"name": "Name" , "temperature": "Temperature", "diameter": "Diameter", 
					"gravity": "Gravity", "mass": "Mass", "size": "Size", "agency": "Agency",
					"mission_type": "Mission Type", "year_launched": "Launch Year"};

	return (
			<li onClick={() => sortBy(attr, dir, label[attr], 1)} ><a>{label[attr]}</a></li>
		);
}; 

export default Attribute;