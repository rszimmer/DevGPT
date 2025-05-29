module.exports = function filter_html(fileToRead) {
  let mainObject = {};

  const filterted_files = fileToRead?.Sources?.filter((source) => {
    for (sharedgpt of source.ChatgptSharing) {
      if (sharedgpt?.Conversations)
        for (conversation of sharedgpt.Conversations) {
          for (codeItem of conversation.ListOfCode) {
            if (codeItem?.Type === "html") return true;
          }
        }
    }
  });

  mainObject["htmlEntries"] = filterted_files.length;
  const helperObj = {};

  for (item of filterted_files) {
    if (Object.keys(helperObj).includes(item.RepoLanguage)) {
      helperObj[item.RepoLanguage] += 1;
    } else {
      if (helperObj["undefined"] && item.RepoLanguage === undefined)
        helperObj[item.RepoLanguage] += 1;
      if (helperObj["null"] && item.RepoLanguage === null)
        helperObj[item.RepoLanguage] += 1;
      else helperObj[item.RepoLanguage] = 1;
    }
  }

  mainObject["languages"] = helperObj;

  return mainObject;
};
