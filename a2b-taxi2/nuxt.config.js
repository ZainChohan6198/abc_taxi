import pkg from './package'

export default {
  mode: 'universal',
  server: {
    port: 9191, // default: 3000
    host: '0.0.0.0' // default: localhost
  },
  /*
  ** Headers of the page
  */
  head: {
    title: 'A2B Tommyfield Cars',
    meta: [
      { charset: 'utf-8' },
      { name: 'viewport', content: 'width=device-width, initial-scale=1' },
      { hid: 'description', name: 'description', content: pkg.description },
      { name: 'keywords', content: 'taxi in oldham, a2b, a2b tommyfield, A2b Tommyfield cars, Taxi Service Uk, Taxi Uk' },
      { name: 'google-site-verification', content: 'XOhRlEowdQrORf8VgQ100a_2hfKdwloO3f8Wl_YBhnU' }
    ],
    link: [
      { rel: 'icon', type: 'image/x-icon', href: '/favicon.ico' },
      { rel: 'stylesheet', href: '/css/app.css' },
      { rel: 'stylesheet', href: 'https://fonts.googleapis.com/css?family=Montserrat:300,400,500,600,700|Roboto:300,400,500,700,900' },
      { rel: 'stylesheet', href: 'https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css', integrity: 'sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm', crossorigin: 'anonymous' }

    ],
    script: [
      { src: 'https://code.jquery.com/jquery-3.2.1.slim.min.js', integrity: 'sha384-KJ3o2DKtIkvYIK3UENzmM7KCkRr/rE9/Qpg6aAZGJwFDMVNA/GpGFF93hXpG5KkN', crossorigin: 'anonymous' },
      { src: 'https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.12.9/umd/popper.min.js', integrity: 'sha384-ApNbgh9B+Y1QKtv3Rn7W3mgPxhU9K/ScQsAP7hUibX39j7fakFPskvXusvfa0b4Q', crossorigin: 'anonymous' },
      { src: 'https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/js/bootstrap.min.js', integrity: 'sha384-JZR6Spejh4U02d8jOt6vLEHfe/JQGiRRSQQxSfFWpi1MquVdAyjUar5+76PVCmYl', crossorigin: 'anonymous' }

    ]

  },

  /*
  ** Customize the progress-bar color
  */

  loading: { color: '#fff' },

  /*
  ** Global CSS
  */
  css: [
    // Load a Node.js module directly (here it's a Sass file)
    // CSS file in the project
    // SCSS file in the project
    '@/assets/css/font-awesome.min.css',
    '@/assets/css/app.scss',
    '@/assets/css/fonts.css'
  ],
  /*
  ** Plugins to load before mounting the App
  */
  plugins: [
    '~/plugins/vue-autosuggest.js',
    '~/plugins/vue-datetime.js',
    '~/plugins/map.js',
    '~/plugins/axios.js',
    '~/plugins/moment.js'

  ],

  /*
  ** Nuxt.js modules
  */
  modules: [
    // Doc: https://axios.nuxtjs.org/usage
    '@nuxtjs/axios',
    ['@nuxtjs/dotenv', { filename: '.env.local' }]
  ],
  /*
  ** Axios module configuration
  */
  axios: {
    // See https://github.com/nuxt-community/axios-module#options
  },

  /*
  ** Build configuration
  */
  build: {
    transpile: [/^vue2-google-maps($|\/)/, /^vue2-gmap-custom-marker($|\/)/]
    /*
    ** You can extend webpack config here
    */
    // extend(config, ctx) {
    //   // Run ESLint on save
    //   if (ctx.isDev && ctx.isClient) {
    //     config.module.rules.push({
    //       enforce: 'pre',
    //       test: /\.(js|vue)$/,
    //       loader: 'eslint-loader',
    //       exclude: /(node_modules)/
    //     })
    //   }
    // }
  }
}
