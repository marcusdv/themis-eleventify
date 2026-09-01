module.exports = function(eleventyConfig) {
  // Pass through assets
  eleventyConfig.addPassthroughCopy("src/assets");
  eleventyConfig.addPassthroughCopy("src/tools");

  // Set input and output directories
  return {
    dir: {
      input: "src",
      output: "_output",
      includes: "_includes",
      layouts: "_layouts",
    },
  };
};
