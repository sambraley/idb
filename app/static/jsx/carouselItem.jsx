class CarouselItem extends React.Component {
    render() {
        return (
					    <div className={"item " + this.props.class}>
					    	<div className={"carousel-image"} style={{backgroundImage: 'url(' + this.props.url + ')'}}></div>
					    	<div className={"carousel-content center"}>
					        <h1>{this.props.message}</h1>
					      </div>
					    </div>
				);
    }
}

export default CarouselItem;