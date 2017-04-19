import Highlighter from 'react-highlight-words'

var search = [];
if (window.location.href.indexOf('?') >= 0){
	search = window.location.href.split('?')[1].split('&')[0].split('=')[1].split('+');
}

var item_list = document.getElementsByClassName('react-highlight');
for (var i = 0; i < item_list.length; i += 1) {
	var temp = item_list[i];
	ReactDOM.render(
		<Highlighter className={temp.tagName} searchWords={search} textToHighlight={temp.innerHTML}/>,
		temp
	);
}