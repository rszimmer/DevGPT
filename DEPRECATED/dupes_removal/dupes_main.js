const { textCosineSimilarity } = require("./cosine_similarity.js");
const COMMIT1012 = require("../results/new_filter/prompt/1012_COMMIT.json");
const FILE1012 = require("../results/new_filter/prompt/1012_FILE.json");
const ISSUE1012 = require("../results/new_filter/prompt/1012_ISSUE.json");
const PR1012 = require("../results/new_filter/prompt/1012_PR.json");
const DISCUSSION1012 = require("../results/new_filter/prompt/1012_DISCUSSION.json");
const CONCAT0727 = require("../results/dupes_removed/CONCAT_0727.json");
const CONCAT0803 = require("../results/dupes_removed/CONCAT_0803.json");
const CONCAT0810 = require("../results/dupes_removed/CONCAT_0810.json");
const CONCAT0817 = require("../results/dupes_removed/CONCAT_0817.json");
const CONCAT0824 = require("../results/dupes_removed/CONCAT_0824.json");
const CONCAT0831 = require("../results/dupes_removed/CONCAT_0831.json");
const CONCAT0907 = require("../results/dupes_removed/CONCAT_0907.json");
const CONCAT0914 = require("../results/dupes_removed/CONCAT_0914.json");
const CONCAT1012 = require("../results/dupes_removed/CONCAT_1012.json");
const file_writer = require("../file_writer.js");
const concat = require("./concat.js");

//Pegar o primeiro campo do objeto (removendo do objeto original)
//Comparar esse campo com os demais campos do objeto original
//Se: encontrar um igual, então remove aquele que é igual do objeto original
//Senão: vida que segue
//Colocar em um novo objeto
module.exports = function dupes_main() {
  [
    [
      concat([
        CONCAT0727,
        CONCAT0803,
        CONCAT0810,
        CONCAT0817,
        CONCAT0824,
        CONCAT0831,
        CONCAT0907,
        CONCAT0914,
        CONCAT1012,
      ]),
      "CONCATALL",
    ],
  ].forEach(([importedFile, name]) => {
    const objectLength = Object.keys(importedFile).length;
    const countedObjects = [];

    for (let i = 0; i < objectLength; i++) {
      while (importedFile[i] === undefined && i < objectLength) {
        i++;
      }
      const selectedEntry = importedFile[i];
      delete importedFile[i];
      for (let [key, value] of Object.entries(importedFile)) {
        if (Object.keys(value).length === Object.keys(selectedEntry).length) {
          let equalitySum = 0;
          for (let j = 0; j < Object.keys(selectedEntry).length; j++) {
            equalitySum += textCosineSimilarity(
              value[j].Promp,
              selectedEntry[j].Promp,
            );
          }
          if (equalitySum === Object.keys(selectedEntry).length) {
            delete importedFile[key];
          }
        }
      }
      countedObjects.push(selectedEntry);
    }

    file_writer(
      `../own/results/dupes_removed/${name}`,
      JSON.stringify({ ...countedObjects }),
    );
  });
};
