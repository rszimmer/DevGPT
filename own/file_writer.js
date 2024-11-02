const fs = require("node:fs");

module.exports = function file_writer(name, text) {
  fs.writeFile(`./file_results/${name}.txt`, text, (err) => {
    if (err) {
      console.error(err);
    } else {
    }
  });
};
