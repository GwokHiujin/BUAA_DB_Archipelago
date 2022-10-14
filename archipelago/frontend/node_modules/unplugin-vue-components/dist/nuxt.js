"use strict";Object.defineProperty(exports, "__esModule", {value: true});

var _chunkMF6CXARBjs = require('./chunk-MF6CXARB.js');
require('./chunk-EUNTLVSW.js');
require('./chunk-6F4PWJZI.js');

// src/nuxt.ts
function nuxt_default(options) {
  this.extendBuild((config) => {
    config.plugins = config.plugins || [];
    config.plugins.unshift(_chunkMF6CXARBjs.unplugin_default.webpack(options));
  });
  this.nuxt.hook("vite:extend", async (vite) => {
    vite.config.plugins = vite.config.plugins || [];
    vite.config.plugins.push(_chunkMF6CXARBjs.unplugin_default.vite(options));
  });
}


module.exports = nuxt_default;
exports.default = module.exports;