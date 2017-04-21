import Highlighter from 'react-highlight-words'

class SearchListItem extends React.Component {
	constructor(props) {
		super(props);
		console.log(props.model);
		var base_url = "/" + this.props.model.model_type + "/";
		var link = base_url + this.props.model.pid;
		if (this.props.search !== undefined){
			link += "?q=" + this.props.search;
		}
		this.state = {
			link: link
		}
	}
	highlight(text, search, className) {
		if (search === undefined){
			search = "";
		}
		search = search.split('+');

		return (<Highlighter className={className} searchWords={search} textToHighlight={text}/>);
	}

	render() {
		return (
			<div className="search-item">
				<a href={this.state.link}>
					{this.highlight(this.props.model.name, this.props.search, "h3")}
				</a>
				<div className="attributes">
					{this.props.model.model_type === "satellites" &&
						<p>Model Type: Satellite</p>
				    }
				    {this.props.model.model_type === "planets" &&
						<p>Model Type: Planet</p>
				    }
				    {this.props.model.model_type === "galaxies" &&
						<p>Model Type: Galaxy</p>
				    }
				    {this.props.model.model_type === "stars" &&
						<p>Model Type: Star</p>
				    }
			    </div>
			</div> 
			);
	}
};


export default SearchListItem;