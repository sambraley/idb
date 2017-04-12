
const ModelListItem = ({model}) => {
	const link = "/" + window.location.href.split('/')[3] + "/" + model.pid;
	const image_url = model.img_url;
	const style = {
		width: '400px',
		height: '400px'
	};
	return (
		<div className="col-lg-4 col-md-6 col-sm-12 text-center model-list-item">
			<a href={link}>
				<img className="img-thumbnail about-image" style={style} src={image_url} />
				<h3>{model.name}</h3>
			</a>
		</div> 
		);
};


export default ModelListItem;