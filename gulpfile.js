// requirements

var gulp = require('gulp');
var gulpBrowser = require("gulp-browser");
var reactify = require('reactify');
var del = require('del');
var size = require('gulp-size');


// tasks

gulp.task('transform', function () {
  var stream = gulp.src('./app/static/jsx/*.js')
    .pipe(gulpBrowser.browserify({transform: ['reactify']}))
    .pipe(gulp.dest('./app/static/js/'))
    .pipe(size());
  return stream;
});

gulp.task('del', function () {
  return del(['./project/static/js']);
});

gulp.task('default', ['del'], function() {
  gulp.start('transform');
});