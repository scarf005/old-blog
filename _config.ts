import lume from 'lume'
import code_highlight from 'lume/plugins/code_highlight.ts'
import date from 'lume/plugins/date.ts'
import postcss from 'lume/plugins/postcss.ts'
import pug from 'lume/plugins/pug.ts'
import relative_urls from 'lume/plugins/relative_urls.ts'
import terser from 'lume/plugins/terser.ts'

const site = lume({
  location: new URL('https://www.maribel.dev'),
})

site
  .copy('CNAME')
  .ignore('README.md')
  .use(pug())
  .use(date())
  .use(code_highlight())
  .use(postcss())
  .use(relative_urls())
  .use(terser())
// .copy("img");
// .use(resolve_urls())
// .use(base_path())

export default site
