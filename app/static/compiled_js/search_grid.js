(function e(t,n,r){function s(o,u){if(!n[o]){if(!t[o]){var a=typeof require=="function"&&require;if(!u&&a)return a(o,!0);if(i)return i(o,!0);var f=new Error("Cannot find module '"+o+"'");throw f.code="MODULE_NOT_FOUND",f}var l=n[o]={exports:{}};t[o][0].call(l.exports,function(e){var n=t[o][1][e];return s(n?n:e)},l,l.exports,e,t,n,r)}return n[o].exports}var i=typeof require=="function"&&require;for(var o=0;o<r.length;o++)s(r[o]);return s})({1:[function(require,module,exports){
"use strict";

Object.defineProperty(exports, "__esModule", {
	value: true
});

var _createClass = function () { function defineProperties(target, props) { for (var i = 0; i < props.length; i++) { var descriptor = props[i]; descriptor.enumerable = descriptor.enumerable || false; descriptor.configurable = true; if ("value" in descriptor) descriptor.writable = true; Object.defineProperty(target, descriptor.key, descriptor); } } return function (Constructor, protoProps, staticProps) { if (protoProps) defineProperties(Constructor.prototype, protoProps); if (staticProps) defineProperties(Constructor, staticProps); return Constructor; }; }();

function _classCallCheck(instance, Constructor) { if (!(instance instanceof Constructor)) { throw new TypeError("Cannot call a class as a function"); } }

function _possibleConstructorReturn(self, call) { if (!self) { throw new ReferenceError("this hasn't been initialised - super() hasn't been called"); } return call && (typeof call === "object" || typeof call === "function") ? call : self; }

function _inherits(subClass, superClass) { if (typeof superClass !== "function" && superClass !== null) { throw new TypeError("Super expression must either be null or a function, not " + typeof superClass); } subClass.prototype = Object.create(superClass && superClass.prototype, { constructor: { value: subClass, enumerable: false, writable: true, configurable: true } }); if (superClass) Object.setPrototypeOf ? Object.setPrototypeOf(subClass, superClass) : subClass.__proto__ = superClass; }

var ModelListItem = function (_React$Component) {
	_inherits(ModelListItem, _React$Component);

	function ModelListItem(props) {
		_classCallCheck(this, ModelListItem);

		var _this = _possibleConstructorReturn(this, (ModelListItem.__proto__ || Object.getPrototypeOf(ModelListItem)).call(this, props));

		var base_url = "/" + _this.props.model.model_type + "/";
		var link = base_url + _this.props.model.pid;
		_this.state = {
			style: {
				width: '400px',
				height: '400px'
			},
			image_url: "/undefined",
			link: link
		};
		var image_url = "/api/v1" + base_url + _this.props.model.pid + "/image";
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

	_createClass(ModelListItem, [{
		key: "render",
		value: function render() {
			return React.createElement(
				"div",
				{ className: "col-lg-4 col-md-6 col-sm-12 text-center model-list-item" },
				React.createElement(
					"a",
					{ href: this.state.link },
					React.createElement("img", { className: "img-thumbnail about-image", style: this.state.style, src: this.state.image_url }),
					React.createElement(
						"h3",
						null,
						this.props.model.name
					)
				)
			);
		}
	}]);

	return ModelListItem;
}(React.Component);

;

exports.default = ModelListItem;

},{}],2:[function(require,module,exports){
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
			{ className: "col-lg-12 text-center" },
			React.createElement(
				"h1",
				null,
				title
			)
		)
	);
};

exports.default = ModelTitle;

},{}],3:[function(require,module,exports){
"use strict";

Object.defineProperty(exports, "__esModule", {
	value: true
});

var _model_list_item = require("./model_list_item");

var _model_list_item2 = _interopRequireDefault(_model_list_item);

function _interopRequireDefault(obj) { return obj && obj.__esModule ? obj : { default: obj }; }

var ModelList = function ModelList(props) {
	var modelItem = props.models.map(function (model) {
		return React.createElement(_model_list_item2.default, { model: model });
	});
	return React.createElement(
		"div",
		{ className: "row" },
		modelItem
	);
};

exports.default = ModelList;

},{"./model_list_item":1}],4:[function(require,module,exports){
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

},{}],5:[function(require,module,exports){
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

},{}],6:[function(require,module,exports){
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
	if (current_page != total_pages && current_page > 1) {
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

},{"./page_item":5}],7:[function(require,module,exports){
'use strict';

var _createClass = function () { function defineProperties(target, props) { for (var i = 0; i < props.length; i++) { var descriptor = props[i]; descriptor.enumerable = descriptor.enumerable || false; descriptor.configurable = true; if ("value" in descriptor) descriptor.writable = true; Object.defineProperty(target, descriptor.key, descriptor); } } return function (Constructor, protoProps, staticProps) { if (protoProps) defineProperties(Constructor.prototype, protoProps); if (staticProps) defineProperties(Constructor, staticProps); return Constructor; }; }();

var _nav_bar = require('./../components/nav_bar');

var _nav_bar2 = _interopRequireDefault(_nav_bar);

var _models_list = require('./../components/models_list');

var _models_list2 = _interopRequireDefault(_models_list);

var _model_title = require('./../components/model_title');

var _model_title2 = _interopRequireDefault(_model_title);

var _pages = require('./../components/pages');

var _pages2 = _interopRequireDefault(_pages);

require('isomorphic-fetch');

function _interopRequireDefault(obj) { return obj && obj.__esModule ? obj : { default: obj }; }

function _classCallCheck(instance, Constructor) { if (!(instance instanceof Constructor)) { throw new TypeError("Cannot call a class as a function"); } }

function _possibleConstructorReturn(self, call) { if (!self) { throw new ReferenceError("this hasn't been initialised - super() hasn't been called"); } return call && (typeof call === "object" || typeof call === "function") ? call : self; }

function _inherits(subClass, superClass) { if (typeof superClass !== "function" && superClass !== null) { throw new TypeError("Super expression must either be null or a function, not " + typeof superClass); } subClass.prototype = Object.create(superClass && superClass.prototype, { constructor: { value: subClass, enumerable: false, writable: true, configurable: true } }); if (superClass) Object.setPrototypeOf ? Object.setPrototypeOf(subClass, superClass) : subClass.__proto__ = superClass; }

var App = function (_React$Component) {
	_inherits(App, _React$Component);

	function App(props) {
		_classCallCheck(this, App);

		var _this = _possibleConstructorReturn(this, (App.__proto__ || Object.getPrototypeOf(App)).call(this, props));

		var dict = {};
		dict['page'] = 1;
		var href = window.location.href;
		if (href.indexOf('?') >= 0 && href.indexOf('&') >= 0) {
			var parameters = window.location.href.split('?')[1].split('&');
			for (var i = 0; i < parameters.length; i += 1) {
				var key = parameters[i].split('=')[0];
				var value = parameters[i].split('=')[1];
				dict[key] = value;
			}
		} else if (href.indexOf('?') >= 0) {
			var parameters = window.location.href.split('?')[1];
			var key = parameters.split('=')[0];
			var value = parameters.split('=')[1];
			dict[key] = value;
		}
		_this.state = {
			models: [],
			total_pages: 1,
			current_page: Number(dict['page']),
			loaded: false,
			search: dict['q']
		};
		_this.getModels();
		return _this;
	}

	_createClass(App, [{
		key: 'getModels',
		value: function getModels() {
			var _this2 = this;

			var url = "/api/v1/search?page=" + this.state.current_page + "&results_per_page=6&q=" + this.state.search;
			fetch(url).then(function (response) {
				return response.json();
			}).then(function (responseJson) {
				_this2.setState({
					models: responseJson.objects,
					total_pages: responseJson.total_pages,
					current_page: responseJson.page,
					loaded: true
				});
			}).catch(function (error) {
				console.error(error);
			});
		}
	}, {
		key: 'redirect',
		value: function redirect() {
			var url = "/search?page=" + this.state.current_page + "&q=" + this.state.search;
			window.location = url;
		}
	}, {
		key: 'changePage',
		value: function changePage(page) {
			this.state['current_page'] = page;
			this.redirect();
		}
	}, {
		key: 'render',
		value: function render() {
			if (!this.state.loaded) {
				return React.createElement(
					'h1',
					{ className: 'text-center' },
					'Loading Search Results'
				);
			}
			if (this.state.models.length <= 0) {
				return React.createElement(
					'h1',
					{ className: 'text-center' },
					'No Results Found'
				);
			}
			return React.createElement(
				'div',
				{ className: 'model-container' },
				React.createElement(_model_title2.default, { title: 'Search Results' }),
				React.createElement(
					'div',
					{ className: 'row' },
					React.createElement(
						'div',
						{ className: 'col-md-12 text-center' },
						React.createElement(_pages2.default, {
							current_page: this.state.current_page,
							total_pages: this.state.total_pages,
							onPageSelect: this.changePage.bind(this) })
					)
				),
				React.createElement(_models_list2.default, {
					models: this.state.models,
					page: this.current_page }),
				React.createElement(
					'div',
					{ key: 'pages', className: 'col-md-12 text-center' },
					React.createElement(_pages2.default, {
						current_page: this.state.current_page,
						total_pages: this.state.total_pages,
						onPageSelect: this.changePage.bind(this) })
				)
			);
		}
	}]);

	return App;
}(React.Component);

ReactDOM.render(React.createElement(App, null), document.querySelector('.content-container'));

},{"./../components/model_title":2,"./../components/models_list":3,"./../components/nav_bar":4,"./../components/pages":6,"isomorphic-fetch":8}],8:[function(require,module,exports){
// the whatwg-fetch polyfill installs the fetch() function
// on the global object (window or self)
//
// Return that as the export for use in Webpack, Browserify etc.
require('whatwg-fetch');
module.exports = self.fetch.bind(self);

},{"whatwg-fetch":9}],9:[function(require,module,exports){
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

},{}]},{},[7]);
