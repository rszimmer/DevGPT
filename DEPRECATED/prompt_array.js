const CONCAT0727 = require("./results/dupes_removed/CONCAT_0727.json");
const file_writer = require("./file_writer.js");

module.exports = function prompt_array() {
  const finalArray = [];
  for (let outerObject of Object.values(CONCAT0727)) {
    finalArray.push(outerObject[0].Promp);
    // console.log(outerObject[0].Promp);
  }

  return finalArray;
};
