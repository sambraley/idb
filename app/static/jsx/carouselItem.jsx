class CarouselItem extends React.Component {
    render() {
        return (
					    <div className={"item " + this.props.class}>
					    	<div className={"carousel-image"} style={{backgroundImage: 'url(' + this.props.url + ')'}}></div>
					    </div>
				);
    }
}

export default CarouselItem;