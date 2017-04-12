import Github_Commits from '../github_commits.jsx';
import Github_Issues from '../github_issues.jsx';
import Github_Member_Info from '../github_member_info.jsx'

var access_token = "55dc1276759f6ff631870b2c509b632382276575";

var member_info = [
    {'name': 'Nick Kantor',    'github_id': 'njk464',       'image': 'nick_kantor.png',   'p1_lead': true,  'p2_lead': false, 'p3_lead': false, 'tests': 0,   'responsibilities': "Front-End Developer", 'bio': "I'm a Senior Computer Science student and tend to spend my free time playing my trumpet for the longhorn band. After I graduate I plan on pursuing a Master's degree in Information Security."},
    {'name': 'Samuel Braley',  'github_id': 'samuelbraley', 'image': 'samuel_braley.jpg', 'p1_lead': false, 'p2_lead': false, 'p3_lead': false, 'tests': 0,   'responsibilities': "Documentation and Apiary", 'bio': "I am a Computer Science senior with certificates in Business Foundations and Game Design. I enjoy being one of the many Sams in the world and plan on being a programmer manager after I graduate."},
    {'name': 'Taben Malik',    'github_id': 'tabenmalik',   'image': 'taben.jpg', 		  'p1_lead': false, 'p2_lead': false, 'p3_lead': false, 'tests': 0,   'responsibilities': "Data Collection and Modeling", 'bio': "A double major in Computer Science and Aerospace Engineering. I am a strong advocate of a Mars mission and hope to be a part of one someday."},
    {'name': 'Gustavo Osorio', 'github_id': 'lpztavo',      'image': 'gustavo.jpg',       'p1_lead': false, 'p2_lead': false, 'p3_lead': false, 'tests': 12,  'responsibilities': "UML Design and Modeling", 'bio': "I'm a senior Computer Science student. I enjoy dancing and coding, but I'm not skilled enough to do both simultaneously."},
    {'name': 'Scott Farrior',  'github_id': 'sfarrior',     'image': 'sfarrior.jpg',      'p1_lead': false, 'p2_lead': true,  'p3_lead': false, 'tests': 0,   'responsibilities': "Server setup/administration and SQLAlchemy backend", 'bio': "I'm a Computer Science major. I work as a TA/Grader as well as Computer Lab technician for the community college, and would like to be an instructor one day."},
    {'name': 'David Ares',     'github_id': 'dares23',      'image': 'david.jpg',         'p1_lead': false, 'p2_lead': false, 'p3_lead': true,  'tests': 0,   'responsibilities': "Front-End Developer", 'bio': "I am a non-traditional student with one year of Full-stack web development. Before returning to school, I gained seven years of experience in sales, marketing, and management."}]

ReactDOM.render(
	<Github_Commits url="https://api.github.com/repos/samuelbraley/idb/stats/commit_activity" token={access_token}/>,
	document.getElementById('overall-commits')
);

ReactDOM.render(
	<Github_Issues url="https://api.github.com/repos/samuelbraley/idb/issues" token={access_token}/>,
	document.getElementById('overall-issues')
);

ReactDOM.render(
	<Github_Member_Info member_info={member_info} url="https://api.github.com/repos/samuelbraley/idb" token={access_token}/>,
	document.getElementById('member-info')
);
