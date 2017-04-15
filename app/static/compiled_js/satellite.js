(function e(t,n,r){function s(o,u){if(!n[o]){if(!t[o]){var a=typeof require=="function"&&require;if(!u&&a)return a(o,!0);if(i)return i(o,!0);var f=new Error("Cannot find module '"+o+"'");throw f.code="MODULE_NOT_FOUND",f}var l=n[o]={exports:{}};t[o][0].call(l.exports,function(e){var n=t[o][1][e];return s(n?n:e)},l,l.exports,e,t,n,r)}return n[o].exports}var i=typeof require=="function"&&require;for(var o=0;o<r.length;o++)s(r[o]);return s})({1:[function(require,module,exports){
"use strict";

Object.defineProperty(exports, "__esModule", {
	value: true
});

var _createClass = function () { function defineProperties(target, props) { for (var i = 0; i < props.length; i++) { var descriptor = props[i]; descriptor.enumerable = descriptor.enumerable || false; descriptor.configurable = true; if ("value" in descriptor) descriptor.writable = true; Object.defineProperty(target, descriptor.key, descriptor); } } return function (Constructor, protoProps, staticProps) { if (protoProps) defineProperties(Constructor.prototype, protoProps); if (staticProps) defineProperties(Constructor, staticProps); return Constructor; }; }();

function _classCallCheck(instance, Constructor) { if (!(instance instanceof Constructor)) { throw new TypeError("Cannot call a class as a function"); } }

function _possibleConstructorReturn(self, call) { if (!self) { throw new ReferenceError("this hasn't been initialised - super() hasn't been called"); } return call && (typeof call === "object" || typeof call === "function") ? call : self; }

function _inherits(subClass, superClass) { if (typeof superClass !== "function" && superClass !== null) { throw new TypeError("Super expression must either be null or a function, not " + typeof superClass); } subClass.prototype = Object.create(superClass && superClass.prototype, { constructor: { value: subClass, enumerable: false, writable: true, configurable: true } }); if (superClass) Object.setPrototypeOf ? Object.setPrototypeOf(subClass, superClass) : subClass.__proto__ = superClass; }

var Satellite_Img = function (_React$Component) {
	_inherits(Satellite_Img, _React$Component);

	function Satellite_Img(props) {
		_classCallCheck(this, Satellite_Img);

		var _this = _possibleConstructorReturn(this, (Satellite_Img.__proto__ || Object.getPrototypeOf(Satellite_Img)).call(this, props));

		_this.state = {
			image_url: "undefined"
		};
		var base_url = "/" + window.location.href.split('/')[3] + "/" + window.location.href.split('/')[4];
		var image_url = "/api/v1" + base_url + "/image";
		console.log(image_url);
		fetch(image_url).then(function (response) {
			return response.json();
		}).then(function (responseJson) {
			_this.setState({
				image_url: responseJson.img_url
			});
		}).catch(function (error) {
			console.error(error);
		});
		return _this;
	}

	_createClass(Satellite_Img, [{
		key: "render",
		value: function render() {
			return React.createElement("img", { className: "img-thumbnail", style: { width: '400px', height: '400px' }, src: this.state.image_url });
		}
	}]);

	return Satellite_Img;
}(React.Component);

exports.default = Satellite_Img;

},{}],2:[function(require,module,exports){
'use strict';

var _satelliteImg = require('../components/satellite-img.jsx');

var _satelliteImg2 = _interopRequireDefault(_satelliteImg);

function _interopRequireDefault(obj) { return obj && obj.__esModule ? obj : { default: obj }; }

ReactDOM.render(React.createElement(_satelliteImg2.default, null), document.getElementById('react-satellite'));

},{"../components/satellite-img.jsx":1}]},{},[2]);
