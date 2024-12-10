const { isUtf8 } = require("node:buffer");
const fs = require("node:fs");

module.exports = function file_writer(name, text) {
  fs.writeFile(`${name}.json`, text, "utf8", (err) => {
    if (err) {
      console.error(err);
    } else {
    }
  });
};
