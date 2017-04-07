import PageItem from './page_item';

const Pages = ({current_page, total_pages, onPageSelect}) => {
	const pages = [];
	// Adding previous button
	if (current_page != 1) {
		pages.push(<li onClick={() => onPageSelect(current_page - 1)} className="page-item" key="previous-button"><a >Previous</a></li>);
	}
	//Setting list of page numbers
	var start;
	var end;
	if (total_pages <= 10) {
		end = total_pages;
		start = 1;
	}
	else if (10 >= current_page + 5) {
		end = 10;
		start = 1;
	}
	else if (total_pages > current_page + 5) {
		end = current_page + 5;
		start = end - 9;
	}
	else {
		end = total_pages;
		start = end - 9;
	}
	// creating pageItems
	for (var i = start; (i <= end && i <= total_pages) ; i++) {
		if (i === current_page) {
			pages.push(<PageItem 
							page_number={i} 
							onPageSelect={onPageSelect} 
							isActive={true} 
							key={i} />);
		}
		else {
			pages.push(<PageItem 
							page_number={i} 
							onPageSelect={onPageSelect} 
							isActive={false} 
							key={i} />);
		}
	}
	//adding next button
	if (current_page != total_pages && current_page > 1){
		pages.push(<li onClick={() => onPageSelect(current_page + 1)} className="page-item" key="next-button" ><a>Next</a></li>);
	}
	
	return (
			<ul className="pagination">
					{pages}
			</ul>
		);
};

export default Pages;
