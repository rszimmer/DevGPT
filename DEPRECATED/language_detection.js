module.exports = function languageDetector(fileToRead) {
  function onLanguageDetected(langInfo) {
    for (const lang of langInfo.languages) {
      console.log(`Language is: ${lang.language}`);
      console.log(`Percentage is: ${lang.percentage}`);
    }
  }

  let text = "L'homme est né libre, et partout il est dans les fers.";

  let detecting = browser.i18n.detectLanguage(text);
  detecting.then(onLanguageDetected);
};
