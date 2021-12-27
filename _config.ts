import lume from "lume"
import attributes from "lume/plugins/attributes.ts"
import base_path from "lume/plugins/base_path.ts"
import bundler from "lume/plugins/bundler.ts"
import code_highlight from "lume/plugins/code_highlight.ts"
import date from "lume/plugins/date.ts"
import inline from "lume/plugins/inline.ts"
import jsx from "lume/plugins/jsx.ts"
import modify_urls from "lume/plugins/modify_urls.ts"
import on_demand from "lume/plugins/on_demand.ts"
import postcss from "lume/plugins/postcss.ts"
import pug from "lume/plugins/pug.ts"
import relative_urls from "lume/plugins/relative_urls.ts"
import resolve_urls from "lume/plugins/resolve_urls.ts"
import slugify_urls from "lume/plugins/slugify_urls.ts"
import svgo from "lume/plugins/svgo.ts"
import terser from "lume/plugins/terser.ts"

const site = lume()

site
  .use(attributes())
  .use(base_path())
  .use(bundler())
  .use(code_highlight())
  .use(date())
  .use(inline())
  .use(jsx())
  .use(modify_urls())
  .use(on_demand())
  .use(postcss())
  .use(pug())
  .use(relative_urls())
  .use(resolve_urls())
  .use(slugify_urls())
  .use(svgo())
  .use(terser())

export default site
