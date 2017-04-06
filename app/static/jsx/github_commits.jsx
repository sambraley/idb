class Github_Commits extends React.Component {
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
			var count = 0;
			for (var i = 0; i < json.length; i += 1)
			{
				count += json[i].total;
			}
			this.state.count = count;
			this.forceUpdate();
		}
    render() {
        return (
					    <h3><strong>Overall Commits:</strong> {this.state.count}</h3>
				);
    }
}

export default Github_Commits;