const fs = require("node:fs");

module.exports = function file_writer(name, text) {
  fs.writeFile(`./json_results/${name}.json`, text, (err) => {
    if (err) {
      console.error(err);
    } else {
    }
  });
};
