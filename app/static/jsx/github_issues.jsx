import "isomorphic-fetch";

class Github_Issues extends React.Component {
		constructor(props) {
			super(props);
			this.state = {
				"count": 0
			};
			var per_page = "&per_page=100";
			var token = "&access_token="+this.props.token + per_page;
			var state = "?state=all"+token;
			fetch(this.props.url + state).then(r => r.json())
			.then(data => this.count_push(data, 1))
			.catch(e => console.log(e));
		}
		count_push(json, page) {
			this.state.count += json.length;
			this.forceUpdate();
		}
    render() {
        return (
					    <h3><strong>Overall Issues:</strong> {this.state.count}</h3>
				);
    }
}

export default Github_Issues;