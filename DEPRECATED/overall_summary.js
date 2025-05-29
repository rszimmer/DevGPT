const fs = require("fs");
const path = require("path");
const file_writer = require("./file_writer.js");

const jsonsInDir = fs
  .readdirSync("./json_results")
  .filter((file) => path.extname(file) === ".json");

const totalResults = {};
totalResults["htmlEntries"] = 0;
totalResults["languages"] = {};

jsonsInDir.forEach((file) => {
  const fileData = fs.readFileSync(path.join("./json_results", file));
  const json = JSON.parse(fileData.toString());
  for (ogType in json) {
    totalResults["htmlEntries"] += json[ogType]?.htmlEntries || 0;
    for (languageList in json[ogType]["languages"]) {
      if (
        typeof totalResults["languages"][languageList.toString()] === "number"
      ) {
        totalResults["languages"][languageList.toString()] +=
          json[ogType]["languages"][languageList.toString()];
      } else {
        totalResults["languages"][languageList.toString()] =
          json[ogType]["languages"][languageList.toString()] || 0;
      }
    }
  }
});

file_writer("overall_html", JSON.stringify(totalResults));
