import Github_Stats from '../github_stats.jsx';
import "isomorphic-fetch"

ReactDOM.render(
	<Github_Stats name="Overall Commits" url="https://api.github.com/repos/samuelbraley/idb/stats/commit_activity"/>,
	document.getElementById('overall-commits')
);
