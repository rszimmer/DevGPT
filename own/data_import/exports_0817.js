const fs = require("fs");
const path = require("path");

const jsonsInDir = fs
  .readdirSync("../snapshot_20230817")
  .filter((file) => path.extname(file) === ".json");

const objHelper = {};
const filesNameList = ["PR", "ISSUE", "DISCUSSION", "COMMIT", "FILE", "HN"];

jsonsInDir.forEach((file) => {
  const fileData = fs.readFileSync(path.join("../snapshot_20230817", file));
  const name = filesNameList.filter((e) => file.toUpperCase().includes(e))[0];
  const json = JSON.parse(fileData.toString());
  objHelper[name] = json;
});

module.exports = objHelper;
