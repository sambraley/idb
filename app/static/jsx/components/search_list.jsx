import SearchListItem from './search_list_item.jsx';

const SearchList = (props) => {
	const searchItem = props.models.map((model) => {
		return <SearchListItem model={model} search={props.search}/> 
	});
	return (
			<div className="row">
				{ searchItem }
			</div> 
		);
}


export default SearchList;