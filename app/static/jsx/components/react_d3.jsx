class React_D3 extends React.Component {
	constructor(props) {
		super(props);
		this.state = {
			visualization: "albums"
		};
	}
	changeVisual(v_class) {
		this.setState({
			visualization: v_class
		})
	}
    render() {
        return (
        		<div>
		        	<h1 className="text-center">Boswemian Visualizations</h1>
					<div className="dropdown">
					    <button className="btn btn-primary dropdown-toggle" type="button" data-toggle="dropdown">Choose a visualization
					    <span className="caret"></span></button>
					    <ul className="dropdown-menu">
					        <li onClick={() => this.changeVisual("albums")}><a >Bubble Visualization of Albums</a></li>
					        <li onClick={() => this.changeVisual("adjacency")}><a>Adjacency Matrix of Artists and Venues</a></li>
					        <li onClick={() => this.changeVisual("geographic")}><a>Geographic Map for Concerts</a></li>
					    </ul>
					</div>
					<svg className={"center-block " + this.state.visualization} width="960" height="960" fontFamily="sans-serif" fontSize="10" textAnchor="middle"></svg>
        		</div>
        		);
    }
}

export default React_D3;