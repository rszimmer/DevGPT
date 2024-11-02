const fs = require("fs");
const path = require("path");
const file_writer = require("./file_writer.js");

const jsonsInDir = fs
  .readdirSync("./json_results")
  .filter((file) => path.extname(file) === ".json");

const totalResults = {};
totalResults["htmlEntries"] = 0;

jsonsInDir.forEach((file) => {
  const fileData = fs.readFileSync(path.join("./json_results", file));
  const json = JSON.parse(fileData.toString());
  for (ogType in json) {
    // console.log(json[ogType].htmlEntries);
    totalResults["htmlEntries"] += json[ogType]?.htmlEntries || 0;
  }
});

file_writer("overall_html", JSON.stringify(totalResults));
