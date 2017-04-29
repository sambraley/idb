import Github_Member from './github_member.jsx'
import "isomorphic-fetch"

class Github_Member_Info extends React.Component {
		constructor(props) {
			super(props);
		}
    render() {
    	var url = this.props.url;
    	var member_list = this.props.member_info.map((member_info) =>
    		<Github_Member key={member_info.name} member_info={member_info} url={this.props.url} token={this.props.token}/>);
      return (<div>{member_list}</div>);
    }
}

export default Github_Member_Info;