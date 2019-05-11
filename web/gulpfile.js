const { src, dest, parallel } = require('gulp');
const less = require('gulp-less');
const minifyCSS = require('gulp-csso');
const concat = require('gulp-concat');

function html() {
  return src('client/**/*.html')
    .pipe(dest('build'))
}

function css() {
  return src('client/**/*.less')
    .pipe(concat('app.min.css'))
    .pipe(less())
    .pipe(dest('build/css'))
}

function js() {
  return src('client/**/*.js', { sourcemaps: true })
    .pipe(concat('app.min.js'))
    .pipe(dest('build/js', { sourcemaps: true }))
}

exports.js = js;
exports.css = css;
exports.html = html;
exports.default = parallel(html, css, js);
