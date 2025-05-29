const COMMIT0727 = require("../results/new_filter/prompt/0727_COMMIT.json");
const DISCUSSION0727 = require("../results/new_filter/prompt/0727_DISCUSSION.json");
const FILE0727 = require("../results/new_filter/prompt/0727_FILE.json");
const HN0727 = require("../results/new_filter/prompt/0727_HN.json");
const ISSUE0727 = require("../results/new_filter/prompt/0727_ISSUE.json");
const PR0727 = require("../results/new_filter/prompt/0727_PR.json");

module.exports = function concat_files(files) {
  let newObj = {};
  let iterator = 0;
  files.forEach((obj) => {
    for (let [key, item] of Object.entries(obj)) {
      if (Object.keys(item).length !== 0) {
        newObj[iterator] = item;
        iterator++;
      }
    }
  });
  return newObj;
};
