module.exports = function filter_html(fileToRead) {
  const filterted_files = fileToRead?.Sources?.filter(
    (source) => source.RepoLanguage === "HTML" || source.RepoLanguage === "CSS",
  );

  return { ...filterted_files };
};
