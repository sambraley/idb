(function e(t,n,r){function s(o,u){if(!n[o]){if(!t[o]){var a=typeof require=="function"&&require;if(!u&&a)return a(o,!0);if(i)return i(o,!0);var f=new Error("Cannot find module '"+o+"'");throw f.code="MODULE_NOT_FOUND",f}var l=n[o]={exports:{}};t[o][0].call(l.exports,function(e){var n=t[o][1][e];return s(n?n:e)},l,l.exports,e,t,n,r)}return n[o].exports}var i=typeof require=="function"&&require;for(var o=0;o<r.length;o++)s(r[o]);return s})({1:[function(require,module,exports){
"use strict";

Object.defineProperty(exports, "__esModule", {
	value: true
});

var _createClass = function () { function defineProperties(target, props) { for (var i = 0; i < props.length; i++) { var descriptor = props[i]; descriptor.enumerable = descriptor.enumerable || false; descriptor.configurable = true; if ("value" in descriptor) descriptor.writable = true; Object.defineProperty(target, descriptor.key, descriptor); } } return function (Constructor, protoProps, staticProps) { if (protoProps) defineProperties(Constructor.prototype, protoProps); if (staticProps) defineProperties(Constructor, staticProps); return Constructor; }; }();

require("isomorphic-fetch");

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
		var per_page = "&per_page=100";
		var token = "?access_token=" + _this.props.token + per_page;
		fetch(_this.props.url + token).then(function (r) {
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

},{"isomorphic-fetch":7}],2:[function(require,module,exports){
"use strict";

Object.defineProperty(exports, "__esModule", {
	value: true
});

var _createClass = function () { function defineProperties(target, props) { for (var i = 0; i < props.length; i++) { var descriptor = props[i]; descriptor.enumerable = descriptor.enumerable || false; descriptor.configurable = true; if ("value" in descriptor) descriptor.writable = true; Object.defineProperty(target, descriptor.key, descriptor); } } return function (Constructor, protoProps, staticProps) { if (protoProps) defineProperties(Constructor.prototype, protoProps); if (staticProps) defineProperties(Constructor, staticProps); return Constructor; }; }();

require("isomorphic-fetch");

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
		var per_page = "&per_page=100";
		var token = "&access_token=" + _this.props.token + per_page;
		var state = "?state=all" + token;
		fetch(_this.props.url + state).then(function (r) {
			return r.json();
		}).then(function (data) {
			return _this.count_push(data, 1);
		}).catch(function (e) {
			return console.log(e);
		});
		return _this;
	}

	_createClass(Github_Issues, [{
		key: "count_push",
		value: function count_push(json, page) {
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

},{"isomorphic-fetch":7}],3:[function(require,module,exports){
"use strict";

Object.defineProperty(exports, "__esModule", {
	value: true
});

var _createClass = function () { function defineProperties(target, props) { for (var i = 0; i < props.length; i++) { var descriptor = props[i]; descriptor.enumerable = descriptor.enumerable || false; descriptor.configurable = true; if ("value" in descriptor) descriptor.writable = true; Object.defineProperty(target, descriptor.key, descriptor); } } return function (Constructor, protoProps, staticProps) { if (protoProps) defineProperties(Constructor.prototype, protoProps); if (staticProps) defineProperties(Constructor, staticProps); return Constructor; }; }();

require("isomorphic-fetch");

function _classCallCheck(instance, Constructor) { if (!(instance instanceof Constructor)) { throw new TypeError("Cannot call a class as a function"); } }

function _possibleConstructorReturn(self, call) { if (!self) { throw new ReferenceError("this hasn't been initialised - super() hasn't been called"); } return call && (typeof call === "object" || typeof call === "function") ? call : self; }

function _inherits(subClass, superClass) { if (typeof superClass !== "function" && superClass !== null) { throw new TypeError("Super expression must either be null or a function, not " + typeof superClass); } subClass.prototype = Object.create(superClass && superClass.prototype, { constructor: { value: subClass, enumerable: false, writable: true, configurable: true } }); if (superClass) Object.setPrototypeOf ? Object.setPrototypeOf(subClass, superClass) : subClass.__proto__ = superClass; }

var Github_Member = function (_React$Component) {
	_inherits(Github_Member, _React$Component);

	function Github_Member(props) {
		_classCallCheck(this, Github_Member);

		var _this = _possibleConstructorReturn(this, (Github_Member.__proto__ || Object.getPrototypeOf(Github_Member)).call(this, props));

		_this.state = {
			"commits": 0,
			"issues": 0
		};
		var per_page = "&per_page=100";
		var token = "&access_token=" + _this.props.token + per_page;
		for (var i = 0; i < _this.props.member_info["github_id"].length; i += 1) {
			var commits = "/commits?author=" + _this.props.member_info["github_id"][i] + token;
			var issues = "/issues?state=all&creator=" + _this.props.member_info["github_id"][i] + token;
			fetch(_this.props.url + commits).then(function (r) {
				return r.json();
			}).then(function (data) {
				return _this.count_commits(data, _this.props.url + commits, 1);
			}).catch(function (e) {
				return console.log(e);
			});
			fetch(_this.props.url + issues).then(function (r) {
				return r.json();
			}).then(function (data) {
				return _this.count_issues(data);
			}).catch(function (e) {
				return console.log(e);
			});
		}

		return _this;
	}

	_createClass(Github_Member, [{
		key: "count_commits",
		value: function count_commits(json, url, page) {
			var _this2 = this;

			this.state.commits += json.length;
			this.forceUpdate();
			page += 1;
			if (json.length == 100) {
				fetch(url + "&page=" + page).then(function (r) {
					return r.json();
				}).then(function (data) {
					return _this2.count_commits(data, url, page);
				}).catch(function (e) {
					return console.log(e);
				});
			}
		}
	}, {
		key: "count_issues",
		value: function count_issues(json) {
			this.state.issues += json.length;
			this.forceUpdate();
		}
	}, {
		key: "render",
		value: function render() {
			var info = React.createElement(
				"div",
				{ className: "col-md-6 col-lg-4 text-center service-box" },
				React.createElement("img", { className: "img-thumbnail about-image", src: "/static/images/" + this.props.member_info['image'] }),
				React.createElement(
					"h3",
					null,
					this.props.member_info["name"]
				),
				React.createElement(
					"p",
					{ className: "text-muted" },
					this.props.member_info["bio"]
				),
				React.createElement(
					"p",
					{ className: "text-muted" },
					React.createElement(
						"strong",
						null,
						"Major Responsibilites:"
					),
					" ",
					this.props.member_info["responsibilities"]
				),
				React.createElement(
					"p",
					{ className: "text-muted" },
					React.createElement(
						"strong",
						null,
						"Commits:"
					),
					" ",
					this.state.commits
				),
				React.createElement(
					"p",
					{ className: "text-muted" },
					React.createElement(
						"strong",
						null,
						"Issues:"
					),
					" ",
					this.state.issues
				),
				React.createElement(
					"p",
					{ className: "text-muted" },
					React.createElement(
						"strong",
						null,
						"Unit tests:"
					),
					" ",
					this.props.member_info["tests"]
				),
				this.props.member_info["p1_lead"] ? React.createElement(
					"p",
					{ className: "text-muted" },
					React.createElement(
						"strong",
						null,
						"Phase 1 Leader"
					)
				) : null,
				this.props.member_info["p2_lead"] ? React.createElement(
					"p",
					{ className: "text-muted" },
					React.createElement(
						"strong",
						null,
						"Phase 2 Leader"
					)
				) : null,
				this.props.member_info["p3_lead"] ? React.createElement(
					"p",
					{ className: "text-muted" },
					React.createElement(
						"strong",
						null,
						"Phase 3 Leader"
					)
				) : null
			);
			return info;
		}
	}]);

	return Github_Member;
}(React.Component);

exports.default = Github_Member;

},{"isomorphic-fetch":7}],4:[function(require,module,exports){
"use strict";

Object.defineProperty(exports, "__esModule", {
  value: true
});

var _createClass = function () { function defineProperties(target, props) { for (var i = 0; i < props.length; i++) { var descriptor = props[i]; descriptor.enumerable = descriptor.enumerable || false; descriptor.configurable = true; if ("value" in descriptor) descriptor.writable = true; Object.defineProperty(target, descriptor.key, descriptor); } } return function (Constructor, protoProps, staticProps) { if (protoProps) defineProperties(Constructor.prototype, protoProps); if (staticProps) defineProperties(Constructor, staticProps); return Constructor; }; }();

var _github_member = require("./github_member.jsx");

var _github_member2 = _interopRequireDefault(_github_member);

require("isomorphic-fetch");

function _interopRequireDefault(obj) { return obj && obj.__esModule ? obj : { default: obj }; }

function _classCallCheck(instance, Constructor) { if (!(instance instanceof Constructor)) { throw new TypeError("Cannot call a class as a function"); } }

function _possibleConstructorReturn(self, call) { if (!self) { throw new ReferenceError("this hasn't been initialised - super() hasn't been called"); } return call && (typeof call === "object" || typeof call === "function") ? call : self; }

function _inherits(subClass, superClass) { if (typeof superClass !== "function" && superClass !== null) { throw new TypeError("Super expression must either be null or a function, not " + typeof superClass); } subClass.prototype = Object.create(superClass && superClass.prototype, { constructor: { value: subClass, enumerable: false, writable: true, configurable: true } }); if (superClass) Object.setPrototypeOf ? Object.setPrototypeOf(subClass, superClass) : subClass.__proto__ = superClass; }

var Github_Member_Info = function (_React$Component) {
  _inherits(Github_Member_Info, _React$Component);

  function Github_Member_Info(props) {
    _classCallCheck(this, Github_Member_Info);

    return _possibleConstructorReturn(this, (Github_Member_Info.__proto__ || Object.getPrototypeOf(Github_Member_Info)).call(this, props));
  }

  _createClass(Github_Member_Info, [{
    key: "render",
    value: function render() {
      var _this2 = this;

      var url = this.props.url;
      var member_list = this.props.member_info.map(function (member_info) {
        return React.createElement(_github_member2.default, { member_info: member_info, url: _this2.props.url, token: _this2.props.token });
      });
      return React.createElement(
        "div",
        null,
        member_list
      );
    }
  }]);

  return Github_Member_Info;
}(React.Component);

exports.default = Github_Member_Info;

},{"./github_member.jsx":3,"isomorphic-fetch":7}],5:[function(require,module,exports){
"use strict";

Object.defineProperty(exports, "__esModule", {
  value: true
});

var _createClass = function () { function defineProperties(target, props) { for (var i = 0; i < props.length; i++) { var descriptor = props[i]; descriptor.enumerable = descriptor.enumerable || false; descriptor.configurable = true; if ("value" in descriptor) descriptor.writable = true; Object.defineProperty(target, descriptor.key, descriptor); } } return function (Constructor, protoProps, staticProps) { if (protoProps) defineProperties(Constructor.prototype, protoProps); if (staticProps) defineProperties(Constructor, staticProps); return Constructor; }; }();

require("isomorphic-fetch");

function _classCallCheck(instance, Constructor) { if (!(instance instanceof Constructor)) { throw new TypeError("Cannot call a class as a function"); } }

function _possibleConstructorReturn(self, call) { if (!self) { throw new ReferenceError("this hasn't been initialised - super() hasn't been called"); } return call && (typeof call === "object" || typeof call === "function") ? call : self; }

function _inherits(subClass, superClass) { if (typeof superClass !== "function" && superClass !== null) { throw new TypeError("Super expression must either be null or a function, not " + typeof superClass); } subClass.prototype = Object.create(superClass && superClass.prototype, { constructor: { value: subClass, enumerable: false, writable: true, configurable: true } }); if (superClass) Object.setPrototypeOf ? Object.setPrototypeOf(subClass, superClass) : subClass.__proto__ = superClass; }

var url = "/run_tests";

var React_Tests = function (_React$Component) {
  _inherits(React_Tests, _React$Component);

  function React_Tests(props) {
    _classCallCheck(this, React_Tests);

    var _this = _possibleConstructorReturn(this, (React_Tests.__proto__ || Object.getPrototypeOf(React_Tests)).call(this, props));

    _this.state = {
      "test_output": "Running Tests"
    };
    _this.run_tests = _this.run_tests.bind(_this);
    _this.update_state = _this.update_state.bind(_this);
    return _this;
  }

  _createClass(React_Tests, [{
    key: "run_tests",
    value: function run_tests() {
      var _this2 = this;

      fetch(url).then(function (r) {
        return r.text();
      }).then(function (data) {
        return _this2.update_state(data);
      }).catch(function (e) {
        return console.log(e);
      });
    }
  }, {
    key: "update_state",
    value: function update_state(data) {
      this.state.test_output = data;
      this.forceUpdate();
    }
  }, {
    key: "render",
    value: function render() {
      return React.createElement(
        "div",
        null,
        React.createElement(
          "div",
          { className: "col-md-4 text-center" },
          React.createElement(
            "a",
            { href: "https://github.com/samuelbraley/idb" },
            "Repository"
          )
        ),
        React.createElement(
          "div",
          { className: "col-md-4 text-center" },
          React.createElement(
            "a",
            { href: "https://github.com/samuelbraley/idb/issues" },
            "Issue Tracker"
          )
        ),
        React.createElement(
          "div",
          { className: "col-md-4 text-center" },
          React.createElement(
            "a",
            { href: "http://docs.spacecowboys.apiary.io" },
            "Rest API"
          )
        ),
        React.createElement(
          "div",
          { className: "col-md-4 text-center" },
          React.createElement(
            "a",
            { id: "test-link", "data-toggle": "modal", "data-target": "#myModal", onClick: this.run_tests },
            "Run Unit Tests"
          )
        ),
        React.createElement(
          "div",
          { className: "col-md-4 text-center" },
          React.createElement(
            "a",
            { href: "/visualization" },
            "Visualizations of BoswemianRhapsody.me"
          )
        ),
        React.createElement(
          "div",
          null,
          React.createElement(
            "div",
            { id: "myModal", className: "modal fade", role: "dialog" },
            React.createElement(
              "div",
              { className: "modal-dialog" },
              React.createElement(
                "div",
                { className: "modal-content" },
                React.createElement(
                  "div",
                  { className: "modal-header" },
                  React.createElement(
                    "button",
                    { type: "button", className: "close", "data-dismiss": "modal" },
                    "\xD7"
                  ),
                  React.createElement(
                    "h4",
                    { className: "modal-title" },
                    "Test Results"
                  )
                ),
                React.createElement(
                  "div",
                  { className: "modal-body" },
                  React.createElement(
                    "pre",
                    null,
                    this.state.test_output
                  )
                ),
                React.createElement(
                  "div",
                  { className: "modal-footer" },
                  React.createElement(
                    "button",
                    { type: "button", className: "btn btn-primary", onClick: this.run_tests },
                    "Rerun tests"
                  )
                )
              )
            )
          )
        )
      );
    }
  }]);

  return React_Tests;
}(React.Component);

exports.default = React_Tests;

},{"isomorphic-fetch":7}],6:[function(require,module,exports){
'use strict';

var _github_commits = require('../components/github_commits.jsx');

var _github_commits2 = _interopRequireDefault(_github_commits);

var _github_issues = require('../components/github_issues.jsx');

var _github_issues2 = _interopRequireDefault(_github_issues);

var _github_member_info = require('../components/github_member_info.jsx');

var _github_member_info2 = _interopRequireDefault(_github_member_info);

var _reactTest = require('../components/react-test.jsx');

var _reactTest2 = _interopRequireDefault(_reactTest);

function _interopRequireDefault(obj) { return obj && obj.__esModule ? obj : { default: obj }; }

var access_token = "55dc1276759f6ff631870b2c509b632382276575";

var member_info = [{ 'name': 'Nick Kantor', 'github_id': ['njk464'], 'image': 'nick_kantor.png', 'p1_lead': true, 'p2_lead': false, 'p3_lead': false, 'tests': 0, 'responsibilities': "Front-End Developer", 'bio': "I'm a Senior Computer Science student and tend to spend my free time playing my trumpet for the longhorn band. After I graduate I plan on pursuing a Master's degree in Information Security." }, { 'name': 'Samuel Braley', 'github_id': ['samuelbraley', 'spacecowboys373@gmail.com'], 'image': 'samuel_braley.jpg', 'p1_lead': false, 'p2_lead': false, 'p3_lead': false, 'tests': 0, 'responsibilities': "Documentation and Apiary", 'bio': "I am a Computer Science senior with certificates in Business Foundations and Game Design. I enjoy being one of the many Sams in the world and plan on being a programmer manager after I graduate." }, { 'name': 'Taben Malik', 'github_id': ['tabenmalik'], 'image': 'taben.jpg', 'p1_lead': false, 'p2_lead': false, 'p3_lead': false, 'tests': 0, 'responsibilities': "Data Collection and Modeling", 'bio': "A double major in Computer Science and Aerospace Engineering. I am a strong advocate of a Mars mission and hope to be a part of one someday." }, { 'name': 'Gustavo Osorio', 'github_id': ['lpztavo'], 'image': 'gustavo.jpg', 'p1_lead': false, 'p2_lead': false, 'p3_lead': false, 'tests': 12, 'responsibilities': "UML Design and Modeling", 'bio': "I'm a senior Computer Science student. I enjoy dancing and coding, but I'm not skilled enough to do both simultaneously." }, { 'name': 'Scott Farrior', 'github_id': ['farrior@cs.utexas.edu', 'sfarrior'], 'image': 'sfarrior.jpg', 'p1_lead': false, 'p2_lead': true, 'p3_lead': false, 'tests': 0, 'responsibilities': "Server setup/administration and SQLAlchemy backend", 'bio': "I'm a Computer Science major. I work as a TA/Grader as well as Computer Lab technician for the community college, and would like to be an instructor one day." }, { 'name': 'David Ares', 'github_id': ['dares23', 'dares23@cs.utexas.edu'], 'image': 'david.jpg', 'p1_lead': false, 'p2_lead': false, 'p3_lead': true, 'tests': 0, 'responsibilities': "Front-End Developer", 'bio': "I am a non-traditional student with one year of Full-stack web development. Before returning to school, I gained seven years of experience in sales, marketing, and management." }];

ReactDOM.render(React.createElement(_github_commits2.default, { url: 'https://api.github.com/repos/samuelbraley/idb/stats/commit_activity', token: access_token }), document.getElementById('overall-commits'));

ReactDOM.render(React.createElement(_github_issues2.default, { url: 'https://api.github.com/repos/samuelbraley/idb/issues', token: access_token }), document.getElementById('overall-issues'));

ReactDOM.render(React.createElement(_github_member_info2.default, { member_info: member_info, url: 'https://api.github.com/repos/samuelbraley/idb', token: access_token }), document.getElementById('member-info'));

ReactDOM.render(React.createElement(_reactTest2.default, null), document.getElementById('react-tests'));

},{"../components/github_commits.jsx":1,"../components/github_issues.jsx":2,"../components/github_member_info.jsx":4,"../components/react-test.jsx":5}],7:[function(require,module,exports){
// the whatwg-fetch polyfill installs the fetch() function
// on the global object (window or self)
//
// Return that as the export for use in Webpack, Browserify etc.
require('whatwg-fetch');
module.exports = self.fetch.bind(self);

},{"whatwg-fetch":8}],8:[function(require,module,exports){
(function(self) {
  'use strict';

  if (self.fetch) {
    return
  }

  var support = {
    searchParams: 'URLSearchParams' in self,
    iterable: 'Symbol' in self && 'iterator' in Symbol,
    blob: 'FileReader' in self && 'Blob' in self && (function() {
      try {
        new Blob()
        return true
      } catch(e) {
        return false
      }
    })(),
    formData: 'FormData' in self,
    arrayBuffer: 'ArrayBuffer' in self
  }

  if (support.arrayBuffer) {
    var viewClasses = [
      '[object Int8Array]',
      '[object Uint8Array]',
      '[object Uint8ClampedArray]',
      '[object Int16Array]',
      '[object Uint16Array]',
      '[object Int32Array]',
      '[object Uint32Array]',
      '[object Float32Array]',
      '[object Float64Array]'
    ]

    var isDataView = function(obj) {
      return obj && DataView.prototype.isPrototypeOf(obj)
    }

    var isArrayBufferView = ArrayBuffer.isView || function(obj) {
      return obj && viewClasses.indexOf(Object.prototype.toString.call(obj)) > -1
    }
  }

  function normalizeName(name) {
    if (typeof name !== 'string') {
      name = String(name)
    }
    if (/[^a-z0-9\-#$%&'*+.\^_`|~]/i.test(name)) {
      throw new TypeError('Invalid character in header field name')
    }
    return name.toLowerCase()
  }

  function normalizeValue(value) {
    if (typeof value !== 'string') {
      value = String(value)
    }
    return value
  }

  // Build a destructive iterator for the value list
  function iteratorFor(items) {
    var iterator = {
      next: function() {
        var value = items.shift()
        return {done: value === undefined, value: value}
      }
    }

    if (support.iterable) {
      iterator[Symbol.iterator] = function() {
        return iterator
      }
    }

    return iterator
  }

  function Headers(headers) {
    this.map = {}

    if (headers instanceof Headers) {
      headers.forEach(function(value, name) {
        this.append(name, value)
      }, this)
    } else if (Array.isArray(headers)) {
      headers.forEach(function(header) {
        this.append(header[0], header[1])
      }, this)
    } else if (headers) {
      Object.getOwnPropertyNames(headers).forEach(function(name) {
        this.append(name, headers[name])
      }, this)
    }
  }

  Headers.prototype.append = function(name, value) {
    name = normalizeName(name)
    value = normalizeValue(value)
    var oldValue = this.map[name]
    this.map[name] = oldValue ? oldValue+','+value : value
  }

  Headers.prototype['delete'] = function(name) {
    delete this.map[normalizeName(name)]
  }

  Headers.prototype.get = function(name) {
    name = normalizeName(name)
    return this.has(name) ? this.map[name] : null
  }

  Headers.prototype.has = function(name) {
    return this.map.hasOwnProperty(normalizeName(name))
  }

  Headers.prototype.set = function(name, value) {
    this.map[normalizeName(name)] = normalizeValue(value)
  }

  Headers.prototype.forEach = function(callback, thisArg) {
    for (var name in this.map) {
      if (this.map.hasOwnProperty(name)) {
        callback.call(thisArg, this.map[name], name, this)
      }
    }
  }

  Headers.prototype.keys = function() {
    var items = []
    this.forEach(function(value, name) { items.push(name) })
    return iteratorFor(items)
  }

  Headers.prototype.values = function() {
    var items = []
    this.forEach(function(value) { items.push(value) })
    return iteratorFor(items)
  }

  Headers.prototype.entries = function() {
    var items = []
    this.forEach(function(value, name) { items.push([name, value]) })
    return iteratorFor(items)
  }

  if (support.iterable) {
    Headers.prototype[Symbol.iterator] = Headers.prototype.entries
  }

  function consumed(body) {
    if (body.bodyUsed) {
      return Promise.reject(new TypeError('Already read'))
    }
    body.bodyUsed = true
  }

  function fileReaderReady(reader) {
    return new Promise(function(resolve, reject) {
      reader.onload = function() {
        resolve(reader.result)
      }
      reader.onerror = function() {
        reject(reader.error)
      }
    })
  }

  function readBlobAsArrayBuffer(blob) {
    var reader = new FileReader()
    var promise = fileReaderReady(reader)
    reader.readAsArrayBuffer(blob)
    return promise
  }

  function readBlobAsText(blob) {
    var reader = new FileReader()
    var promise = fileReaderReady(reader)
    reader.readAsText(blob)
    return promise
  }

  function readArrayBufferAsText(buf) {
    var view = new Uint8Array(buf)
    var chars = new Array(view.length)

    for (var i = 0; i < view.length; i++) {
      chars[i] = String.fromCharCode(view[i])
    }
    return chars.join('')
  }

  function bufferClone(buf) {
    if (buf.slice) {
      return buf.slice(0)
    } else {
      var view = new Uint8Array(buf.byteLength)
      view.set(new Uint8Array(buf))
      return view.buffer
    }
  }

  function Body() {
    this.bodyUsed = false

    this._initBody = function(body) {
      this._bodyInit = body
      if (!body) {
        this._bodyText = ''
      } else if (typeof body === 'string') {
        this._bodyText = body
      } else if (support.blob && Blob.prototype.isPrototypeOf(body)) {
        this._bodyBlob = body
      } else if (support.formData && FormData.prototype.isPrototypeOf(body)) {
        this._bodyFormData = body
      } else if (support.searchParams && URLSearchParams.prototype.isPrototypeOf(body)) {
        this._bodyText = body.toString()
      } else if (support.arrayBuffer && support.blob && isDataView(body)) {
        this._bodyArrayBuffer = bufferClone(body.buffer)
        // IE 10-11 can't handle a DataView body.
        this._bodyInit = new Blob([this._bodyArrayBuffer])
      } else if (support.arrayBuffer && (ArrayBuffer.prototype.isPrototypeOf(body) || isArrayBufferView(body))) {
        this._bodyArrayBuffer = bufferClone(body)
      } else {
        throw new Error('unsupported BodyInit type')
      }

      if (!this.headers.get('content-type')) {
        if (typeof body === 'string') {
          this.headers.set('content-type', 'text/plain;charset=UTF-8')
        } else if (this._bodyBlob && this._bodyBlob.type) {
          this.headers.set('content-type', this._bodyBlob.type)
        } else if (support.searchParams && URLSearchParams.prototype.isPrototypeOf(body)) {
          this.headers.set('content-type', 'application/x-www-form-urlencoded;charset=UTF-8')
        }
      }
    }

    if (support.blob) {
      this.blob = function() {
        var rejected = consumed(this)
        if (rejected) {
          return rejected
        }

        if (this._bodyBlob) {
          return Promise.resolve(this._bodyBlob)
        } else if (this._bodyArrayBuffer) {
          return Promise.resolve(new Blob([this._bodyArrayBuffer]))
        } else if (this._bodyFormData) {
          throw new Error('could not read FormData body as blob')
        } else {
          return Promise.resolve(new Blob([this._bodyText]))
        }
      }

      this.arrayBuffer = function() {
        if (this._bodyArrayBuffer) {
          return consumed(this) || Promise.resolve(this._bodyArrayBuffer)
        } else {
          return this.blob().then(readBlobAsArrayBuffer)
        }
      }
    }

    this.text = function() {
      var rejected = consumed(this)
      if (rejected) {
        return rejected
      }

      if (this._bodyBlob) {
        return readBlobAsText(this._bodyBlob)
      } else if (this._bodyArrayBuffer) {
        return Promise.resolve(readArrayBufferAsText(this._bodyArrayBuffer))
      } else if (this._bodyFormData) {
        throw new Error('could not read FormData body as text')
      } else {
        return Promise.resolve(this._bodyText)
      }
    }

    if (support.formData) {
      this.formData = function() {
        return this.text().then(decode)
      }
    }

    this.json = function() {
      return this.text().then(JSON.parse)
    }

    return this
  }

  // HTTP methods whose capitalization should be normalized
  var methods = ['DELETE', 'GET', 'HEAD', 'OPTIONS', 'POST', 'PUT']

  function normalizeMethod(method) {
    var upcased = method.toUpperCase()
    return (methods.indexOf(upcased) > -1) ? upcased : method
  }

  function Request(input, options) {
    options = options || {}
    var body = options.body

    if (input instanceof Request) {
      if (input.bodyUsed) {
        throw new TypeError('Already read')
      }
      this.url = input.url
      this.credentials = input.credentials
      if (!options.headers) {
        this.headers = new Headers(input.headers)
      }
      this.method = input.method
      this.mode = input.mode
      if (!body && input._bodyInit != null) {
        body = input._bodyInit
        input.bodyUsed = true
      }
    } else {
      this.url = String(input)
    }

    this.credentials = options.credentials || this.credentials || 'omit'
    if (options.headers || !this.headers) {
      this.headers = new Headers(options.headers)
    }
    this.method = normalizeMethod(options.method || this.method || 'GET')
    this.mode = options.mode || this.mode || null
    this.referrer = null

    if ((this.method === 'GET' || this.method === 'HEAD') && body) {
      throw new TypeError('Body not allowed for GET or HEAD requests')
    }
    this._initBody(body)
  }

  Request.prototype.clone = function() {
    return new Request(this, { body: this._bodyInit })
  }

  function decode(body) {
    var form = new FormData()
    body.trim().split('&').forEach(function(bytes) {
      if (bytes) {
        var split = bytes.split('=')
        var name = split.shift().replace(/\+/g, ' ')
        var value = split.join('=').replace(/\+/g, ' ')
        form.append(decodeURIComponent(name), decodeURIComponent(value))
      }
    })
    return form
  }

  function parseHeaders(rawHeaders) {
    var headers = new Headers()
    rawHeaders.split(/\r?\n/).forEach(function(line) {
      var parts = line.split(':')
      var key = parts.shift().trim()
      if (key) {
        var value = parts.join(':').trim()
        headers.append(key, value)
      }
    })
    return headers
  }

  Body.call(Request.prototype)

  function Response(bodyInit, options) {
    if (!options) {
      options = {}
    }

    this.type = 'default'
    this.status = 'status' in options ? options.status : 200
    this.ok = this.status >= 200 && this.status < 300
    this.statusText = 'statusText' in options ? options.statusText : 'OK'
    this.headers = new Headers(options.headers)
    this.url = options.url || ''
    this._initBody(bodyInit)
  }

  Body.call(Response.prototype)

  Response.prototype.clone = function() {
    return new Response(this._bodyInit, {
      status: this.status,
      statusText: this.statusText,
      headers: new Headers(this.headers),
      url: this.url
    })
  }

  Response.error = function() {
    var response = new Response(null, {status: 0, statusText: ''})
    response.type = 'error'
    return response
  }

  var redirectStatuses = [301, 302, 303, 307, 308]

  Response.redirect = function(url, status) {
    if (redirectStatuses.indexOf(status) === -1) {
      throw new RangeError('Invalid status code')
    }

    return new Response(null, {status: status, headers: {location: url}})
  }

  self.Headers = Headers
  self.Request = Request
  self.Response = Response

  self.fetch = function(input, init) {
    return new Promise(function(resolve, reject) {
      var request = new Request(input, init)
      var xhr = new XMLHttpRequest()

      xhr.onload = function() {
        var options = {
          status: xhr.status,
          statusText: xhr.statusText,
          headers: parseHeaders(xhr.getAllResponseHeaders() || '')
        }
        options.url = 'responseURL' in xhr ? xhr.responseURL : options.headers.get('X-Request-URL')
        var body = 'response' in xhr ? xhr.response : xhr.responseText
        resolve(new Response(body, options))
      }

      xhr.onerror = function() {
        reject(new TypeError('Network request failed'))
      }

      xhr.ontimeout = function() {
        reject(new TypeError('Network request failed'))
      }

      xhr.open(request.method, request.url, true)

      if (request.credentials === 'include') {
        xhr.withCredentials = true
      }

      if ('responseType' in xhr && support.blob) {
        xhr.responseType = 'blob'
      }

      request.headers.forEach(function(value, name) {
        xhr.setRequestHeader(name, value)
      })

      xhr.send(typeof request._bodyInit === 'undefined' ? null : request._bodyInit)
    })
  }
  self.fetch.polyfill = true
})(typeof self !== 'undefined' ? self : this);

},{}]},{},[6]);
