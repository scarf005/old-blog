import lume from 'lume'
import codeHighlight from 'lume/plugins/code_highlight.ts'
import date from 'lume/plugins/date.ts'
import postcss from 'lume/plugins/postcss.ts'
import pug from 'lume/plugins/pug.ts'
import relativeUrls from 'lume/plugins/relative_urls.ts'
import terser from 'lume/plugins/terser.ts'

Deno.env.set('TZ', 'Asia/Seoul') // temporary solution to the date bug

const site = lume({
  location: new URL('https://www.maribel.dev'),
})

site
  .copy('CNAME')
  .copy('img')
  .ignore('README.md')
  .use(pug())
  .use(date())
  .use(codeHighlight())
  .use(postcss())
  .use(relativeUrls())
  .use(terser())
// .copy("img");
// .use(base_path())

export default site
