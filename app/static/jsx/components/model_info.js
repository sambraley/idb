
const ModelInfo = ({model}) => {
	console.log("in model info, got model id: " + model.pid);
	console.log(model);
	var link = "/static/images/HAT-P-33%20b.png";
	//var aladin = A.aladin('#aladin-lite-div', {survey: "P/DSS2/color", fov:60});
	//var aladinEmbed = aladin.getEmbedCode();
	return (
		<div>
			<div className="row">
			  	<div className="col-lg-12 text-center">
			  		<h1>{model.name}</h1>
			  	</div>
			</div>
			<div className="row">
				<div className="col-md-6 text-center" styles="padding-top:40px;">
					<img src="/static/images/HAT-P-33%20b.png"></img>
				</div>
			    <div className="col-md-6 text-center">
					<div className="col-md-12">
						<h3>Diameter:</h3><p>{model.diameter}</p>
						<h3>Surface Temperatures:</h3><p>{model.surface_temperature}</p>
						<h3>Right Ascension:</h3><p>{model.ra}</p>
						<h3>Declination:</h3><p>{model.dec}</p>
						<h3>Mass:</h3><p>{model.mass}</p>
						<h3>Temperature:</h3><p>{model.temperature}</p>
						<h3>Gravity:</h3><p>{model.gravity}</p>
						<h3>Orbital Period:</h3><p>{model.orbital_period}</p>
						<h3>Orbiting Bodies:</h3><p>{model.orbiting_bodies}</p>
					</div> 
			    </div> 
			</div>
		</div>
		);
};


export default ModelInfo;