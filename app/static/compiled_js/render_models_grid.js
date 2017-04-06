(function e(t,n,r){function s(o,u){if(!n[o]){if(!t[o]){var a=typeof require=="function"&&require;if(!u&&a)return a(o,!0);if(i)return i(o,!0);var f=new Error("Cannot find module '"+o+"'");throw f.code="MODULE_NOT_FOUND",f}var l=n[o]={exports:{}};t[o][0].call(l.exports,function(e){var n=t[o][1][e];return s(n?n:e)},l,l.exports,e,t,n,r)}return n[o].exports}var i=typeof require=="function"&&require;for(var o=0;o<r.length;o++)s(r[o]);return s})({1:[function(require,module,exports){
"use strict";

Object.defineProperty(exports, "__esModule", {
	value: true
});

var _createClass = function () { function defineProperties(target, props) { for (var i = 0; i < props.length; i++) { var descriptor = props[i]; descriptor.enumerable = descriptor.enumerable || false; descriptor.configurable = true; if ("value" in descriptor) descriptor.writable = true; Object.defineProperty(target, descriptor.key, descriptor); } } return function (Constructor, protoProps, staticProps) { if (protoProps) defineProperties(Constructor.prototype, protoProps); if (staticProps) defineProperties(Constructor, staticProps); return Constructor; }; }();

function _classCallCheck(instance, Constructor) { if (!(instance instanceof Constructor)) { throw new TypeError("Cannot call a class as a function"); } }

function _possibleConstructorReturn(self, call) { if (!self) { throw new ReferenceError("this hasn't been initialised - super() hasn't been called"); } return call && (typeof call === "object" || typeof call === "function") ? call : self; }

function _inherits(subClass, superClass) { if (typeof superClass !== "function" && superClass !== null) { throw new TypeError("Super expression must either be null or a function, not " + typeof superClass); } subClass.prototype = Object.create(superClass && superClass.prototype, { constructor: { value: subClass, enumerable: false, writable: true, configurable: true } }); if (superClass) Object.setPrototypeOf ? Object.setPrototypeOf(subClass, superClass) : subClass.__proto__ = superClass; }

var DropDown = function (_React$Component) {
	_inherits(DropDown, _React$Component);

	function DropDown() {
		_classCallCheck(this, DropDown);

		return _possibleConstructorReturn(this, (DropDown.__proto__ || Object.getPrototypeOf(DropDown)).apply(this, arguments));
	}

	_createClass(DropDown, [{
		key: "render",
		value: function render() {
			return React.createElement(
				"div",
				{ className: "sort-container col-sm-2", id: "sort-toolbar-container" },
				React.createElement(
					"select",
					{ className: "form-control", id: "sort-dropdown", "data-ui": "sort-container" },
					React.createElement(
						"option",
						{ value: "title", "data-ui": "sort-item" },
						"Sort By"
					),
					React.createElement(
						"option",
						{ value: "title", "data-ui": "sort-item" },
						"A - Z"
					),
					React.createElement(
						"option",
						{ value: "title_r", "data-ui": "sort-item" },
						"Z - A"
					)
				)
			);
		}
	}]);

	return DropDown;
}(React.Component);

;

exports.default = DropDown;

},{}],2:[function(require,module,exports){
"use strict";

Object.defineProperty(exports, "__esModule", {
	value: true
});

var ModelListItem = function ModelListItem(_ref) {
	var model = _ref.model;

	var link = "/" + window.location.href.split('/')[3] + "/" + model.pid;
	return React.createElement(
		"div",
		{ className: "col-md-4 text-center model-list-item" },
		React.createElement(
			"a",
			{ href: link },
			React.createElement("img", { className: "img-thumbnail about-image", src: "/static/images/HAT-P-33.png" }),
			React.createElement(
				"h3",
				null,
				model.name
			)
		)
	);
};

exports.default = ModelListItem;

},{}],3:[function(require,module,exports){
"use strict";

Object.defineProperty(exports, "__esModule", {
	value: true
});

var ModelTitle = function ModelTitle(_ref) {
	var title = _ref.title;

	return React.createElement(
		"div",
		{ className: "row" },
		React.createElement(
			"div",
			{ className: "col-lg-12" },
			React.createElement(
				"h1",
				null,
				title
			)
		)
	);
};

exports.default = ModelTitle;

},{}],4:[function(require,module,exports){
"use strict";

Object.defineProperty(exports, "__esModule", {
	value: true
});

var _model_list_item = require("./model_list_item");

var _model_list_item2 = _interopRequireDefault(_model_list_item);

function _interopRequireDefault(obj) { return obj && obj.__esModule ? obj : { default: obj }; }

var ModelList = function ModelList(props) {
	if (!props) {
		console.log("nothing in props");
		return React.createElement(
			"div",
			null,
			"Loading..."
		);
	}

	var modelItem = props.models.map(function (model) {
		return React.createElement(_model_list_item2.default, {
			key: model.pid,
			model: model });
	});
	return React.createElement(
		"div",
		{ className: "row" },
		modelItem
	);
};

exports.default = ModelList;

},{"./model_list_item":2}],5:[function(require,module,exports){
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

},{}],6:[function(require,module,exports){
"use strict";

Object.defineProperty(exports, "__esModule", {
	value: true
});

var PageItem = function PageItem(_ref) {
	var page_number = _ref.page_number,
	    onPageSelect = _ref.onPageSelect,
	    isActive = _ref.isActive;

	if (isActive === true) {
		return React.createElement(
			"li",
			{ className: "active" },
			React.createElement(
				"a",
				null,
				page_number
			)
		);
	} else {
		return React.createElement(
			"li",
			{ onClick: function onClick() {
					return onPageSelect(page_number);
				}, className: "page-item" },
			React.createElement(
				"a",
				null,
				page_number
			)
		);
	}
};
exports.default = PageItem;

},{}],7:[function(require,module,exports){
"use strict";

Object.defineProperty(exports, "__esModule", {
	value: true
});

var _page_item = require("./page_item");

var _page_item2 = _interopRequireDefault(_page_item);

function _interopRequireDefault(obj) { return obj && obj.__esModule ? obj : { default: obj }; }

var Pages = function Pages(_ref) {
	var current_page = _ref.current_page,
	    total_pages = _ref.total_pages,
	    onPageSelect = _ref.onPageSelect;

	var pages = [];
	// Adding previous button
	if (current_page != 1) {
		pages.push(React.createElement(
			"li",
			{ onClick: function onClick() {
					return onPageSelect(current_page - 1);
				}, className: "page-item", id: "previous-button" },
			React.createElement(
				"a",
				null,
				"Previous"
			)
		));
	}
	//Setting list of page numbers
	var start;
	var end;
	if (total_pages <= 10) {
		end = total_pages;
		start = 1;
	} else if (10 >= current_page + 5) {
		end = 10;
		start = 1;
	} else if (total_pages > current_page + 5) {
		end = current_page + 5;
		start = end - 9;
	} else {
		end = total_pages;
		start = end - 9;
	}
	// creating pageItems
	for (var i = start; i <= end && i <= total_pages; i++) {
		if (i === current_page) {
			pages.push(React.createElement(_page_item2.default, {
				page_number: i,
				onPageSelect: onPageSelect,
				isActive: true,
				id: i }));
		} else {
			pages.push(React.createElement(_page_item2.default, {
				page_number: i,
				onPageSelect: onPageSelect,
				isActive: false,
				id: i }));
		}
	}
	//adding next button
	if (current_page != total_pages) {
		pages.push(React.createElement(
			"li",
			{ onClick: function onClick() {
					return onPageSelect(current_page + 1);
				}, className: "page-item" },
			React.createElement(
				"a",
				null,
				"Next"
			)
		));
	}

	return React.createElement(
		"div",
		{ className: "container" },
		React.createElement(
			"ul",
			{ className: "pagination" },
			pages
		)
	);
};

exports.default = Pages;

},{"./page_item":6}],8:[function(require,module,exports){
'use strict';

var _createClass = function () { function defineProperties(target, props) { for (var i = 0; i < props.length; i++) { var descriptor = props[i]; descriptor.enumerable = descriptor.enumerable || false; descriptor.configurable = true; if ("value" in descriptor) descriptor.writable = true; Object.defineProperty(target, descriptor.key, descriptor); } } return function (Constructor, protoProps, staticProps) { if (protoProps) defineProperties(Constructor.prototype, protoProps); if (staticProps) defineProperties(Constructor, staticProps); return Constructor; }; }();

var _nav_bar = require('./../components/nav_bar');

var _nav_bar2 = _interopRequireDefault(_nav_bar);

var _models_list = require('./../components/models_list');

var _models_list2 = _interopRequireDefault(_models_list);

var _model_title = require('./../components/model_title');

var _model_title2 = _interopRequireDefault(_model_title);

var _drop_down = require('./../components/drop_down');

var _drop_down2 = _interopRequireDefault(_drop_down);

var _pages = require('./../components/pages.js');

var _pages2 = _interopRequireDefault(_pages);

function _interopRequireDefault(obj) { return obj && obj.__esModule ? obj : { default: obj }; }

function _classCallCheck(instance, Constructor) { if (!(instance instanceof Constructor)) { throw new TypeError("Cannot call a class as a function"); } }

function _possibleConstructorReturn(self, call) { if (!self) { throw new ReferenceError("this hasn't been initialised - super() hasn't been called"); } return call && (typeof call === "object" || typeof call === "function") ? call : self; }

function _inherits(subClass, superClass) { if (typeof superClass !== "function" && superClass !== null) { throw new TypeError("Super expression must either be null or a function, not " + typeof superClass); } subClass.prototype = Object.create(superClass && superClass.prototype, { constructor: { value: subClass, enumerable: false, writable: true, configurable: true } }); if (superClass) Object.setPrototypeOf ? Object.setPrototypeOf(subClass, superClass) : subClass.__proto__ = superClass; }

var exts = { "planets": "Planets", "galaxies": "Galaxies", "satellites": "Satellites", "stars": "Stars" };
var modelType = window.location.href.split('/')[3];
var baseUrl = window.location.href.split('/')[2];
var apiExt = "/api/v1/" + modelType + "?page=1&results_per_page=9";
var url = "http://" + baseUrl + apiExt;

var App = function (_React$Component) {
	_inherits(App, _React$Component);

	function App(props) {
		_classCallCheck(this, App);

		var _this = _possibleConstructorReturn(this, (App.__proto__ || Object.getPrototypeOf(App)).call(this, props));

		_this.state = {
			models: [],
			title: exts[modelType],
			total_pages: 1,
			current_page: 1
		};

		return _this;
	}

	_createClass(App, [{
		key: 'componentDidMount',
		value: function componentDidMount() {
			var _this2 = this;

			if (this.current_page !== undefined) {
				var _apiExt = "/api/v1/" + modelType + "?page=" + this.current_page + "&results_per_page=9";
			} else {
				var _apiExt2 = "/api/v1/" + modelType + "?page=1&results_per_page=9";
			}
			var url = "http://" + baseUrl + apiExt;
			fetch(url).then(function (response) {
				return response.json();
			}).then(function (responseJson) {
				_this2.setState({
					models: responseJson.objects,
					total_pages: responseJson.total_pages,
					current_page: responseJson.page
				});
			}).catch(function (error) {
				console.error(error);
			});
		}
	}, {
		key: 'getModels',
		value: function getModels(current_page) {
			var _this3 = this;

			console.log("in the getModels () ");
			this.setState({ current_page: current_page });
			console.log(current_page);
			var apiExt = "/api/v1/" + modelType + "?page=" + current_page + "&results_per_page=9";
			var url = "http://" + baseUrl + apiExt;
			fetch(url).then(function (response) {
				return response.json();
			}).then(function (responseJson) {
				console.log(responseJson.objects);
				_this3.setState({
					models: responseJson.objects,
					total_pages: responseJson.total_pages,
					current_page: responseJson.page
				});
			}).catch(function (error) {
				console.error(error);
			});
		}
	}, {
		key: 'render',
		value: function render() {
			return React.createElement(
				'div',
				{ id: 'main-div' },
				React.createElement(
					'div',
					{ id: 'nav-bar-div' },
					React.createElement(_nav_bar2.default, null)
				),
				React.createElement(
					'div',
					{ className: 'container model-container' },
					React.createElement(_model_title2.default, { title: this.state.title }),
					React.createElement(
						'div',
						{ className: 'row' },
						React.createElement(_drop_down2.default, null)
					),
					React.createElement(_models_list2.default, {
						models: this.state.models,
						page: this.current_page }),
					React.createElement(_pages2.default, {
						current_page: this.state.current_page,
						total_pages: this.state.total_pages,
						onPageSelect: this.getModels.bind(this) })
				)
			);
		}
	}]);

	return App;
}(React.Component);

ReactDOM.render(React.createElement(App, null), document.querySelector('.container'));

},{"./../components/drop_down":1,"./../components/model_title":3,"./../components/models_list":4,"./../components/nav_bar":5,"./../components/pages.js":7}]},{},[8]);
