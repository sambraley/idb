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

var planets = [{
	"dec": 44.915352,
	"star_pid": 230,
	"diameter": 176735.008,
	"mass": 3.477136e+27,
	"orbital_period": 1.327347,
	"temperature": 1823,
	"ra": 188.266255,
	"galaxy_pid": 143,
	"name": "HAT-P-36 b",
	"gravity": 0.029718570060615346,
	"pid": 1
}, {
	"dec": 51.269138,
	"star_pid": 28,
	"diameter": 164710.316,
	"mass": 2.218762e+27,
	"orbital_period": 2.797436,
	"temperature": 1271,
	"ra": 284.296064,
	"galaxy_pid": 143,
	"name": "HAT-P-37 b",
	"gravity": 0.02183335709325446,
	"pid": 2
}, {
	"dec": 32.246151,
	"star_pid": 140,
	"diameter": 115353.15,
	"mass": 5.06766e+26,
	"orbital_period": 4.640382,
	"temperature": 1082,
	"ra": 35.383234,
	"galaxy_pid": 143,
	"name": "HAT-P-38 b",
	"gravity": 0.010167166878461332,
	"pid": 3
}, {
	"dec": 17.830082,
	"star_pid": 248,
	"diameter": 219660.362,
	"mass": 1.136902e+27,
	"orbital_period": 3.54387,
	"temperature": 1752,
	"ra": 113.758247,
	"galaxy_pid": 143,
	"name": "HAT-P-39 b",
	"gravity": 0.006290295385687977,
	"pid": 4
}, {
	"dec": 45.457378,
	"star_pid": 62,
	"diameter": 241892.06,
	"mass": 1.1672699999999999e+27,
	"orbital_period": 4.457243,
	"temperature": 1770,
	"ra": 335.512861,
	"galaxy_pid": 143,
	"name": "HAT-P-40 b",
	"gravity": 0.005325734316961424,
	"pid": 5
}, {
	"dec": 4.672421,
	"star_pid": 119,
	"diameter": 235600.07,
	"mass": 1.5184e+27,
	"orbital_period": 2.694047,
	"temperature": 1941,
	"ra": 297.322651,
	"galaxy_pid": 143,
	"name": "HAT-P-41 b",
	"gravity": 0.00730275556261142,
	"pid": 6
}, {
	"dec": 6.09723,
	"star_pid": 96,
	"diameter": 178972.16,
	"mass": 1.981512e+27,
	"orbital_period": 4.641878,
	"temperature": 1428,
	"ra": 135.344391,
	"galaxy_pid": 143,
	"name": "HAT-P-42 b",
	"gravity": 0.01651494558211872,
	"pid": 7
}];

var App = function (_React$Component) {
	_inherits(App, _React$Component);

	function App(props) {
		_classCallCheck(this, App);

		var _this = _possibleConstructorReturn(this, (App.__proto__ || Object.getPrototypeOf(App)).call(this, props));

		var planet_id = window.location.href.split("/")[4];
		console.log("got planet_id: " + planet_id);

		_this.state = {
			model: planets[parseInt(planet_id) - 1]
		};

		// this.setState({ 
		// 	models: planets,
		// 	title: "Planets"
		// });

		// console.log(this.state.models);
		// console.log(this.state.title);
		return _this;
	}

	// YTSearch({key: API_KEY, term: term}, (videos) => {
	// 	this.setState({ 
	// 		videos: videos,
	// 		selectedVideo: videos[0]
	// 	});
	// when key and vaule are the same name, setState({ videos });

	_createClass(App, [{
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
