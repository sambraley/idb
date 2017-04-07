const selectOption = ({attr}) => {
	const label = {"name": "Name" , "temperature": "Temperature", "diameter": "Diameter", 
					"gravity": "Gravity", "mass": "Mass", "size": "Size", "agency": "Agency",
					"mission_type": "Mission Type", "year_launched": "Launch Year", 
					"<": "Less Than", "<=": "Less Than or Equal To", ">": "Greater Than", 
					">=": "Greater Than or Equal To", "==": "Equal To", "!=": "Not Equal To",
					"Earth": "Earth"};
	const attr2 = []; 
	attr.map((attr1) => {
		attr1.push(<option value={attr1}>{label[attr1]}</option>);
	});

	return (
			{attr2}
		);
}; 

export default selectOption;