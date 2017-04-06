import Github_Commits from '../github_commits.jsx';
import Github_Issues from '../github_issues.jsx';

ReactDOM.render(
	<Github_Commits url="https://api.github.com/repos/samuelbraley/idb/stats/commit_activity"/>,
	document.getElementById('overall-commits')
);

ReactDOM.render(
	<Github_Issues url="https://api.github.com/repos/samuelbraley/idb/issues"/>,
	document.getElementById('overall-issues')
);
