(function e(t,n,r){function s(o,u){if(!n[o]){if(!t[o]){var a=typeof require=="function"&&require;if(!u&&a)return a(o,!0);if(i)return i(o,!0);var f=new Error("Cannot find module '"+o+"'");throw f.code="MODULE_NOT_FOUND",f}var l=n[o]={exports:{}};t[o][0].call(l.exports,function(e){var n=t[o][1][e];return s(n?n:e)},l,l.exports,e,t,n,r)}return n[o].exports}var i=typeof require=="function"&&require;for(var o=0;o<r.length;o++)s(r[o]);return s})({1:[function(require,module,exports){
"use strict";

Object.defineProperty(exports, "__esModule", {
	value: true
});

var _createClass = function () { function defineProperties(target, props) { for (var i = 0; i < props.length; i++) { var descriptor = props[i]; descriptor.enumerable = descriptor.enumerable || false; descriptor.configurable = true; if ("value" in descriptor) descriptor.writable = true; Object.defineProperty(target, descriptor.key, descriptor); } } return function (Constructor, protoProps, staticProps) { if (protoProps) defineProperties(Constructor.prototype, protoProps); if (staticProps) defineProperties(Constructor, staticProps); return Constructor; }; }();

function _classCallCheck(instance, Constructor) { if (!(instance instanceof Constructor)) { throw new TypeError("Cannot call a class as a function"); } }

function _possibleConstructorReturn(self, call) { if (!self) { throw new ReferenceError("this hasn't been initialised - super() hasn't been called"); } return call && (typeof call === "object" || typeof call === "function") ? call : self; }

function _inherits(subClass, superClass) { if (typeof superClass !== "function" && superClass !== null) { throw new TypeError("Super expression must either be null or a function, not " + typeof superClass); } subClass.prototype = Object.create(superClass && superClass.prototype, { constructor: { value: subClass, enumerable: false, writable: true, configurable: true } }); if (superClass) Object.setPrototypeOf ? Object.setPrototypeOf(subClass, superClass) : subClass.__proto__ = superClass; }

var Github_Commits = function (_React$Component) {
	_inherits(Github_Commits, _React$Component);

	function Github_Commits(props) {
		_classCallCheck(this, Github_Commits);

		var _this = _possibleConstructorReturn(this, (Github_Commits.__proto__ || Object.getPrototypeOf(Github_Commits)).call(this, props));

		_this.state = {
			"count": 0
		};
		fetch(_this.props.url).then(function (r) {
			return r.json();
		}).then(function (data) {
			return _this.count_push(data);
		}).catch(function (e) {
			return console.log(e);
		});
		return _this;
	}

	_createClass(Github_Commits, [{
		key: "count_push",
		value: function count_push(json) {
			var count = 0;
			for (var i = 0; i < json.length; i += 1) {
				count += json[i].total;
			}
			this.state.count = count;
			this.forceUpdate();
		}
	}, {
		key: "render",
		value: function render() {
			return React.createElement(
				"h3",
				null,
				React.createElement(
					"strong",
					null,
					"Overall Commits:"
				),
				" ",
				this.state.count
			);
		}
	}]);

	return Github_Commits;
}(React.Component);

exports.default = Github_Commits;

},{}],2:[function(require,module,exports){
"use strict";

Object.defineProperty(exports, "__esModule", {
	value: true
});

var _createClass = function () { function defineProperties(target, props) { for (var i = 0; i < props.length; i++) { var descriptor = props[i]; descriptor.enumerable = descriptor.enumerable || false; descriptor.configurable = true; if ("value" in descriptor) descriptor.writable = true; Object.defineProperty(target, descriptor.key, descriptor); } } return function (Constructor, protoProps, staticProps) { if (protoProps) defineProperties(Constructor.prototype, protoProps); if (staticProps) defineProperties(Constructor, staticProps); return Constructor; }; }();

function _classCallCheck(instance, Constructor) { if (!(instance instanceof Constructor)) { throw new TypeError("Cannot call a class as a function"); } }

function _possibleConstructorReturn(self, call) { if (!self) { throw new ReferenceError("this hasn't been initialised - super() hasn't been called"); } return call && (typeof call === "object" || typeof call === "function") ? call : self; }

function _inherits(subClass, superClass) { if (typeof superClass !== "function" && superClass !== null) { throw new TypeError("Super expression must either be null or a function, not " + typeof superClass); } subClass.prototype = Object.create(superClass && superClass.prototype, { constructor: { value: subClass, enumerable: false, writable: true, configurable: true } }); if (superClass) Object.setPrototypeOf ? Object.setPrototypeOf(subClass, superClass) : subClass.__proto__ = superClass; }

var Github_Issues = function (_React$Component) {
	_inherits(Github_Issues, _React$Component);

	function Github_Issues(props) {
		_classCallCheck(this, Github_Issues);

		var _this = _possibleConstructorReturn(this, (Github_Issues.__proto__ || Object.getPrototypeOf(Github_Issues)).call(this, props));

		_this.state = {
			"count": 0
		};
		var closed = "?state=open";
		var open = "?state=closed";
		fetch(_this.props.url + closed).then(function (r) {
			return r.json();
		}).then(function (data) {
			return _this.count_push(data);
		}).catch(function (e) {
			return console.log(e);
		});
		fetch(_this.props.url + open).then(function (r) {
			return r.json();
		}).then(function (data) {
			return _this.count_push(data);
		}).catch(function (e) {
			return console.log(e);
		});
		return _this;
	}

	_createClass(Github_Issues, [{
		key: "count_push",
		value: function count_push(json) {
			this.state.count += json.length;
			this.forceUpdate();
		}
	}, {
		key: "render",
		value: function render() {
			return React.createElement(
				"h3",
				null,
				React.createElement(
					"strong",
					null,
					"Overall Issues:"
				),
				" ",
				this.state.count
			);
		}
	}]);

	return Github_Issues;
}(React.Component);

exports.default = Github_Issues;

},{}],3:[function(require,module,exports){
'use strict';

var _github_commits = require('../github_commits.jsx');

var _github_commits2 = _interopRequireDefault(_github_commits);

var _github_issues = require('../github_issues.jsx');

var _github_issues2 = _interopRequireDefault(_github_issues);

function _interopRequireDefault(obj) { return obj && obj.__esModule ? obj : { default: obj }; }

ReactDOM.render(React.createElement(_github_commits2.default, { url: 'https://api.github.com/repos/samuelbraley/idb/stats/commit_activity' }), document.getElementById('overall-commits'));

ReactDOM.render(React.createElement(_github_issues2.default, { url: 'https://api.github.com/repos/samuelbraley/idb/issues' }), document.getElementById('overall-issues'));

},{"../github_commits.jsx":1,"../github_issues.jsx":2}]},{},[3]);
