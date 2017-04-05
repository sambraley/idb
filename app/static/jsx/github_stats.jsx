class Github_Stats extends React.Component {
		constructor(props) {
			super(props);
			this.state = {
				"count": 0
			};
			fetch(this.props.url).then(r => r.json())
			.then(data => this.count_push(data))
			.catch(e => console.log(e));
		}
		count_push(json) {
			this.state.count = json.length;
			console.log(json);
			this.forceUpdate();
		}
    render() {
        return (
					    <h3><strong>{this.props.name}:</strong> {this.state.count}</h3>
				);
    }
}

export default Github_Stats;