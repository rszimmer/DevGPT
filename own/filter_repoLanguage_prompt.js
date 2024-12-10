module.exports = function filter_repoLanguage_prompt(fileToRead) {
  const filterted_files = fileToRead?.Sources?.filter(
    (source) => source.RepoLanguage === "HTML" || source.RepoLanguage === "CSS",
  );

  const final_array = filterted_files?.map((source) => {
    const chatgptSharing_array = [];
    const conversations_array = [];
    for (sharedgpt of source.ChatgptSharing) {
      if (sharedgpt?.Conversations) {
        for (conversation of sharedgpt.Conversations) {
          conversations_array.push({
            Promp: conversation.Prompt,
            // Answer: conversation.Answer,
          });
        }
      }
      chatgptSharing_array.push(...conversations_array);
    }
    return { ...chatgptSharing_array };
  });

  return { ...final_array };
};
