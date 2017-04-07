(function e(t,n,r){function s(o,u){if(!n[o]){if(!t[o]){var a=typeof require=="function"&&require;if(!u&&a)return a(o,!0);if(i)return i(o,!0);var f=new Error("Cannot find module '"+o+"'");throw f.code="MODULE_NOT_FOUND",f}var l=n[o]={exports:{}};t[o][0].call(l.exports,function(e){var n=t[o][1][e];return s(n?n:e)},l,l.exports,e,t,n,r)}return n[o].exports}var i=typeof require=="function"&&require;for(var o=0;o<r.length;o++)s(r[o]);return s})({1:[function(require,module,exports){
"use strict";

Object.defineProperty(exports, "__esModule", {
	value: true
});

var ModelInfo = function ModelInfo(_ref) {
	var model = _ref.model;

	console.log("in model info, got model id: " + model.pid);
	console.log(model);
	var link = "/static/images/HAT-P-33%20b.png";
	//var aladin = A.aladin('#aladin-lite-div', {survey: "P/DSS2/color", fov:60});
	//var aladinEmbed = aladin.getEmbedCode();
	return React.createElement(
		"div",
		null,
		React.createElement(
			"div",
			{ className: "row" },
			React.createElement(
				"div",
				{ className: "col-lg-12 text-center" },
				React.createElement(
					"h1",
					null,
					model.name
				)
			)
		),
		React.createElement(
			"div",
			{ className: "row" },
			React.createElement(
				"div",
				{ className: "col-md-6 text-center", styles: "padding-top:40px;" },
				React.createElement("img", { src: "/static/images/HAT-P-33%20b.png" })
			),
			React.createElement(
				"div",
				{ className: "col-md-6 text-center" },
				React.createElement(
					"div",
					{ className: "col-md-12" },
					React.createElement(
						"h3",
						null,
						"Diameter:"
					),
					React.createElement(
						"p",
						null,
						model.diameter
					),
					React.createElement(
						"h3",
						null,
						"Surface Temperatures:"
					),
					React.createElement(
						"p",
						null,
						model.surface_temperature
					),
					React.createElement(
						"h3",
						null,
						"Right Ascension:"
					),
					React.createElement(
						"p",
						null,
						model.ra
					),
					React.createElement(
						"h3",
						null,
						"Declination:"
					),
					React.createElement(
						"p",
						null,
						model.dec
					),
					React.createElement(
						"h3",
						null,
						"Mass:"
					),
					React.createElement(
						"p",
						null,
						model.mass
					),
					React.createElement(
						"h3",
						null,
						"Temperature:"
					),
					React.createElement(
						"p",
						null,
						model.temperature
					),
					React.createElement(
						"h3",
						null,
						"Gravity:"
					),
					React.createElement(
						"p",
						null,
						model.gravity
					),
					React.createElement(
						"h3",
						null,
						"Orbital Period:"
					),
					React.createElement(
						"p",
						null,
						model.orbital_period
					),
					React.createElement(
						"h3",
						null,
						"Orbiting Bodies:"
					),
					React.createElement(
						"p",
						null,
						model.orbiting_bodies
					)
				)
			)
		)
	);
};

exports.default = ModelInfo;

},{}],2:[function(require,module,exports){
"use strict";

Object.defineProperty(exports, "__esModule", {
	value: true
});

var _createClass = function () { function defineProperties(target, props) { for (var i = 0; i < props.length; i++) { var descriptor = props[i]; descriptor.enumerable = descriptor.enumerable || false; descriptor.configurable = true; if ("value" in descriptor) descriptor.writable = true; Object.defineProperty(target, descriptor.key, descriptor); } } return function (Constructor, protoProps, staticProps) { if (protoProps) defineProperties(Constructor.prototype, protoProps); if (staticProps) defineProperties(Constructor, staticProps); return Constructor; }; }();

function _classCallCheck(instance, Constructor) { if (!(instance instanceof Constructor)) { throw new TypeError("Cannot call a class as a function"); } }

function _possibleConstructorReturn(self, call) { if (!self) { throw new ReferenceError("this hasn't been initialised - super() hasn't been called"); } return call && (typeof call === "object" || typeof call === "function") ? call : self; }

function _inherits(subClass, superClass) { if (typeof superClass !== "function" && superClass !== null) { throw new TypeError("Super expression must either be null or a function, not " + typeof superClass); } subClass.prototype = Object.create(superClass && superClass.prototype, { constructor: { value: subClass, enumerable: false, writable: true, configurable: true } }); if (superClass) Object.setPrototypeOf ? Object.setPrototypeOf(subClass, superClass) : subClass.__proto__ = superClass; }

var NavBar = function (_React$Component) {
	_inherits(NavBar, _React$Component);

	function NavBar() {
		_classCallCheck(this, NavBar);

		return _possibleConstructorReturn(this, (NavBar.__proto__ || Object.getPrototypeOf(NavBar)).apply(this, arguments));
	}

	_createClass(NavBar, [{
		key: "render",
		value: function render() {
			return React.createElement(
				"nav",
				{ className: "navbar navbar-default navbar-fixed-top", role: "navigation" },
				React.createElement(
					"div",
					{ className: "container" },
					React.createElement(
						"div",
						{ className: "navbar-header" },
						React.createElement(
							"a",
							{ className: "navbar-brand active", href: "/" },
							"SpaceCowboys"
						)
					),
					React.createElement(
						"div",
						{ className: "collapse navbar-collapse" },
						React.createElement(
							"ul",
							{ className: "nav navbar-nav" },
							React.createElement(
								"li",
								null,
								React.createElement(
									"a",
									{ className: "navbar-item", href: "/planets" },
									"Planets"
								)
							),
							React.createElement(
								"li",
								null,
								React.createElement(
									"a",
									{ className: "navbar-item", href: "/galaxies" },
									"Galaxies"
								)
							),
							React.createElement(
								"li",
								null,
								React.createElement(
									"a",
									{ className: "navbar-item", href: "/satellites" },
									"Satellites"
								)
							),
							React.createElement(
								"li",
								null,
								React.createElement(
									"a",
									{ className: "navbar-item", href: "/stars" },
									"Stars"
								)
							),
							React.createElement(
								"li",
								null,
								React.createElement(
									"a",
									{ className: "navbar-item", href: "/about" },
									"About"
								)
							),
							React.createElement(
								"li",
								null,
								React.createElement(
									"a",
									{ className: "navbar-item", href: "/report" },
									"Report"
								)
							)
						)
					)
				)
			);
		}
	}]);

	return NavBar;
}(React.Component);

exports.default = NavBar;

},{}],3:[function(require,module,exports){
'use strict';

var _createClass = function () { function defineProperties(target, props) { for (var i = 0; i < props.length; i++) { var descriptor = props[i]; descriptor.enumerable = descriptor.enumerable || false; descriptor.configurable = true; if ("value" in descriptor) descriptor.writable = true; Object.defineProperty(target, descriptor.key, descriptor); } } return function (Constructor, protoProps, staticProps) { if (protoProps) defineProperties(Constructor.prototype, protoProps); if (staticProps) defineProperties(Constructor, staticProps); return Constructor; }; }();

var _nav_bar = require('./../components/nav_bar');

var _nav_bar2 = _interopRequireDefault(_nav_bar);

var _model_info = require('./../components/model_info');

var _model_info2 = _interopRequireDefault(_model_info);

function _interopRequireDefault(obj) { return obj && obj.__esModule ? obj : { default: obj }; }

function _classCallCheck(instance, Constructor) { if (!(instance instanceof Constructor)) { throw new TypeError("Cannot call a class as a function"); } }

function _possibleConstructorReturn(self, call) { if (!self) { throw new ReferenceError("this hasn't been initialised - super() hasn't been called"); } return call && (typeof call === "object" || typeof call === "function") ? call : self; }

function _inherits(subClass, superClass) { if (typeof superClass !== "function" && superClass !== null) { throw new TypeError("Super expression must either be null or a function, not " + typeof superClass); } subClass.prototype = Object.create(superClass && superClass.prototype, { constructor: { value: subClass, enumerable: false, writable: true, configurable: true } }); if (superClass) Object.setPrototypeOf ? Object.setPrototypeOf(subClass, superClass) : subClass.__proto__ = superClass; }

/* window.location.href */
console.log(window.location.href);
console.log(window.location.hostname);
var modelType = window.location.href.split('/')[3];
var planet_id = window.location.href.split("/")[4];
console.log("got planet_id: " + planet_id);
var baseUrl = window.location.href.split('/')[2];
var apiExt = "/api/v1/" + modelType + "/" + planet_id;
var url = "http://" + baseUrl + apiExt;

var App = function (_React$Component) {
	_inherits(App, _React$Component);

	function App(props) {
		_classCallCheck(this, App);

		var _this = _possibleConstructorReturn(this, (App.__proto__ || Object.getPrototypeOf(App)).call(this, props));

		_this.state = {
			id: planet_id,
			model: null
		};

		return _this;
	}

	_createClass(App, [{
		key: 'getModel',
		value: function getModel(id) {
			var _this2 = this;

			fetch(url).then(function (response) {
				return response.json();
			}).then(function (responseJson) {
				_this2.setState({});
			}).catch(function (error) {
				console.error(error);
			});
		}
	}, {
		key: 'render',
		value: function render() {
			return React.createElement(
				'div',
				null,
				React.createElement(
					'div',
					null,
					React.createElement(_nav_bar2.default, null)
				),
				React.createElement(
					'div',
					{ className: 'container model-container' },
					React.createElement(_model_info2.default, { model: this.state.model })
				)
			);
		}
	}]);

	return App;
}(React.Component);

ReactDOM.render(React.createElement(App, null), document.querySelector('.container'));

},{"./../components/model_info":1,"./../components/nav_bar":2}]},{},[3]);
