import ModelListItem from './model_list_item';

const ModelList = (props) => {
	const modelItem = props.models.map((model) => {
		return <ModelListItem model={model} /> 
	});
	return (
			<div className="row">
				{ modelItem }
			</div> 
		);
}


export default ModelList;