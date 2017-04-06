
const PageItem = ({page_number, onPageSelect, isActive}) => {
	if (isActive === true) {
		return <li className="active" ><a>{page_number}</a></li>;
	}
	else{
		return <li onClick={() => onPageSelect(page_number)} className="page-item" ><a>{page_number}</a></li>;
	}
};
export default PageItem;
