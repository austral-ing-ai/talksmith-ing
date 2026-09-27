# Fine-tuning LLMs Guide | Unsloth Documentation

_Source: <https://unsloth.ai/docs/get-started/fine-tuning-llms-guide>_

[Introducing Unsloth Desktop: the first local app to run & train models✨Read more](/docs/desktop)![Logo](https://unsloth.ai/docs/~gitbook/image?url=https%3A%2F%2F2815821428-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Forganizations%252FHpyELzcNe0topgVLGCZY%252Fsites%252Fsite_mXXTe%252Flogo%252F5W6YArempcQo3pu6l9mk%252Funsloth%2520final%2520space%2520black.png%3Falt%3Dmedia%26token%3Da204ba01-b272-4059-a60d-139dc5d1245d&width=260&dpr=3&quality=100&sign=a0dda7c9bab703764dcda9be60d63c3d&sv=3)![Logo](https://unsloth.ai/docs/~gitbook/image?url=https%3A%2F%2F2815821428-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Forganizations%252FHpyELzcNe0topgVLGCZY%252Fsites%252Fsite_mXXTe%252Flogo%252Fqb5xJcZ4NHJqPEnbI3U2%252Funsloth%2520final%2520space%2520white.png%3Falt%3Dmedia%26token%3Ded5bbc94-79d4-4abd-8b76-5d7ab3a1d468&width=260&dpr=3&quality=100&sign=9f7b99666d64a90520e3b1eee500b165&sv=3)</docs>⌘Ctrlk[Reddit](https://www.reddit.com/r/unsloth/)[Discord](https://discord.gg/unsloth)[GitHub](https://github.com/unslothai/unsloth)[Newsletter](https://unsloth.ai/newsletter)More🇺🇸 EnglishFor the complete documentation index, see [llms.txt](https://unsloth.ai/docs/llms.txt). This page is also available as [Markdown](https://unsloth.ai/docs/get-started/fine-tuning-llms-guide.md).CopyOn this page

# 🧬Fine-tuning LLMs Guide

Learn all the basics and best practices of fine-tuning. Beginner-friendly.

## 1. What Is Fine-tuning?<#id-1.-what-is-fine-tuning>

Fine-tuning / training / post-training models customizes its behavior, enhances + injects knowledge, and optimizes performance for domains and specific tasks. For example:

- 

OpenAI’s **GPT-5** was post-trained to improve instruction following and helpful chat behavior.

- 

The standard method of post training is called Supervised Fine-Tuning (SFT). Other methods include preference optimization (DPO, ORPO), distillation and [Reinforcement Learning (RL)](/docs/get-started/reinforcement-learning-rl-guide) (GRPO, GSPO), where an "agent" learns to make decisions by interacting with an environment and receiving **feedback** in the form of **rewards** or **penalties**.

With [Unsloth](https://github.com/unslothai/unsloth), you can fine-tune or do RL for free on Colab, Kaggle, or locally with just 3GB VRAM by using our [notebooks](https://docs.unsloth.ai/get-started/unsloth-notebooks). By fine-tuning a pre-trained model on a dataset, you can:

- 

**Update + Learn New Knowledge**: Inject and learn new domain-specific information.

- 

**Customize Behavior**: Adjust the model’s tone, personality, or response style.

- 

**Optimize for Tasks**: Improve accuracy and relevance for specific use cases.

**Example fine-tuning or RL use-cases**:

- 

Enables LLMs to predict if a headline impacts a company positively or negatively.

- 

Can use historical customer interactions for more accurate and custom responses.

- 

Fine-tune LLM on legal texts for contract analysis, case law research, and compliance.

You can think of a fine-tuned model as a specialized agent designed to do specific tasks more effectively and efficiently. **Fine-tuning can replicate all of RAG's capabilities**, but not vice versa.

#### ❓What is LoRA/QLoRA?<#what-is-lora-qlora>

In LLMs, we have model weights. Llama 70B has 70 billion numbers. Instead of changing all 70B numbers, we instead add thin matrices A and B to each weight, and optimize those. This means we only optimize 1% of weights. LoRA is when the original model is 16-bit unquantized while QLoRA quantizes to 4-bit to save 75% memory.

![](https://unsloth.ai/docs/~gitbook/image?url=https%3A%2F%2F3215535692-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FxhOjnexMCB3dmuQFQ2Zq%252Fuploads%252Fgit-blob-715b6260aae497f160d7f9a1019bcfa472675dcf%252Fimage%2520%287%29%2520%281%29%2520%281%29.png%3Falt%3Dmedia&width=768&dpr=3&quality=100&sign=34299e25f47606e1eb2c726e90eae33c&sv=3)Instead of optimizing Model Weights (yellow), we optimize 2 thin matrices A and B.

#### Fine-tuning misconceptions:<#fine-tuning-misconceptions>

You may have heard that fine-tuning does not make a model learn new knowledge or RAG performs better than fine-tuning. That is **false**. You can train a specialized coding model with fine-tuning and RL while RAG can’t change the model’s weights and only augments what the model sees at inference time. Read more FAQ + misconceptions [here](/docs/get-started/fine-tuning-for-beginners/faq-+-is-fine-tuning-right-for-me#fine-tuning-vs.-rag-whats-the-difference):

[🤔FAQ + Is Fine-tuning Right For Me?](/docs/get-started/fine-tuning-for-beginners/faq-+-is-fine-tuning-right-for-me)

> 

**** [Introducing Unsloth Studio:](/docs/new/studio) Our new open-source web UI for training and running models. This means you can now fine-tune models with no-code and have observability and automatic dataset creation features.

![](https://unsloth.ai/docs/~gitbook/image?url=https%3A%2F%2F3215535692-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FxhOjnexMCB3dmuQFQ2Zq%252Fuploads%252FxV1PO5DbF3ksB51nE2Tw%252Fmore%2520cropped%2520ui%2520for%2520homepage.png%3Falt%3Dmedia%26token%3Df75942c9-3d8d-4b59-8ba2-1a4a38de1b86&width=768&dpr=3&quality=100&sign=a643df6a4ccdb5a82a5163cea75e8bc3&sv=3)

## 2. Choose the Right Model + Method<#id-2.-choose-the-right-model--method>

If you're a beginner, it is best to start with a small instruct model like Llama 3.1 (8B) and experiment from there. You'll also need to decide between normal fine-tuning, RL, QLoRA or LoRA training:

- 

**Reinforcement Learning (RL) ** is used when you need a model to excel at a specific behavior (e.g., tool-calling) using an environment and reward function rather than labeled data. We have several [notebook examples](/docs/get-started/unsloth-notebooks#grpo-reasoning-rl-notebooks), but for most use-cases, standard SFT is sufficient.

- 

**LoRA** is a parameter efficient training method that typically keeps the base model’s weights frozen and trains a small set of added low-rank adapter weights (in 16-bit precision).

- 

**QLoRA** combines LoRA with 4-bit precision to handle very large models with minimal resources.

- 

Unsloth also supports full fine-tuning (FFT) and pretraining, which require significantly more resources, but FFT is usually unnecessary. When done correctly, LoRA can match FFT.

- 

Unsloth **all types models**: [text-to-speech](/docs/basics/text-to-speech-tts-fine-tuning), [embedding](/docs/basics/embedding-finetuning), GRPO, RL, [vision](/docs/basics/vision-fine-tuning), multimodal and more.

Research shows that **training and serving in the same precision** helps preserve accuracy. This means if you want to serve in 4-bit, train in 4-bit and vice versa.

We recommend starting with QLoRA, as it is one of the most accessible and effective methods for training models. Our [dynamic 4-bit](https://unsloth.ai/blog/dynamic-4bit) quants, the accuracy loss for QLoRA compared to LoRA is now largely recovered.

![](https://unsloth.ai/docs/~gitbook/image?url=https%3A%2F%2F3215535692-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FxhOjnexMCB3dmuQFQ2Zq%252Fuploads%252Fgit-blob-cfc51c261e6d24df3aa967d9b9a482313465cbc1%252Fmodel%2520name%2520change.png%3Falt%3Dmedia&width=768&dpr=3&quality=100&sign=4a1182a133a1fba11ac91f178215d3aa&sv=3)

You can change the model name to whichever model you like by matching it with model's name on Hugging Face e.g. '`unsloth/llama-3.1-8b-unsloth-bnb-4bit`'.

We recommend starting with **Instruct models**, as they allow direct fine-tuning using conversational chat templates (ChatML, ShareGPT etc.) and require less data compared to **Base models** (which uses Alpaca, Vicuna etc). Learn more about the differences between [instruct and base models here](/docs/get-started/fine-tuning-llms-guide/what-model-should-i-use#instruct-or-base-model).

- 

Model names ending in `**unsloth-bnb-4bit**` indicate they are ****[Unsloth dynamic 4-bit](https://unsloth.ai/blog/dynamic-4bit) **quants**. These models consume slightly more VRAM than standard BitsAndBytes 4-bit models but offer significantly higher accuracy.

- 

If a model name ends with just `**bnb-4bit**`, without "unsloth", it refers to a standard BitsAndBytes 4-bit quantization.

- 

Models with **no suffix** are in their original **16-bit or 8-bit formats**. While they are the original models from the official model creators, we sometimes include important fixes - such as chat template or tokenizer fixes. So it's recommended to use our versions when available.

There are other settings which you can toggle:

- 

`**max_seq_length = 2048**` – Controls context length. While Llama-3 supports 8192, we recommend 2048 for testing. Unsloth enables 4× longer context fine-tuning.

- 

`**dtype = None**` – Defaults to None; use `torch.float16` or `torch.bfloat16` for newer GPUs.

- 

`**load_in_4bit = True**` – Enables 4-bit quantization, reducing memory use 4× for fine-tuning. Disabling it enables LoRA 16-bit fine-tuning. You can also enable 16-bit LoRA with `load_in_16bit = True`

- 

To enable full fine-tuning (FFT), set `full_finetuning = True`. For 8-bit fine-tuning, set `load_in_8bit = True`.

- 

**Note:** Only one training method can be set to `True` at a time.

A common mistake is jumping straight into full fine-tuning (FFT), which is compute-heavy. Start by testing with LoRA or QLoRA first, if it won’t work there, it almost certainly won’t work with FFT. And if LoRA fails, don’t assume FFT will magically fix it.

You can also do [Text-to-speech (TTS)](/docs/basics/text-to-speech-tts-fine-tuning), [reasoning (GRPO)](/docs/get-started/reinforcement-learning-rl-guide), [vision](/docs/basics/vision-fine-tuning), [RL](/docs/get-started/reinforcement-learning-rl-guide/preference-dpo-orpo-and-kto) (GRPO, DPO), [continued pretraining](/docs/basics/continued-pretraining), text completion and other training methodologies with Unsloth.

Read our guide on choosing models:

[❓What Model Should I Use?](/docs/get-started/fine-tuning-llms-guide/what-model-should-i-use)

For inidivudal tutorials on models:

[Complete LLM Directory](/docs/models/tutorials)

## 3. Your Dataset<#id-3.-your-dataset>

For LLMs, datasets are collections of data that can be used to train our models. In order to be useful for training, text data needs to be in a format that can be tokenized.

- 

You will need to create a dataset usually with 2 columns - question and answer. The quality and amount will largely reflect the end result of your fine-tune so it's imperative to get this part right.

- 

You can [synthetically generate data](/docs/get-started/fine-tuning-llms-guide/datasets-guide#synthetic-data-generation) and structure your dataset (into QA pairs) using ChatGPT or local LLMs.

- 

You can also use our new Synthetic Dataset notebook which automatically parses documents (PDFs, videos etc.), generates QA pairs and auto cleans data using local models like Llama 3.2. [Access the notebook here.](https://colab.research.google.com/github/unslothai/notebooks/blob/main/nb/Meta_Synthetic_Data_Llama3_2_(3B).ipynb)

- 

Fine-tuning can learn from an existing repository of documents and continuously expand its knowledge base, but just dumping data alone won’t work as well. For optimal results, curate a well-structured dataset, ideally as question-answer pairs. This enhances learning, understanding, and response accuracy.

- 

But, that's not always the case, e.g. if you are fine-tuning a LLM for code, just dumping all your code data can actually enable your model to yield significant performance improvements, even without structured formatting. So it really depends on your use case.

***Read more about creating your dataset:***

[📈Datasets Guide](/docs/get-started/fine-tuning-llms-guide/datasets-guide)

For most of our notebook examples, we utilize the [Alpaca dataset](https://docs.unsloth.ai/basics/tutorial-how-to-finetune-llama-3-and-use-in-ollama#id-6.-alpaca-dataset) however other notebooks like Vision will use different datasets which may need images in the answer ouput as well.

### 4. Understand Training Hyperparameters<#id-4.-understand-training-hyperparameters>

Learn how to choose the right [hyperparameters](/docs/get-started/fine-tuning-llms-guide/lora-hyperparameters-guide) using best practices from research and real-world experiments - and understand how each one affects your model's performance.

**For a complete guide on how hyperparameters affect training, see:**

[🧠Hyperparameters Guide](/docs/get-started/fine-tuning-llms-guide/lora-hyperparameters-guide)

## 5. Install + Requirements<#id-5.-install--requirements>

You can use Unsloth via two main ways, our free notebooks or locally.

### Unsloth Notebooks<#unsloth-notebooks>

We would recommend beginners to utilise our pre-made [notebooks](/docs/get-started/unsloth-notebooks) first as it's the easiest way to get started with guided steps. You can later export the notebooks to use locally.

Unsloth has step-by-step notebooks for [text-to-speech](/docs/basics/text-to-speech-tts-fine-tuning), [embedding](/docs/basics/embedding-finetuning), GRPO, RL, [vision](/docs/basics/vision-fine-tuning), multimodal, different use-cases and more.

### Local Installation<#local-installation>

You can also install Unsloth locally via [Docker](/docs/get-started/install/docker) or `pip install unsloth` (with Linux, WSL or [Windows](/docs/get-started/install/windows-installation)). Also depending on the model you're using, you'll need enough VRAM and resources.

Installing Unsloth will require a Windows or Linux device. Once you install Unsloth, you can copy and paste our notebooks and use them in your own local environment. See:

[🛠️Unsloth Requirements](/docs/get-started/fine-tuning-for-beginners/unsloth-requirements)[📥Installation](/docs/get-started/install)

## 6. Training + Evaluation<#id-6.-training--evaluation>

Once you have everything set, it's time to train! If something's not working, remember you can always change hyperparameters, your dataset etc.

You’ll see a log of numbers during training. This is the training loss, which shows how well the model is learning from your dataset. For many cases, a loss around 0.5 to 1.0 is a good sign, but it depends on your dataset and task. If the loss is not going down, you might need to adjust your settings. If the loss goes to 0, that could mean overfitting, so it's important to check validation too.

![](https://unsloth.ai/docs/~gitbook/image?url=https%3A%2F%2F3215535692-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FxhOjnexMCB3dmuQFQ2Zq%252Fuploads%252Fgit-blob-feb9b0f5763d41cecaec9a3a9cd227ad918f0ca7%252Fimage.png%3Falt%3Dmedia&width=768&dpr=3&quality=100&sign=532fef9e2847314dd2481babe6c877c5&sv=3)The training loss will appear as numbers

We generally recommend keeping the default settings unless you need longer training or larger batch sizes.

- 

`**per_device_train_batch_size = 2**` – Increase for better GPU utilization but beware of slower training due to padding. Instead, increase `gradient_accumulation_steps` for smoother training.

- 

`**gradient_accumulation_steps = 4**` – Simulates a larger batch size without increasing memory usage.

- 

`**max_steps = 60**` – Speeds up training. For full runs, replace with `num_train_epochs = 1` (1–3 epochs recommended to avoid overfitting).

- 

`**learning_rate = 2e-4**` – Lower for slower but more precise fine-tuning. Try values like `1e-4`, `5e-5`, or `2e-5`.

#### Evaluation<#evaluation>

In order to evaluate, you could do manually evaluation by just chatting with the model and see if it's to your liking. You can also enable evaluation for Unsloth, but keep in mind it can be time-consuming depending on the dataset size. To speed up evaluation you can: reduce the evaluation dataset size or set `evaluation_steps = 100`.

For testing, you can also take 20% of your training data and use that for testing. If you already used all of the training data, then you have to manually evaluate it. You can also use automatic eval tools but keep in mind that automated tools may not perfectly align with your evaluation criteria.

## 7. Running + Deploying the model<#id-7.-running--deploying-the-model>

Now let's run the model after we completed the training process! You can edit the yellow underlined part! In fact, because we created a multi turn chatbot, we can now also call the model as if it saw some conversations in the past like below:

![](https://unsloth.ai/docs/~gitbook/image?url=https%3A%2F%2F3215535692-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FxhOjnexMCB3dmuQFQ2Zq%252Fuploads%252Fgit-blob-f2d5f23fa62ec89e06bf20fea433f9a1e42a2fe3%252Fimage.png%3Falt%3Dmedia&width=768&dpr=3&quality=100&sign=4b3c1daeb3bdbb75fef3913530a9cfd1&sv=3)![](https://unsloth.ai/docs/~gitbook/image?url=https%3A%2F%2F3215535692-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FxhOjnexMCB3dmuQFQ2Zq%252Fuploads%252Fgit-blob-cdf5d779635901dce7793df92531dbf3caf0fb0a%252Fimage%2520%2847%29.png%3Falt%3Dmedia&width=768&dpr=3&quality=100&sign=550e180a8b26c3914310745b808499a8&sv=3)

Reminder Unsloth itself provides **2x faster inference** natively as well, so always do not forget to call `FastLanguageModel.for_inference(model)`. If you want the model to output longer responses, set `max_new_tokens = 128` to some larger number like 256 or 1024. Notice you will have to wait longer for the result as well!

### Saving + Deployment<#saving--deployment>

For saving and deploying your model in desired inference engines like Ollama, vLLM, Open WebUI, you will need to use the LoRA adapter on top of the base model. We have designated guides for each framework:

[🖥️Inference & Deployment](/docs/basics/inference-and-deployment)

If you’re running inference on a single device (like a laptop or Mac), use llama.cpp to convert to GGUF format to use in Ollama, llama.cpp, LM Studio etc:

[GGUF & llama.cpp](/docs/basics/inference-and-deployment/saving-to-gguf)

If you’re deploying an LLM for enterprise or multi-user inference for FP8, AWQ, use vLLM:

[vLLM](/docs/basics/inference-and-deployment/vllm-guide)

We can now save the fine-tuned model as a small 100MB file called a LoRA adapter like below. You can instead push to the Hugging Face hub as well if you want to upload your model! Remember to get a Hugging Face [token](https://huggingface.co/settings/tokens) and add your token!

![](https://unsloth.ai/docs/~gitbook/image?url=https%3A%2F%2F3215535692-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FxhOjnexMCB3dmuQFQ2Zq%252Fuploads%252Fgit-blob-8c577103f7c4fe883cabaf35c8437307c6501686%252Fimage.png%3Falt%3Dmedia&width=768&dpr=3&quality=100&sign=c45907e48ea5d416f5dc32aa737e7d41&sv=3)![](https://unsloth.ai/docs/~gitbook/image?url=https%3A%2F%2F3215535692-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FxhOjnexMCB3dmuQFQ2Zq%252Fuploads%252Fgit-blob-1a1be852ca551240bdce47cf99e6ccd7d31c1326%252Fimage.png%3Falt%3Dmedia&width=768&dpr=3&quality=100&sign=c2ec65ab33451f07159854446b9c20ab&sv=3)

After saving the model, we can again use Unsloth to run the model itself! Use `FastLanguageModel` again to call it for inference!

## 8. We're done!<#id-8.-were-done>

You've successfully fine-tuned a language model and exported it to your desired inference engine with Unsloth!

To learn more about fine-tuning tips and tricks, head over to our blogs which provide tremendous and educational value: [https://unsloth.ai/blog/](https://unsloth.ai/blog/)

If you need any help on fine-tuning, you can also join our Discord server [here](https://discord.gg/unsloth) or [Reddit r/unsloth](https://www.reddit.com/r/unsloth/). Thanks for reading and hopefully this was helpful!

![](https://unsloth.ai/docs/~gitbook/image?url=https%3A%2F%2F3215535692-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FxhOjnexMCB3dmuQFQ2Zq%252Fuploads%252Fgit-blob-69482ba90d417f7bf98dddaf83795cdd3eb20efc%252Fsloth%2520sparkling%2520square.png%3Falt%3Dmedia&width=768&dpr=3&quality=100&sign=6305e913b9cf60fa33d8e788024abdad&sv=3)[PreviousUnsloth Notebooks](/docs/get-started/unsloth-notebooks)[NextDatasets Guide](/docs/get-started/fine-tuning-llms-guide/datasets-guide)

Last updated 6 months ago

Was this helpful?

- [1. What Is Fine-tuning?](#id-1.-what-is-fine-tuning)
- [2. Choose the Right Model + Method](#id-2.-choose-the-right-model--method)
- [3. Your Dataset](#id-3.-your-dataset)
- [4. Understand Training Hyperparameters](#id-4.-understand-training-hyperparameters)
- [5. Install + Requirements](#id-5.-install--requirements)
- [Unsloth Notebooks](#unsloth-notebooks)
- [Local Installation](#local-installation)
- [6. Training + Evaluation](#id-6.-training--evaluation)
- [7. Running + Deploying the model](#id-7.-running--deploying-the-model)
- [Saving + Deployment](#saving--deployment)
- [8. We're done!](#id-8.-were-done)

Was this helpful?
