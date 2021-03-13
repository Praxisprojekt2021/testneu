import i18next from 'https://deno.land/x/i18next/index.js'
    import Backend from 'https://deno.land/x/i18next_fs_backend/index.js'
    i18next
  .use(Backend)
  .init({
    /*backend: {
      loadPath: __dirname + 'i18n/de.json',
    }*/
    resources: {
    de: {
      translation: {
        "hello": "Hallo Welt"
      }
    }
  },
    fallbackLng: 'de',
    preload: ['de'],
  }), function(err, t) {
  // initialized and ready to go!
  document.getElementById('output').innerHTML = i18next.t('hello');
};