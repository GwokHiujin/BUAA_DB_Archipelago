// vue.config.js
const AutoImport = require("unplugin-auto-import/webpack");
const Components = require("unplugin-vue-components/webpack");
const { ElementPlusResolver } = require("unplugin-vue-components/resolvers");

module.exports = {
  runtimeCompiler: true,
  lintOnSave: false,// 关闭语法检查
  configureWebpack: {
    plugins: [
      AutoImport({
        resolvers: [ElementPlusResolver()],
      }),
      Components({
        resolvers: [ElementPlusResolver()],
      }),
    ],
  },
  devServer: {
    host: '0.0.0.0', // 默认是localhost
    port: 8000, // 前端项目编译后使用的端口号，跟webpack配置的port同理
    proxy: {
      '/api': {
        target: "http://localhost:8000",
        secure: false,
        ws: true,
        changeOrigin: true,
        pathRewrite: {
          '^/api': '/api/',
        }
      }
    }
  }
};
