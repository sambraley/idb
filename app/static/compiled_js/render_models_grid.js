(function e(t,n,r){function s(o,u){if(!n[o]){if(!t[o]){var a=typeof require=="function"&&require;if(!u&&a)return a(o,!0);if(i)return i(o,!0);var f=new Error("Cannot find module '"+o+"'");throw f.code="MODULE_NOT_FOUND",f}var l=n[o]={exports:{}};t[o][0].call(l.exports,function(e){var n=t[o][1][e];return s(n?n:e)},l,l.exports,e,t,n,r)}return n[o].exports}var i=typeof require=="function"&&require;for(var o=0;o<r.length;o++)s(r[o]);return s})({1:[function(require,module,exports){
"use strict";

Object.defineProperty(exports, "__esModule", {
	value: true
});

var _dropdownAttrs = require("./dropdown-attrs");

var _dropdownAttrs2 = _interopRequireDefault(_dropdownAttrs);

function _interopRequireDefault(obj) { return obj && obj.__esModule ? obj : { default: obj }; }

var attrs = {
	"planets": ["name", "temperature", "diameter", "gravity", "mass"],
	"galaxies": ["name", "size"],
	"stars": ["name", "diameter", "temperature"],
	"satellites": ["name", "agency", "mission_type", "year_launched"]
};

var DropDown = function DropDown(_ref) {
	var modelType = _ref.modelType,
	    sortBy = _ref.sortBy,
	    sort_title = _ref.sort_title;

	var dir1 = "asc";
	var dir2 = "desc";
	var attrItem1 = attrs[modelType].map(function (attr) {
		return React.createElement(_dropdownAttrs2.default, {
			attr: attr,
			sortBy: sortBy,
			dir: dir1,
			key: attr });
	});
	var attrItem2 = attrs[modelType].map(function (attr) {
		return React.createElement(_dropdownAttrs2.default, {
			attr: attr,
			sortBy: sortBy,
			dir: dir2,
			key: attr });
	});
	return React.createElement(
		"div",
		{ className: "dropdown" },
		React.createElement(
			"button",
			{ className: "btn btn-primary dropdown-toggle", type: "button", "data-toggle": "dropdown" },
			sort_title,
			React.createElement("span", { className: "caret" })
		),
		React.createElement(
			"ul",
			{ className: "dropdown-menu" },
			React.createElement(
				"li",
				{ className: "dropdown-header" },
				"Ascending"
			),
			attrItem1,
			React.createElement("li", { className: "divider" }),
			React.createElement(
				"li",
				{ className: "dropdown-header" },
				"Descending"
			),
			attrItem2
		)
	);
};

exports.default = DropDown;

},{"./dropdown-attrs":2}],2:[function(require,module,exports){
"use strict";

Object.defineProperty(exports, "__esModule", {
				value: true
});
var Attribute = function Attribute(_ref) {
				var attr = _ref.attr,
				    sortBy = _ref.sortBy,
				    dir = _ref.dir;

				var label = { "name": "Name", "temperature": "Temperature", "diameter": "Diameter",
								"gravity": "Gravity", "mass": "Mass", "size": "Size", "agency": "Agency",
								"mission_type": "Mission Type", "year_launched": "Launch Year" };

				return React.createElement(
								"li",
								{ onClick: function onClick() {
																return sortBy(attr, dir, label[attr], 1);
												} },
								React.createElement(
												"a",
												null,
												label[attr]
								)
				);
};

exports.default = Attribute;

},{}],3:[function(require,module,exports){
"use strict";

Object.defineProperty(exports, "__esModule", {
	value: true
});

var Modals = function Modals(_ref) {
	var modelType = _ref.modelType,
	    filterBy = _ref.filterBy;


	return React.createElement(
		"div",
		null,
		React.createElement(
			"button",
			{ type: "button", className: "btn btn-primary", "data-toggle": "modal", "data-target": "#myModal" },
			"Filter By"
		),
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
							"Filtering"
						)
					),
					React.createElement(
						"div",
						{ className: "modal-body" },
						React.createElement(
							"div",
							{ className: "form-group" },
							React.createElement(
								"select",
								{ className: "form-control" },
								React.createElement(
									"option",
									{ value: "Attribute" },
									"Attribute"
								),
								React.createElement(
									"option",
									{ value: "Attr1" },
									"Attr 1"
								),
								React.createElement(
									"option",
									{ value: "Attr2" },
									"Attr 2"
								)
							),
							React.createElement(
								"select",
								{ className: "form-control" },
								React.createElement(
									"option",
									{ value: "Attribute" },
									"Operation"
								),
								React.createElement(
									"option",
									{ value: ">" },
									"Greater Then"
								),
								React.createElement(
									"option",
									{ value: "<" },
									"Greater Then"
								)
							),
							React.createElement(
								"select",
								{ className: "form-control" },
								React.createElement(
									"option",
									{ value: "Attribute" },
									"Compare To"
								),
								React.createElement(
									"option",
									{ value: "Attr1" },
									"Jupiter"
								),
								React.createElement(
									"option",
									{ value: "Attr2" },
									"Earth"
								)
							)
						)
					),
					React.createElement(
						"div",
						{ className: "modal-footer" },
						React.createElement(
							"button",
							{ type: "button", className: "btn btn-primary", "data-dismiss": "modal", onClick: function onClick() {
									return filterBy();
								} },
							"Submit"
						),
						React.createElement(
							"button",
							{ type: "button", className: "btn btn-default", "data-dismiss": "modal" },
							"Close"
						)
					)
				)
			)
		)
	);
};

