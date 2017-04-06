class Github_Member extends React.Component {
		constructor(props) {
			super(props);
		}
    render() {
    		var info = (
    			<div className="col-md-4 text-center service-box">
      			<img className="img-thumbnail about-image" src={"/static/images/" + this.props.member_info['image']} />
      			<h3>{this.props.member_info["name"]}</h3>
			      <p className="text-muted">{this.props.member_info["bio"]}</p>
			      <p className="text-muted"><strong>Major Responsibilites:</strong> {this.props.member_info["responsibilities"]}</p>
			      <p className="text-muted"><strong>Commits:</strong> 0</p>
			      <p className="text-muted"><strong>Issues:</strong> 0</p>
			      <p className="text-muted"><strong>Unit tests:</strong> {this.props.member_info["tests"]}</p>
			      {this.props.member_info["p1_lead"] ? (
              <p className="text-muted"><strong>Phase 1 Leader</strong></p>
            ):null}
            {this.props.member_info["p2_lead"] ? (
              <p className="text-muted"><strong>Phase 2 Leader</strong></p>
            ):null}
  				</div>
  			);
        return info;
    }
}

export default Github_Member;