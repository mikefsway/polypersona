# PolyPersona
 This package uses the GPT3.5 API to create a diverse sample of automated survey respondents, which can then respond to survey questions you provide. 

 ## Introduction
 I'm a social researcher in energy, and I occasionally need to run social surveys and survey experiments. I'm interested in exploring whether Large Language Models (LLMs) can usefully simulate survey responses. This could be helpful in making sure questions are clearly phrased, anticipating what could be the most effective experimental conditions to try for real, and perhaps even using in place of social surveys where the application would make a survey impractical.

 ## How it works
 Polypersona is powered by the GPT3.5 API. When the program runs, it endows the system role with combination of demographic, attitudinal, and personality characteristics. These are combined with the survey question and a response requested from the API. The demographic characteristics vary probabilistically in line with UK population data, while most other characteristics are classed as either high, medium, or low with an equal probability. The response is returned in JSON format and recorded in a CSV. 
 
 ## How to use it
 You can set up the demographic, attitudinal, personalility (and any other charateristics you would like to add) in the demoprobs.csv file, along with their probabilities. Likewise, the survey question variations and response formats can be set in conditions.csv. Comments should be self-explanatory in the polypersona.py file. You will need an OpenAI API key, which I suggest you set up as an environment variable according to the instructions in step 2 <a href="https://platform.openai.com/docs/quickstart?context=python">here</a>. 