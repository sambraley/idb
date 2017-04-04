import ModelListItem from './model_list_item';

const ModelList = (props) => {
	if (!props){
		console.log("nothing in props");
		return <div>Loading...</div>;
	}

	const modelItem = props.models.map((model) => {
		return <ModelListItem 
					key={model.pid} 
					model={model} /> 
	});
	return (
			<div className="row">
				{ modelItem }
			</div> 
		);
}


export default ModelList;