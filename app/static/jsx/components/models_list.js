import ModelListItem from './model_list_item';

const ModelList = (props) => {
	//console.log(props);
	console.log(props.models.length)
	const modelItem = props.models.map((model) => {
		return <ModelListItem 
					key={model.pid} 
					model={model} /> 
	});
	console.log(modelItem);
	return (
			<div className="row">
				{ modelItem }
			</div> 
		);
}


export default ModelList;