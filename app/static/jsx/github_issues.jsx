class Github_Issues extends React.Component {
		constructor(props) {
			super(props);
			this.state = {
				"count": 0
			};
			var closed = "?state=open"
			var open = "?state=closed"
			fetch(this.props.url + closed).then(r => r.json())
			.then(data => this.count_push(data))
			.catch(e => console.log(e));
			fetch(this.props.url + open).then(r => r.json())
			.then(data => this.count_push(data))
			.catch(e => console.log(e));
		}
		count_push(json) {
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