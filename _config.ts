import lume from "lume"
import pug from "lume/plugins/pug.ts"
// import base_path from "lume/plugins/base_path.ts"
// import bundler from "lume/plugins/bundler.ts"
// import code_highlight from "lume/plugins/code_highlight.ts"
// import postcss from "lume/plugins/postcss.ts"
// import modify_urls from "lume/plugins/modify_urls.ts"
// import relative_urls from "lume/plugins/relative_urls.ts"
// import resolve_urls from "lume/plugins/resolve_urls.ts"
// import slugify_urls from "lume/plugins/slugify_urls.ts"
// import svgo from "lume/plugins/svgo.ts"
// import terser from "lume/plugins/terser.ts"

const site = lume()

site
  .use(pug())

export default site