exports.default = Modals;

},{}],4:[function(require,module,exports){
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

},{}],5:[function(require,module,exports){
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

},{}],6:[function(require,module,exports){
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

},{"./model_list_item":4}],7:[function(require,module,exports){
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

},{}],8:[function(require,module,exports){
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

},{}],9:[function(require,module,exports){
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
				}, className: "page-item", key: "previous-button" },
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
				key: i }));
		} else {
			pages.push(React.createElement(_page_item2.default, {
				page_number: i,
				onPageSelect: onPageSelect,
				isActive: false,
				key: i }));
		}
	}
	//adding next button
	if (current_page != total_pages) {
		pages.push(React.createElement(
			"li",
			{ onClick: function onClick() {
					return onPageSelect(current_page + 1);
				}, className: "page-item", key: "next-button" },
			React.createElement(
				"a",
				null,
				"Next"
			)
		));
	}

	return React.createElement(
		"ul",
		{ className: "pagination" },
		pages
	);
};

exports.default = Pages;

},{"./page_item":8}],10:[function(require,module,exports){
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

var _pages = require('./../components/pages');

var _pages2 = _interopRequireDefault(_pages);

var _modals = require('./../components/modals');

var _modals2 = _interopRequireDefault(_modals);

function _interopRequireDefault(obj) { return obj && obj.__esModule ? obj : { default: obj }; }

function _classCallCheck(instance, Constructor) { if (!(instance instanceof Constructor)) { throw new TypeError("Cannot call a class as a function"); } }

function _possibleConstructorReturn(self, call) { if (!self) { throw new ReferenceError("this hasn't been initialised - super() hasn't been called"); } return call && (typeof call === "object" || typeof call === "function") ? call : self; }

function _inherits(subClass, superClass) { if (typeof superClass !== "function" && superClass !== null) { throw new TypeError("Super expression must either be null or a function, not " + typeof superClass); } subClass.prototype = Object.create(superClass && superClass.prototype, { constructor: { value: subClass, enumerable: false, writable: true, configurable: true } }); if (superClass) Object.setPrototypeOf ? Object.setPrototypeOf(subClass, superClass) : subClass.__proto__ = superClass; }

var exts = { "planets": "Planets", "galaxies": "Galaxies", "satellites": "Satellites", "stars": "Stars" };
var modelType = window.location.href.split('/')[3];

var App = function (_React$Component) {
	_inherits(App, _React$Component);

	function App(props) {
		_classCallCheck(this, App);

		var _this = _possibleConstructorReturn(this, (App.__proto__ || Object.getPrototypeOf(App)).call(this, props));

		_this.state = {
			models: [],
			title: exts[window.location.href.split('/')[3]],
			total_pages: 1,
			current_page: 1,
			modelType: modelType,
			sort_title: "Sort By",
			current_sort_attr: null,
			current_sort_dir: null
		};

		_this.getModels(_this.state.current_page);
		return _this;
	}

	_createClass(App, [{
		key: 'getModels',
		value: function getModels(page) {
			var _this2 = this;

			if (this.state.sort_title === "Sort By") {
				// console.log("pages are not sorted");

				var baseUrl = window.location.href.split('/')[2];
				var apiExt = "/api/v1/" + this.state.modelType + "?page=" + page + "&results_per_page=9";
				var url = "http://" + baseUrl + apiExt;
				// console.log(url);
				fetch(url).then(function (response) {
					return response.json();
				}).then(function (responseJson) {
					// console.log("I'm back with some values");
					_this2.setState({
						models: responseJson.objects,
						total_pages: responseJson.total_pages,
						current_page: responseJson.page
					});
				}).catch(function (error) {
					console.error(error);
				});
			} else {
				// console.log("pages are sorted by " + this.state.sort_title);
				// console.log("using attr " + this.state.current_sort_attr);
				// console.log("by order " + this.state.current_sort_dir);
				this.sortBy(this.state.current_sort_attr, this.state.current_sort_dir, this.state.sort_title, page);
			}
		}
	}, {
		key: 'sortBy',
		value: function sortBy(attr, dir, sort_title, page) {
			var _this3 = this;

			// ?q={"order_by":[{"field": <fieldname>, "direction": <directionname>}]}
			// console.log(attr, dir);
			var baseUrl = window.location.href.split('/')[2];
			var apiExt = "/api/v1/" + this.state.modelType + "?page=" + page + "&results_per_page=9&q={%22order_by%22:[{%22field%22:%22" + attr + "%22,%22direction%22:%22" + dir + "%22}]}";
			var url = "http://" + baseUrl + apiExt;
			// console.log(url);
			fetch(url).then(function (response) {
				return response.json();
			}).then(function (responseJson) {
				// console.log("Back from sorting call");
				_this3.setState({
					models: responseJson.objects,
					total_pages: responseJson.total_pages,
					current_page: responseJson.page,
					sort_title: sort_title,
					current_sort_attr: attr,
					current_sort_dir: dir
				});
			}).catch(function (error) {
				console.error(error);
			});
		}
	}, {
		key: 'filterBy',
		value: function filterBy() {
			console.log("in filterBy func");
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
					{ className: 'container-fluid model-container' },
					React.createElement(_model_title2.default, { title: this.state.title }),
					React.createElement(
						'div',
						{ className: 'row' },
						React.createElement(
							'div',
							{ className: 'col-md-2 text-left sort-filter-button' },
							React.createElement(_drop_down2.default, {
								sort_title: this.state.sort_title,
								modelType: this.state.modelType,
								sortBy: this.sortBy.bind(this) })
						),
						React.createElement(
							'div',
							{ className: 'col-md-1 text-left sort-filter-button' },
							React.createElement(_modals2.default, {
								modelType: this.state.modelType,
								filterBy: this.filterBy.bind(this) })
						),
						React.createElement(
							'div',
							{ className: 'col-md-9 text-right' },
							React.createElement(_pages2.default, {
								current_page: this.state.current_page,
								total_pages: this.state.total_pages,
								onPageSelect: this.getModels.bind(this) })
						)
					),
					React.createElement(_models_list2.default, {
						models: this.state.models,
						page: this.current_page }),
					React.createElement(
						'div',
						{ key: 'pages', className: 'col-md-12 text-right' },
						React.createElement(_pages2.default, {
							current_page: this.state.current_page,
							total_pages: this.state.total_pages,
							onPageSelect: this.getModels.bind(this) })
					)
				)
			);
		}
	}]);

	return App;
}(React.Component);

ReactDOM.render(React.createElement(App, null), document.querySelector('.container'));

},{"./../components/drop_down":1,"./../components/modals":3,"./../components/model_title":5,"./../components/models_list":6,"./../components/nav_bar":7,"./../components/pages":9}]},{},[10]);
