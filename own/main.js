const filter_html = require("./filter_html.js");
const file_writer = require("./file_writer.js");
const imports0727 = require("./data_import/exports_0727.js");
const imports0803 = require("./data_import/exports_0803.js");
const imports0810 = require("./data_import/exports_0810.js");
const imports0817 = require("./data_import/exports_0817.js");
const imports0824 = require("./data_import/exports_0824.js");
const imports0831 = require("./data_import/exports_0831.js");
const imports0907 = require("./data_import/exports_0907.js");
const imports0914 = require("./data_import/exports_0914.js");
// const imports1012 = require("./data_import/exports_1012.js");

[
  [imports0727, "0727"],
  [imports0803, "0803"],
  [imports0810, "0810"],
  [imports0817, "0817"],
  [imports0824, "0824"],
  [imports0831, "0831"],
  [imports0907, "0907"],
  [imports0914, "0914"],
  // [imports1012, "1012"],
].forEach(([importedFile, name]) => {
  let mainObject = {};
  for (importFile in importedFile) {
    mainObject[importFile] = filter_html(importedFile[importFile]);
  }
  file_writer(name, JSON.stringify(mainObject));
});
