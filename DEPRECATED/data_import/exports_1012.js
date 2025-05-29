const fs = require("fs");
const path = require("path");

const jsonsInDir = fs
  .readdirSync("../snapshot_20231012")
  .filter((file) => path.extname(file) === ".json");

const objHelper = {};
const filesNameList = ["PR", "ISSUE", "DISCUSSION", "COMMIT", "FILE", "HN"];

jsonsInDir.forEach((file) => {
  const fileData = fs.readFileSync(path.join("../snapshot_20231012", file));
  const name = filesNameList.filter((e) => file.toUpperCase().includes(e))[0];
  let json;
  try {
    json = JSON.parse(fileData.toString());
  } catch {}
  objHelper[name] = json;
});

module.exports = objHelper;
