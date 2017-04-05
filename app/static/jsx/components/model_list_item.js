
const ModelListItem = ({model}) => {
	const link = "/" + window.location.href.split('/')[3] + "/" + model.pid;
	return (
		<div className="col-md-4 text-center model-list-item">
			<a href={link}>
				<img className="img-thumbnail about-image" src="/static/images/HAT-P-33.png" />
				<h3>{model.name}</h3>
			</a>
		</div> 
		);
};


export default ModelListItem;