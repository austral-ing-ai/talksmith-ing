# OpenAI is winding down the fine-tuning API and platform - Discussion Thread - Deprecations - OpenAI Developer Community

_Source: <https://community.openai.com/t/openai-is-winding-down-the-fine-tuning-api-and-platform-discussion-thread/1380522>_

[OpenAI Developer Community](/) 

# [OpenAI is winding down the fine-tuning API and platform - Discussion Thread](/t/openai-is-winding-down-the-fine-tuning-api-and-platform-discussion-thread/1380522) 

[API](/c/api/7) [Deprecations](/c/api/deprecations/32) [itsarnavsalkade](https://community.openai.com/u/itsarnavsalkade)  May 8, 2026, 5:10pm 1 

So if i have fine tuned models on gpt4.1 mini and openai deprecates it does this mean my model will never be used for inference? So i would have wasted money and compute on it? For SFT only gpt4.1 variants are available and for RL only o4-mini is available so if im not wrong the degree of freedom to test and fine tune is anyway limited.

Also if GPT5.5 onwards models will be good at instruction following what would developers do with the money they have on the API Platform? As inference costs get cheaper and cheaper due to data center expansions and demands continue to increase will all inference be done using the same models released by OpenAI?

[_j](https://community.openai.com/u/_j)  May 8, 2026, 5:29pm 2 

o4-mini already has a shutoff date later in 2026. That was the first sign that fine-tuning was doomed.

gpt-4.1 series has not appeared in the deprecation list with a shutoff date. I anticipate you will have six months of deprecation notice before shutoff, and like the notice says, model shutoff is fine-tuning model shutoff when based on that model.

You choose which model you use on the API. You run a particular model name you have trained by API specification. To use a fine tuning trained model for inference generation, you specify the job-generated name with your prefix after it is created. Until it is turned off by OpenAI or you delete it.

OpenAI pricing has not become cheaper for API developers with new release models in 2026, instead, huge hikes. For now, there is a wide variety of models to run an API call against, as long as you accept that there is no aspect of machine learning experimentation and nothing emergent, novel, inspirational, educational to come out of these boring consumer products again.

[aprendendo.next](https://community.openai.com/u/aprendendo.next)  May 8, 2026, 6:53pm 3 

It seems they have given up on ft for now, at least until we get some Stargates up and running with some gpu power to spare…

![image](https://us1.discourse-cdn.com/openai1/original/4X/2/4/0/240c8016d7f41d5b36f0f6be0cef71c26ee0cdad.png)[image893×370 25.7 KB](https://us1.discourse-cdn.com/openai1/original/4X/2/4/0/240c8016d7f41d5b36f0f6be0cef71c26ee0cdad.png)

###  Related topics 

Topic Replies Views Activity [With gpt-4o being deprecated - what does that mean for gpt-4o fine tunes?](https://community.openai.com/t/with-gpt-4o-being-deprecated-what-does-that-mean-for-gpt-4o-fine-tunes/1374324) [Deprecations](/c/api/deprecations/32) 4 664  February 16, 2026 [GPT3 Model deprecation question](https://community.openai.com/t/gpt3-model-deprecation-question/312822) [API](/c/api/7) [gpt-4](https://community.openai.com/tag/gpt-4/10) , [chatgpt](https://community.openai.com/tag/chatgpt/16) 2 1615  July 31, 2023 [Deprecation of fine tuned models, but still can't access newer ones?](https://community.openai.com/t/deprecation-of-fine-tuned-models-but-still-cant-access-newer-ones/1379550) [Deprecations](/c/api/deprecations/32) [fine-tuning](https://community.openai.com/tag/fine-tuning/28) , [gpt-5](https://community.openai.com/tag/gpt-5/497) 4 643  April 22, 2026 [What will happen to the fine tuned projects on Open AI portal](https://community.openai.com/t/what-will-happen-to-the-fine-tuned-projects-on-open-ai-portal/1380479) [Deprecations](/c/api/deprecations/32) [fine-tuning](https://community.openai.com/tag/fine-tuning/28) 5 453  May 9, 2026 [OpenAI’s self-serve fine-tuning availability](https://community.openai.com/t/openai-s-self-serve-fine-tuning-availability/1380481) [API](/c/api/7) [fine-tuning](https://community.openai.com/tag/fine-tuning/28) , [api](https://community.openai.com/tag/api/33) 0 472  May 8, 2026
