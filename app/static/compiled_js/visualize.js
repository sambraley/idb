(function e(t,n,r){function s(o,u){if(!n[o]){if(!t[o]){var a=typeof require=="function"&&require;if(!u&&a)return a(o,!0);if(i)return i(o,!0);var f=new Error("Cannot find module '"+o+"'");throw f.code="MODULE_NOT_FOUND",f}var l=n[o]={exports:{}};t[o][0].call(l.exports,function(e){var n=t[o][1][e];return s(n?n:e)},l,l.exports,e,t,n,r)}return n[o].exports}var i=typeof require=="function"&&require;for(var o=0;o<r.length;o++)s(r[o]);return s})({1:[function(require,module,exports){
"use strict";

Object.defineProperty(exports, "__esModule", {
	value: true
});

var _createClass = function () { function defineProperties(target, props) { for (var i = 0; i < props.length; i++) { var descriptor = props[i]; descriptor.enumerable = descriptor.enumerable || false; descriptor.configurable = true; if ("value" in descriptor) descriptor.writable = true; Object.defineProperty(target, descriptor.key, descriptor); } } return function (Constructor, protoProps, staticProps) { if (protoProps) defineProperties(Constructor.prototype, protoProps); if (staticProps) defineProperties(Constructor, staticProps); return Constructor; }; }();

function _classCallCheck(instance, Constructor) { if (!(instance instanceof Constructor)) { throw new TypeError("Cannot call a class as a function"); } }

function _possibleConstructorReturn(self, call) { if (!self) { throw new ReferenceError("this hasn't been initialised - super() hasn't been called"); } return call && (typeof call === "object" || typeof call === "function") ? call : self; }

function _inherits(subClass, superClass) { if (typeof superClass !== "function" && superClass !== null) { throw new TypeError("Super expression must either be null or a function, not " + typeof superClass); } subClass.prototype = Object.create(superClass && superClass.prototype, { constructor: { value: subClass, enumerable: false, writable: true, configurable: true } }); if (superClass) Object.setPrototypeOf ? Object.setPrototypeOf(subClass, superClass) : subClass.__proto__ = superClass; }

var React_D3 = function (_React$Component) {
	_inherits(React_D3, _React$Component);

	function React_D3(props) {
		_classCallCheck(this, React_D3);

		var _this = _possibleConstructorReturn(this, (React_D3.__proto__ || Object.getPrototypeOf(React_D3)).call(this, props));

		_this.state = {
			visualization: "albums"
		};
		return _this;
	}

	_createClass(React_D3, [{
		key: "changeVisual",
		value: function changeVisual(v_class) {
			this.setState({
				visualization: v_class
			});
		}
	}, {
		key: "render",
		value: function render() {
			var _this2 = this;

			return React.createElement(
				"div",
				null,
				React.createElement(
					"h1",
					{ className: "text-center" },
					"Boswemian Visualizations"
				),
				React.createElement(
					"div",
					{ className: "dropdown" },
					React.createElement(
						"button",
						{ className: "btn btn-primary dropdown-toggle", type: "button", "data-toggle": "dropdown" },
						"Choose a visualization",
						React.createElement("span", { className: "caret" })
					),
					React.createElement(
						"ul",
						{ className: "dropdown-menu" },
						React.createElement(
							"li",
							{ onClick: function onClick() {
									return _this2.changeVisual("albums");
								} },
							React.createElement(
								"a",
								null,
								"Bubble Visualization of Albums"
							)
						),
						React.createElement(
							"li",
							{ onClick: function onClick() {
									return _this2.changeVisual("adjacency");
								} },
							React.createElement(
								"a",
								null,
								"Adjacency Matrix of Artists and Venues"
							)
						),
						React.createElement(
							"li",
							{ onClick: function onClick() {
									return _this2.changeVisual("geographic");
								} },
							React.createElement(
								"a",
								null,
								"Geographic Map for Concerts"
							)
						)
					)
				),
				React.createElement("svg", { className: "center-block " + this.state.visualization, width: "960", height: "960", fontFamily: "sans-serif", fontSize: "10", textAnchor: "middle" })
			);
		}
	}]);

	return React_D3;
}(React.Component);

exports.default = React_D3;

},{}],2:[function(require,module,exports){
'use strict';

var _react_d = require('../components/react_d3.jsx');

var _react_d2 = _interopRequireDefault(_react_d);

function _interopRequireDefault(obj) { return obj && obj.__esModule ? obj : { default: obj }; }

ReactDOM.render(React.createElement(_react_d2.default, null), document.getElementById('react-visualize'));

},{"../components/react_d3.jsx":1}]},{},[2]);
