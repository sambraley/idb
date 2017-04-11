import "isomorphic-fetch";

class Github_Member extends React.Component {
		constructor(props) {
			super(props);
			this.state = {
				"commits": 0,
				"issues": 0
			};
			var per_page = "&per_page=100";
			var token = "&access_token="+this.props.token + per_page;
			var commits = "/commits?author="+this.props.member_info["github_id"] + token;
			var issues = "/issues?state=all&creator="+this.props.member_info["github_id"] + token;
			fetch(this.props.url + commits).then(r => r.json())
			.then(data => this.count_commits(data))
			.catch(e => console.log(e));
			fetch(this.props.url + issues).then(r => r.json())
			.then(data => this.count_issues(data))
			.catch(e => console.log(e));
		}
		count_commits(json) {
			this.state.commits += json.length;
			this.forceUpdate();
		}
		count_issues(json) {
			this.state.issues += json.length;
			this.forceUpdate();
		}
    render() {
    		var info = (
    			<div className="col-md-4 text-center service-box">
      			<img className="img-thumbnail about-image" src={"/static/images/" + this.props.member_info['image']} />
      			<h3>{this.props.member_info["name"]}</h3>
			      <p className="text-muted">{this.props.member_info["bio"]}</p>
			      <p className="text-muted"><strong>Major Responsibilites:</strong> {this.props.member_info["responsibilities"]}</p>
			      <p className="text-muted"><strong>Commits:</strong> {this.state.commits}</p>
			      <p className="text-muted"><strong>Issues:</strong> {this.state.issues}</p>
			      <p className="text-muted"><strong>Unit tests:</strong> {this.props.member_info["tests"]}</p>
			      {this.props.member_info["p1_lead"] ? (
             		<p className="text-muted"><strong>Phase 1 Leader</strong></p>
            	  ):null}
            	  {this.props.member_info["p2_lead"] ? (
              	    <p className="text-muted"><strong>Phase 2 Leader</strong></p>
            	  ):null}
            	  {this.props.member_info["p3_lead"] ? (
              	    <p className="text-muted"><strong>Phase 3 Leader</strong></p>
            	  ):null}
  				</div>
  			);
        return info;
    }
}

export default Github_Member;