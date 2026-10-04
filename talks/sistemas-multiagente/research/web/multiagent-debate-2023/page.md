# [2305.14325] Improving Factuality and Reasoning in Language Models through Multiagent Debate

_Source: <https://ar5iv.labs.arxiv.org/html/2305.14325>_

# Improving Factuality and Reasoning in Language Models through Multiagent Debate

Yilun Du Affiliation: MIT CSAIL Email: [yilundu@mit.edu](mailto:yilundu@mit.edu) Shuang Li Affiliation: MIT CSAIL Email: [lishuang@mit.edu](mailto:lishuang@mit.edu) Antonio Torralba Affiliation: MIT CSAIL Email: [torralba@mit.edu](mailto:torralba@mit.edu) Joshua B. Tenenbaum Affiliation: MIT CSAIL, BCS, CBMM Email: [jbt@mit.edu](mailto:jbt@mit.edu) Igor Mordatch Affiliation: Google Brain Email: [imordatch@google.com](mailto:imordatch@google.com) 

###### Abstract

Large language models (LLMs) have demonstrated remarkable capabilities in language generation, understanding, and few-shot learning in recent years. An extensive body of work has explored how their performance may be further improved through the tools of prompting, ranging from verification, self-consistency, or intermediate scratchpads. In this paper, we present a complementary approach to improve language responses where multiple language model instances propose and debate their individual responses and reasoning processes over multiple rounds to arrive at a common final answer. Our findings indicate that this approach significantly enhances mathematical and strategic reasoning across a number of tasks. We also demonstrate that our approach improves the factual validity of generated content, reducing fallacious answers and hallucinations that contemporary models are prone to. Our approach may be directly applied to existing black-box models and uses identical procedure and prompts for all tasks we investigate. Overall, our findings suggest that such "society of minds" approach has the potential to significantly advance the capabilities of LLMs and pave the way for further breakthroughs in language generation and understanding. Project website at [https://composable-models.github.io/llm_debate/](https://composable-models.github.io/llm_debate/).

## 1 Introduction

Large language models (LLMs) have demonstrated remarkable language generation, understanding, and few-shot learning capabilities in recent years. These methods are trained on a massive corpus of text on the internet, where the quality and accuracy of extracted natural language may not be ensured. Thus, current models may suffer from confidently hallucinating facts or making implausible jumps in chains of reasoning. An extensive body of recent work has focused on improving factual accuracy and reasoning in language models. These range from prompting models with few or zero-shot chain-of-thought demonstrations, use of verification, self-consistency, or intermediate scratchpads.

We note that these techniques are applied over a single model instance. Instead, we propose a complementary approach inspired by *The Society of Mind* [[19](#bib.bib19)] and multi-agent settings, where multiple language model instances (or agents) individually propose and jointly debate their responses and reasoning processes to arrive at a single common answer. More specifically, given a query, multiple instances of a language model first generate individual candidate answers to a query. Then each individual model instance reads and critiques the responses of all other models and uses this content to update its own answer. This step is then repeated over several rounds. This process induces models to construct answers that are consistent with both their internal critic as well as sensible in light of the responses of other agents. The resulting quorum of models can hold and maintain multiple chains of reasoning and possible answers simultaneously before proposing the final answer.

We find that our debate approach outperforms single model baselines such as zero-shot chain of thought [[11](#bib.bib11)] and reflection [[26](#bib.bib26), [18](#bib.bib18)] on a variety of six reasoning, factuality, and question-answering tasks. Using both multiple model agents and multiple rounds of debate are important to achieve the best performance. Given an initial query, we find that individual model instances propose a diverse range of answers despite being the same model class (although we also investigate the case of mixing different model types, such as chatGPT [[21](#bib.bib21)] and Bard [[23](#bib.bib23)]). After debating and examining the responses of other model instances, we find that the population almost always converges on a single and more accurate common answer. Debate results are also less likely to include false facts that models are internally uncertain of. This is because as the debate progresses, individual model instances tend to disagree on uncertain facts and omit them from the answer (Figure [7](#S3.F7)). Lastly, we find that debate does not just act to amplify one correct answer in a model quorum - we find many cases where all the models initially make incorrect predictions, but then arrive at the correct answer as debate progresses (Figure [4](#S3.F4),[11](#S3.F11)).

We use the same methodology and prompt templates for all our tasks and require only black-box access to language model generations – no model-internal information such as likelihoods or gradients is needed. This allows our method to be used with common public models serving interfaces. The method is also orthogonal to other model generation improvements such as retrieval or prompt engineering (in fact, we combine our debate method with zero-shot chain of thought). While the debate process is more costly, requiring multiple model instances and rounds, it arrives at significantly improved answers and may be used to generate additional model training data, effectively creating a model self-improvement loop.

To help evaluate the effect of our approach on factual accuracy, we introduce a new benchmark and dataset evaluating factual accuracy of famous computer scientist biographies. We find that contemporary language models have an especially high tendency to hallucinate factually incorrect biographies, often misrepresenting the relevant institutions and dates. Moreover, these facts often inconsistent across different language model instances. By asking models to come to a consensus across their answers, such inconsistent facts may be either removed or corrected.

In summary, our work contributes the following. First, we present a novel approach to improving factual correctness and reasoning accuracy in contemporary language models, leveraging a multi-agent debate process between models. Second, we introduce a new benchmark of factual correctness which contemporary language models struggle with. Finally, we evaluate the performance of our debate procedure in language generation, both in terms of the number of agents, the underlying rounds of debate, and the prompts that elicit such behavior across a set of six different reasoning and factual accuracy tasks.

Figure 1: Multiagent Debate Improves Reasoning and Factual Accuracy. Accuracy of traditional inference and our multi-agent debate over six benchmarks (chess move optimality reported as a normalized score) 

## 2 Language Generation through Multiagent Debate

We present an approach to generate language responses through multiagent debate. We provide an overview of our approach in Section [2.1](#S2.SS1). We further discuss convergence to consensus in the debate process in Section [2.2](#S2.SS2). The overall overview of our approach is shown in Figure [2](#S2.F2).

Figure 2: Illustration of Debate. Illustration of the debate procedure. 

### 2.1 Multiagent Language Generation

Consider your work process when solving the following math question on an exam: “What is the area of a triangle with side lengths of 3, 4, 5?". In one thread of work, you may recognize that the triangle side-lengths directly correspond to a right triangle, and thus directly compute the area as 0.5×3×4=640.5\times 3\times 4=64. To make sure that you have the right answer, you may then try to solve the problem differently by estimating an angle θ\theta in the triangle using the Law of Cosines, and then obtain the area by using the formula 0.5×3×4×sin⁡(θ)0.5\times 3\times 4\times\sin(\theta), arriving at another answer to the given exam problem.

When these lines of work give the same answer, your confidence about the answer increases. In contrast, when these answers are different, individual lines of work may engage in a mental “debate" procedure, where you closely cross-examine the reasoning and assumptions of each line of work and refine solutions until a consistent answer.

Similarly, consider writing a biography of a historical figure. To ensure the factuality of the biography, you may consult multiple different sources on each fact. Facts that are consistent in each source increase your confidence about the fact. In contrast, facts that are inconsistent require careful cross-examination between sources to determine the final consistent data.

To mimic the above multi-threaded reasoning process and multi-source factuality checking processes, we propose to generate answers subject to a multi-agent debate procedure between multiple instances of large language models. Given a question, multiple agents represented as copies of a large language model, generate answers to the question. Each response serves as a possible thought process or source of information which agents may re-examine to find consistent final answers.

After initial responses are generated from different agents, we initiate a round of debate between agents. Individual responses from other agents are concatenated and given as context to each agent, with each agent instructed to construct a new response based on such responses. Each language agent is thus responsible for both verifying the collection of responses given by other agents, and refining its own response based on other agents’ responses. We iteratively repeat this debate procedure over multiple rounds for improved performance.

Concretely, we first prompt each agent to independently solve the given problem or task. After each agent generates a response, we feed each agent a consensus prompt, illustrated in Figure [3](#S2.F3), where each agent is instructed to update their responses based on the responses of other agents. This resultant consensus prompt may then be repeatedly given, using the updated responses of each agent. We illustrate an overview of this multiagent debate procedure in Figure [2](#S2.F2).

Note that our proposed approach operates in an orthogonal manner to existing approaches to prompt language models. Given a question, we may apply additional techniques for prompting language models to further improve our debate procedure by eliciting additional more detailed responses from language models. We illustrate the synergy of our approach with existing approaches to prompting language models in Figure [6](#S3.F6) and directly apply zero-shot chain-of-thought reasoning in our evaluations.

Debate Length Prompt Short *" These are the solutions to the problem from other agents: [other answers]* *Based off the opinion of other agents, can you give an updated response …\ldots"* Long *" These are the solutions to the problem from other agents: [other answers]* *Using the opinion of other agents as additional advice, can you give an updated response …\ldots"*   
Figure 3: Prompts to induce long and short form debate. Responses of other agents to questions are are inserted in the middle of the prompt (indicated with *[other answers]*) 

### 2.2 Consensus in Debates

Given multiple rounds of debate, how can we ensure that a set of language model agents will converge to a final consensus answer? In general, debate can be seen as a multi-agent game, where convergence is not guaranteed. Empirically, however, we find that language models are able to converge on a single shared answer after multiple rounds of debate (Figure [4](#S3.F4)).

We found that we could control the duration of debates by how changing how much a language model trusts its own outputs over those generated by other models through different prompts. We illustrate two prompts below in Figure [3](#S2.F3), which we use to induce different debate durations between language models, and illustrate the effect of such prompts in Figure [12](#S3.F12). In general, we found that prompts that encouraged models to be more “stubborn’ based on their own solutions led to longer debates and better final solutions. Overall, we observed that language model agents were relatively "agreeable", perhaps as a result of instruction tuning or reinforcement learning based on human feedback [[22](#bib.bib22)].

## 3 Experiments

In our experiments, we evaluate our multiagent debate procedure and answer the following questions: (1) To what extent does multiagent debate improve reasoning? (2) To what extent does multiagent debate improve factual validity? (3) What design choices enable multiagent debate to improve language generation performance?

Figure 4: Illustration of Solving Math. Reasoning between agents is omitted. Figure 5: Illustration of Solving Grade School Math. Reasoning between agents omitted. Model Arithmetic (%) ↑\uparrow Grade School Math (%) ↑\uparrow Chess (Δ\DeltaPS) ↑\uparrow Single Agent 67.0 ±\pm 4.7 77.0 ±\pm 4.2 91.4 ±\pm 10.6 Single Agent (Reflection) 72.1 ±\pm 4.5 75.0 ±\pm 4.3 102.1 ±\pm 11.9 Multi-Agent (Majority) 69.0 ±\pm 4.6 81.0 ±\pm 3.9 102.2 ±\pm 6.2 Multi-Agent (Debate) 81.8 ±\pm 2.3 85.0 ±\pm 3.5 122.9 ±\pm 7.6 Table 1: Multiagent Debate Improves Reasoning Multi-agent debate improves the reasoning abilities of language models. Multi-agent results in the table are run with 3 agents and two rounds of debate. 

### 3.1 Improving Reasoning with Multiagent Debate

We first evaluate the extent to which multiagent debate improves the underlying reasoning process in language models.

#### Tasks.

We evaluate our approach on three reasoning tasks of increasing difficulty:

- • 

Arithmetic. We first evaluate the ability of models to correctly evaluate an arithmetic expression (containing addition, multiplication, and subtraction) consisting of six different two-digit numbers. For example: What is the result of 12+15*21+0-3*27?

- • 

GSM8K. Next, we consider harder mathematical reasoning tasks. Using the GSM8K dataset [[3](#bib.bib3)], the models must correctly solve grade school mathematical reasoning tasks.

- • 

Chess Move Prediction. Finally, we consider the strategic reasoning of the ability of models, and ask models to predict the best next move in a game of chess, given the first 14 moves of a chess game between two chess grand-masters described in PGN notation [[6](#bib.bib6)].

We report the accuracy of final answers in arithmetic and GSM8K tasks and report the pawn score (advantage) of predicted moves, as estimated by Stockfish in the Chess move prediction tasks. Additional details may be found in the Appendix.

Figure 6: Synergy with Other Methods. Performance of debate increases with use of Chain of Thought prompting. Figure 7: Illustration of Generating Biographies. Illustration of generating bullet biographies of computer scientists. For brevity, only the first 3 generated bullets are shown. Figure 8: Illustration of MMLU. Illustration of debate when answering factual tasks. Reasoning omitted. 

#### Baselines.

We compare our approach to three alternative approaches to generate responses for reasoning problems. First, we ask agents to directly generate responses (single agent). Next, we consider asking language models to generate and then "self-reflect" on the responses generated [[26](#bib.bib26), [18](#bib.bib18)]. Finally, we consider generating responses using multiple agents and performing majority voting [[15](#bib.bib15), [3](#bib.bib3)]. As the focus of our experiments is to verify the effectiveness of multiagent agent debate, we run both baselines and our approach, using the identical starting prompt and language model across all evaluations. We evaluate models in a zero-shot setting, with prompts found in the Appendix of the paper. We use chatGPT-based language model [[21](#bib.bib21)] in all our experiments except those in Figure [11](#S3.F11) where we compare multiple language models.

Due to computational expense, we evaluate our approach across benchmarks mainly using three agents with two rounds of debates, although we found further gains with both more agents and rounds of debate (Figure [10](#S3.F10)). Additional evaluation details are found in the Appendix.

#### Quantitative Results.

In Table [1](#S3.T1), we report the results of each approach on arithmetic, grade school math, and chess reasoning task. In each task, we observe that utilizing multiple different agents to generate solutions improves performance over using a single language model agent to generate a solution. Simultaneously, we also see that reflection, where a language model is asked to critique its early generation, generally gives a modest boost in performance. Multiagent debate, which may be seen as a combination of both reflection and multiagent generation, gives a substantial boost in reasoning across each of the tasks.

#### Qualitative Results.

In Figure [4](#S3.F4), [5](#S3.F5), we provide qualitative illustrations of the debate procedure between models. Interestingly, we find cases in which all models initially give an incorrect response, yet the result of debate still obtains the correct answer as agents critique each others’ reasoning. Thus, the purpose of our debate isn’t just to amplify a correct answer – all models can initially be wrong but arrive at the correct answer through the debate process.

#### Compatibility with other reasoning methods.

Our multiagent generation procedure operates orthogonally approach to other prompting methods which focus on single-agent generation. In Figure [6](#S3.F6), we illustrate the performance of multi-agent debate with and without zero-shot chain-of-thought prompting [[11](#bib.bib11)] on GSM8K. In both settings, multiagent generation is beneficial.

Model Biographies MMLU Chess Move Validity Single Agent 66.0 ±\pm 2.2 63.9 ±\pm 4.8 29.3 ±\pm 2.6 Single Agent (Reflection) 68.3 ±\pm 2.9 57.7 ±\pm 5.0 38.8 ±\pm 2.9 Multi-Agent (Debate) 73.8 ±\pm 2.3 71.1 ±\pm 4.6 45.2 ±\pm 2.9 Table 2: Multiagent Debate Improves Factual Accuracy Multi-agent debate improves the factual accuracy. Figure 9: Expressing Uncertainty with Multiple Answers. For facts that a language model is uncertain about, different language agents generate different facts. Debate causes agents to converge to one fact that is more accurate, but not necessarily always factually correct. Figure 10: (a) Performance with Increased Agents. Performance improves as the number of underlying agents involved in debate increases. (b) Performance with Increased Rounds. Performance rises as the number of rounds of underlying debate increases. 

### 3.2 Extracting Factual Information from Multiagent Debate

We next evaluate the extent to which multiagent debate improves the underlying factuality in language models.

#### Tasks.

We evaluate the factuality of language models in three different settings:

- • 

Biographies. To evaluate the factuality of language models, we introduce a novel task of accurately generating historical biographies of people. In preliminary testing, we found that existing language models had a tendency to hallucinate many facts on this task. We constructed ground truth bullet point biographies of 524 well-known computer scientists. We then asked language models to generate bullet point biographies for each person, and evaluated the accuracy at which each ground truth bullet point agreed with generated bullets. We report additional evaluation details in the Appendix.

- • 

MMLU. Next, we assess the factuality of language models in responding to different factual knowledge questions typically learned and assessed in different exams. We utilize the existing MMLU dataset [[8](#bib.bib8)] to benchmark the accuracy of responses.

- • 

Chess Move Validity. Lastly, we study the hallucinations in language models when planning under to the given rules of an existing environment or game. Specifically, we measure the validity of possible moves in a game of Chess given by BIG-Bench Chess-State Tracking Benchmark [[27](#bib.bib27)] task of chess-move prediction. In this task, an agent is given a set of next moves, and must make a valid next move of a piece on a board.

#### Baselines.

We use the same baselines as in Section [3.1](#S3.SS1). The multiagent (majority) is not directly applicable in this setting as individual responses are not easily comparable, and so we omit baseline comparison with the majority voting in this setting.

#### Results.

We analyze the performance of each method in Table [2](#S3.T2). We found that approaches based on reflection led to poor performance in the factuality setting. In contrast, debate gives the best performance in this setting also, and significantly outperforms each baseline. We illustrate a debate between agents on the biography task in Figure [7](#S3.F7) and on MMLU in Figure [8](#S3.F8). We found that multiagent debate improved and settled on bullets that were more consistent across agents.

We found that different language agents tended to give different answers when the underlying language model was uncertain about the question. However, directly asking each agent about their confidence [[10](#bib.bib10)] of the answer led to high confidence assessments on each answer. However, when these different language agents were asked to communicate with each other, each agent would quickly change their opinion to a consensus answer which was more accurate. We illustrate this in Figure [9](#S3.F9). Interestingly, we found that on facts that the language model was confident in (i.e. many instances of the same model all gave the same answer), it was very difficult to convince an agent to change their opinion, suggesting that “ease of persuasion” may be a method to assess factual confidence.

Figure 11: Debate Between chatGPT and Bard Illustration of debate between different models. 

### 3.3 Analysis: Understanding Multiagent Debate

Finally, we analyze how multiagent debate improves the underlying language generation procedure in language models.

#### Number of Agents.

First, we analyze the impact of agents number in debate. In Figure [10](#S3.F10)(a), we increase the number of agents used in debate, while fixing the debate length to be two. On arithmetic, performance monotonically increases with the increased number of agents. For larger number of agents, we first summarize all agent responses with chatGPT instead of directly concatenating responses due to context length error.

#### Rounds of Debate

Next, we analyze the impact of the number of rounds of debate in multiagent debate. In Figure [10](#S3.F10)(b), we increase the debate length between agents, while fixing the number of agents to three. We find that on the arithmetic task, the performance also monotonically increases with debate length. However, we found that additional debate rounds above four led to a similar final performance to 4 rounds of debate.

Figure 12: Performance vs Debate Length. Prompts which induce longer debate improve performance. 

#### Effect of Debate Length on Accuracy

As discussed in Section [2.2](#S2.SS2), the underlying convergence time in the debate between agents can be controlled by the extent to which agents are encouraged to maintain their opinions. In Figure [12](#S3.F12), we consider the effect of short and long-form prompts discussed in Figure [3](#S2.F3). We find that debates using longer prompts lead to slower convergence to correct answers, but also lead to a better final consensus on the correct answer. We provide an analysis of consensus between agents in Figure [14](#A1.F14).

#### Using Different Initialization Prompts

In our experiments we use the same prompts for all agents. We also consider the effect of using different questions, where we first instruct each language model to behave like a different persona (professor, doctor, mathematician) on the MMLU dataset. We found that improved performance on MMLU from 71.1 to 74.2 with different agents, suggesting further gains can be obtained with different initialization prompts.

Figure 13: Effect of Summarization. When there are many agents in a debate, responses from other agents may be first summarized and then given as context, reducing context length. This operation improves performance. 

#### Summarization.

While in the majority of experiments in the paper we directly concatenate the responses of other agents as context for an agent to generate a new response, this is expensive when the number of agents involved in debate gets large. We may alternatively first summarize the responses from all other agents into a single response that we provide to agent at each round for more efficient debate. We apply this strategy in Figure [10](#S3.F10) to enable the use of five or more agents in debate. In Figure [13](#S3.F13), we analyze the effect compared to directly concatenating the responses of other agents. We find this improves the performance of debate, suggesting that summarization is another tool that can further improve multiagent debate.

#### Utilizing Different Language Models

Our existing debate results are reported using multiple instances of a chatGPT language model. We further assess the impact of using two different language models, where we ask chatGPT and Bard [[23](#bib.bib23)] language models to debate with each other on a set of 20 GSM8K math problems. In this set, we find that multi-agent debate improves the performance of both agents, with Bard solving 11 problems, chatGPT solving 14 problems, and joint multi-agent debate solving 17 problems. We qualitatively illustrate a debate between agents in Figure [11](#S3.F11). While both agents initially provide incorrect answers to the problem, chatGPT is able to utilize the incorrect response given by Bard to generate the final correct answer.

## 4 Related Work

#### Reasoning and Factuality in Language Models.

A wide range of work has explored how to enable reasoning and factuality in language models. To improve reasoning, approaches have relied on prompting techniques such as scratchpads [[20](#bib.bib20)], verification [[3](#bib.bib3)], chain-of-thought demonstrations [[30](#bib.bib30), [11](#bib.bib11), [25](#bib.bib25)], and intermediate self-reflection [[26](#bib.bib26), [18](#bib.bib18)] and finetuning [[13](#bib.bib13), [24](#bib.bib24), [31](#bib.bib31)]. To improve factuality, approaches have relied on training techniques such as RLHF [[33](#bib.bib33), [16](#bib.bib16), [2](#bib.bib2)], pruning truthful datasets [[12](#bib.bib12)], external knowledge retrieval [[7](#bib.bib7)] and training-free methods based off likelihood estimation [[10](#bib.bib10)].

Our work provides an alternative way to obtain reasoning and factuality in language models using multiagent debates, which only requires black-box access to a language generator. Prior work also has explored how to take the majority vote across different models [[15](#bib.bib15), [3](#bib.bib3), [29](#bib.bib29), [28](#bib.bib28)] while in this work, we use the power of a language model to combine different answers. Most similar to our work, [Irving et al. 2018](#bib.bib9) also proposes a debate procedure to verify the accuracy and safety of powerful AI agents. In contrast to our approach, in their work, agents are asked to alternatively provide proof of a input, and humans are tasked with assessing these debates and determining safety.

#### Compositional Generation.

Our work is also related to existing works that focus on text generation by combining different models [[4](#bib.bib4), [17](#bib.bib17), [32](#bib.bib32), [1](#bib.bib1), [5](#bib.bib5)]. Most similar to our work, [[14](#bib.bib14), [32](#bib.bib32)] propose to combine multiple different large pretrained models together for multimodal reasoning. In contrast, in our work, we aim to use communication between different language models to enable more effective reasoning and factuality in language models.

## 5 Limitations and Discussion

In this paper, we present an orthogonal approach to improve the performance of language models using multi-agent debate. We find that the approach is simple and effective across a wide set of different reasoning and validity language modeling tasks.

#### Limitations.

In comparison to other prompting techniques, our multiagent debate procedure is more computationally expensive, as it requires both multiple language generations, and an underlying debate procedure. However, we believe that this approach may be seen as a method to generate additional data that may be distilled back to self-improve the original base model.

Further, we observed that as debates became longer in duration, current language models sometimes struggled to fully process the entire debate input, and typically only focused on the most recent generations. We believe that this performance will be alleviated with longer-context and improved language models or by summarizing early portions of the debate.

Finally, we found that while debates typically converged into single final answers, these answers were not necessarily correct. Despite answers being incorrect, language models would confidently affirm that their answer is correct and consistent with all other agent responses. We believe this result is in part due to the fact that LMs do not correctly express their uncertainty when generating responses, and believe that other orthogonal approaches to improve this performance would improve the results of multiagent debate.

## References

- Alayrac et al. [2022]  J.-B. Alayrac, J. Donahue, P. Luc, A. Miech, I. Barr, Y. Hasson, K. Lenc, A. Mensch, K. Millican, M. Reynolds, et al. Flamingo: A visual language model for few-shot learning. *NeurIPS*, 2022. URL [https://arxiv.org/abs/2204.14198](https://arxiv.org/abs/2204.14198). 
- Christiano et al. [2017]  P. F. Christiano, J. Leike, T. Brown, M. Martic, S. Legg, and D. Amodei. Deep reinforcement learning from human preferences. In *Neural Information Processing Systems*, 2017. 
- Cobbe et al. [2021]  K. Cobbe, V. Kosaraju, M. Bavarian, M. Chen, H. Jun, L. Kaiser, M. Plappert, J. Tworek, J. Hilton, R. Nakano, et al. Training verifiers to solve math word problems. *arXiv preprint arXiv:2110.14168*, 2021. 
- Du et al. [2020]  Y. Du, S. Li, and I. Mordatch. Compositional visual generation with energy based models. In *Advances in Neural Information Processing Systems*, 2020. 
- Du et al. [2023]  Y. Du, C. Durkan, R. Strudel, J. B. Tenenbaum, S. Dieleman, R. Fergus, J. Sohl-Dickstein, A. Doucet, and W. Grathwohl. Reduce, reuse, recycle: Compositional generation with energy-based diffusion models and mcmc. *arXiv preprint arXiv:2302.11552*, 2023. 
- [6]  Fsmosca. Fsmosca/pgn-standard: Portable game notation specification and implementation guide. URL [https://github.com/fsmosca/PGN-Standard](https://github.com/fsmosca/PGN-Standard). 
- Guu et al. [2020]  K. Guu, K. Lee, Z. Tung, P. Pasupat, and M.-W. Chang. REALM: Retrieval-augmented language model pre-training. *arXiv preprint arXiv:2002.08909*, 2020. 
- Hendrycks et al. [2020]  D. Hendrycks, C. Burns, S. Basart, A. Zou, M. Mazeika, D. Song, and J. Steinhardt. Measuring massive multitask language understanding. *arXiv preprint arXiv:2009.03300*, 2020. 
- Irving et al. [2018]  G. Irving, P. Christiano, and D. Amodei. Ai safety via debate. *arXiv preprint arXiv:1805.00899*, 2018. 
- Kadavath et al. [2022]  S. Kadavath, T. Conerly, A. Askell, T. Henighan, D. Drain, E. Perez, N. Schiefer, Z. H. Dodds, N. DasSarma, E. Tran-Johnson, et al. Language models (mostly) know what they know. *arXiv preprint arXiv:2207.05221*, 2022. 
- Kojima et al. [2022]  T. Kojima, S. S. Gu, M. Reid, Y. Matsuo, and Y. Iwasawa. Large language models are zero-shot reasoners. *arXiv preprint arXiv:2205.11916*, 2022. 
- Lee et al. [2022]  N. Lee, W. Ping, P. Xu, M. Patwary, P. N. Fung, M. Shoeybi, and B. Catanzaro. Factuality enhanced language models for open-ended text generation. *Advances in Neural Information Processing Systems*, 35:34586–34599, 2022. 
- Lewkowycz et al. [2022]  A. Lewkowycz, A. Andreassen, D. Dohan, E. Dyer, H. Michalewski, V. Ramasesh, A. Slone, C. Anil, I. Schlag, T. Gutman-Solo, et al. Solving quantitative reasoning problems with language models. *arXiv preprint arXiv:2206.14858*, 2022. 
- Li et al. [2022a]  S. Li, Y. Du, J. B. Tenenbaum, A. Torralba, and I. Mordatch. Composing ensembles of pre-trained models via iterative consensus. *arXiv preprint arXiv:2210.11522*, 2022a. 
- Li et al. [2022b]  Y. Li, D. Choi, J. Chung, N. Kushman, J. Schrittwieser, R. Leblond, T. Eccles, J. Keeling, F. Gimeno, A. Dal Lago, et al. Competition-level code generation with alphacode. *Science*, 378(6624):1092–1097, 2022b. 
- Liu et al. [2022a]  H. Liu, L. Lee, K. Lee, and P. Abbeel. Instruction-following agents with jointly pre-trained vision-language models. *arXiv preprint arXiv:2210.13431*, 2022a. 
- Liu et al. [2022b]  N. Liu, S. Li, Y. Du, A. Torralba, and J. B. Tenenbaum. Compositional visual generation with composable diffusion models. *arXiv preprint arXiv:2206.01714*, 2022b. 
- Madaan et al. [2023]  A. Madaan, N. Tandon, P. Gupta, S. Hallinan, L. Gao, S. Wiegreffe, U. Alon, N. Dziri, S. Prabhumoye, Y. Yang, et al. Self-refine: Iterative refinement with self-feedback. *arXiv preprint arXiv:2303.17651*, 2023. 
- Minsky [1988]  M. Minsky. *Society of mind*. Simon and Schuster, 1988. 
- Nye et al. [2021]  M. Nye, A. J. Andreassen, G. Gur-Ari, H. Michalewski, J. Austin, D. Bieber, D. Dohan, A. Lewkowycz, M. Bosma, D. Luan, et al. Show your work: Scratchpads for intermediate computation with language models. *arXiv preprint arXiv:2112.00114*, 2021. 
- OpenAI [2022]  OpenAI. Chatgpt: Optimizing language models for dialogue, Dec 2022. URL [https://openai.com/blog/chatgpt/](https://openai.com/blog/chatgpt/). 
- Ouyang et al. [2022]  L. Ouyang, J. Wu, X. Jiang, D. Almeida, C. L. Wainwright, P. Mishkin, C. Zhang, S. Agarwal, K. Slama, A. Ray, et al. Training language models to follow instructions with human feedback. *arXiv preprint arXiv:2203.02155*, 2022. 
- Pichai [2023]  S. Pichai. An important next step on our ai journey, Feb 2023. URL [https://blog.google/technology/ai/bard-google-ai-search-updates/](https://blog.google/technology/ai/bard-google-ai-search-updates/). 
- Rajani et al. [2019]  N. F. Rajani, B. McCann, C. Xiong, and R. Socher. Explain yourself! leveraging language models for commonsense reasoning. *arXiv preprint arXiv:1906.02361*, 2019. 
- Reynolds and McDonell [2021]  L. Reynolds and K. McDonell. Prompt programming for large language models: Beyond the few-shot paradigm. In *Extended Abstracts of the 2021 CHI Conference on Human Factors in Computing Systems*, pages 1–7, 2021. 
- Shinn et al. [2023]  N. Shinn, B. Labash, and A. Gopinath. Reflexion: an autonomous agent with dynamic memory and self-reflection. *arXiv preprint arXiv:2303.11366*, 2023. 
- Srivastava et al. [2022]  A. Srivastava, A. Rastogi, A. Rao, A. A. M. Shoeb, A. Abid, A. Fisch, A. R. Brown, A. Santoro, A. Gupta, A. Garriga-Alonso, et al. Beyond the imitation game: Quantifying and extrapolating the capabilities of language models. *arXiv preprint arXiv:2206.04615*, 2022. 
- Thoppilan et al. [2022]  R. Thoppilan, D. De Freitas, J. Hall, N. Shazeer, A. Kulshreshtha, H.-T. Cheng, A. Jin, T. Bos, L. Baker, Y. Du, et al. Lamda: Language models for dialog applications. *arXiv preprint arXiv:2201.08239*, 2022. 
- Wang et al. [2022]  X. Wang, J. Wei, D. Schuurmans, Q. Le, E. Chi, and D. Zhou. Self-consistency improves chain of thought reasoning in language models. *arXiv preprint arXiv:2203.11171*, 2022. 
- Wei et al. [2022]  J. Wei, X. Wang, D. Schuurmans, M. Bosma, E. Chi, Q. Le, and D. Zhou. Chain of thought prompting elicits reasoning in large language models. *arXiv preprint arXiv:2201.11903*, 2022. 
- Zelikman et al. [2022]  E. Zelikman, Y. Wu, J. Mu, and N. Goodman. Star: Bootstrapping reasoning with reasoning. *Advances in Neural Information Processing Systems*, 35:15476–15488, 2022. 
- Zeng et al. [2022]  A. Zeng, A. Wong, S. Welker, K. Choromanski, F. Tombari, A. Purohit, M. Ryoo, V. Sindhwani, J. Lee, V. Vanhoucke, et al. Socratic models: Composing zero-shot multimodal reasoning with language. *arXiv preprint arXiv:2204.00598*, 2022. URL [https://arxiv.org/abs/2204.00598](https://arxiv.org/abs/2204.00598). 
- Ziegler et al. [2019]  D. M. Ziegler, N. Stiennon, J. Wu, T. B. Brown, A. Radford, D. Amodei, P. Christiano, and G. Irving. Fine-tuning language models from human preferences. *arXiv preprint arXiv:1909.08593*, 2019. 

## Appendix A Appendix

In this appendix, we provide additional analysis and visualizations of the debates used in the main paper in Section [A.1](#A1.SS1). We further provide detailed experimental details on each dataset in Section [A.2](#A1.SS2).

### A.1 Additional Results

Figure 14: Effect of Prompts on Consensus. Using a short debate prompt induces faster consensus between agents 

#### Consensus Between Agents.

In Figure [14](#A1.F14), we illustrate the consensus between agents using either short or long consensus prompts discussed in Figure [3](#S2.F3). The use of debate prompts that encourage agents to adapt more to the opinions of other agents improves consensus.

#### Additional Qualitative Visualizations.

We added additional qualitative visualizations of the debate process. In Figure [16](#A1.F16), Figure [17](#A1.F17), Figure [18](#A1.F18), Figure [19](#A1.F19), Figure [20](#A1.F20), we illustrate debates between agents in the GSM8K dataset which result in the correct answer. In Figure [21](#A1.F21), Figure [22](#A1.F22), Figure [23](#A1.F23), we further illustrate debates in GSM8K which lead to the incorrect answer. We further provide an example illustration of debate in arithmetic in Figure [24](#A1.F24), arithmetic with summarization of individual responses of agents in Figure [25](#A1.F25), MMLU in Figure [26](#A1.F26), a debate with the full contents biographies in Figure [27](#A1.F27), and debate in chess in Figure [28](#A1.F28). In general, we found that debate improved the performance of final generated answers, though sometimes answers would converge to the incorrect value.

### A.2 Evaluation Details

We provided detailed evaluation details for each setting in the paper. We run all experiments using the gpt-3.5-turbo-0301 model. We provide a table listing the prompts used to prompt models and initialize debate in Table [15](#A1.F15).

#### Arithmetic.

To evaluate the arithmetic task, we generated six random integers for each task between 0 and 30. We then evaluated the extent to which the correct integer answer was correctly obtained. We evaluated models on one hundred generated arithmetic tasks.

#### Grade School Math.

To evaluate the GSM8K task, we evaluated the accuracy at which models were able to obtain the final correct answer, as extracted from a box. We evaluated models on one hundred grade school math problems.

#### Chess.

To evaluate the chess reasoning task, we used chess games from [https://www.pgnmentor.com/players/Adams.zip](https://www.pgnmentor.com/players/Adams.zip). We asked chatGPT to predict the next move for white to move at turn 14 and reported the relative Stockfish pawn score with search depth 20 after executing the suggested move from chatGPT. We evaluated models on three hundred selected chess games.

#### Biographies.

To evaluate the biographies task, we compare each generated bullet point biography for a person with a ground truth set of facts about the person extracted from Wikipedia. We iteratively loop through each ground truth fact, and validate the extent to which the generated biography matches a particular bullet by prompting chatGPT with the prompt: *Consider the following biography of <person>: <generated biography> Is the above biography above consistent with the fact below? <ground truth bullet> Give a single-word answer, yes, no, or uncertain.* We then evaluate and report the percentage of ground bullets that chatGPT returns either yes or no on. We ignored ground truth bullets that chatGPT returns returned uncertain.

We found this evaluation metric provided a fast way to evaluate how relatively correct a generated bullet point biography is. However, we found that generated facts could contain incorrect information that was not captured in the ground truth bullet and thus could not be validated through this metric. Nevertheless, we believe this evaluation scheme estimates the relative accuracy of a generated biography.

#### MMLU.

To evaluate MMLU, we measured the accuracy in which models were able to select the correct multiple-choice answer in each problem. We evaluated models on one hundred selected MMLU questions randomly distributed across each of the subject areas.

#### Chess Validity.

To evaluate chess validity, we consider the BIG-Bench Chess-State Tracking Benchmark [[27](#bib.bib27)], where we used the hardest reported task in the benchmark synthetic_short. Each generated answer was deemed correct as long as it was one of the valid answers in the sequence. We evaluated models of one hundred selected chess validity tasks.

Task Type Prompt Arithmetic Starting *What is the result of {}+{}*{}+{}-{}*{}? Make sure to state your answer at the end of the response.* Debate *These are the recent/updated opinions from other agents: <other agent responses> Use these opinions* *carefully as additional advice, can you provide an updated answer? Make sure to state your answer* *at the end of the response.* GSM8K Starting *Can you solve the following math problem? <Problem> Explain your reasoning. Your final answer* *should be a single numerical number, in the form \boxed{{answer}}, at the end of your response.* Debate *These are the solutions to the problem from other agents: <other agent responses> Using the solutions* *from other agents as additional information, can you provide your answer to the math problem? The original* *math problem is <Problem>. Your final answer should be a single numerical number, in the form* *\boxed{{answer}}, at the end of your response.* Chess Starting *Here is the current sequence of moves in a chess game: <moves>. What is the best chess move I should* *execute next? Give a single move suggestion of the form 14. <XXX> and make sure the chess move* *is valid in the current board state.* Debate *Here are other chess move suggestions from other agents: <other agent responses> Using the chess suggestions* *from other agents as additional advice and your earlier generated solution, can you give me your updated thoughts* *on the best next chess move I should play given the chess sequence ? Give a single move suggestion of the form* *14. <XXX> and make sure the chess move is valid in the current board state.* Biographies Starting *Give a bullet point biography of highlighting their contributions and achievements as a computer scientist,* *with each fact separated with a new line character.* Debate *Here are some bullet point biographies of <person> given by other agents: <other agent response> Closely* *examine your biography and the biography of other agents and provide an updated bullet point biography.* MMLU Starting *Can you answer the following question as accurately as possible? : A) , B) , C) , D) Explain your answer,* *putting the answer in the form (X) at the end of your response.* Debate *These are the solutions to the problem from other agents: <other agent responses> Using the reasoning* *from other agents as additional advice, can you give an updated answer? Examine your solution and* *that other agents. Put your answer in the form (X) at the end of your response.* Chess Validity Starting *Given the chess game , give one valid destination square for the chess piece at . State the destination square* *in the form (X), where X follows the regex [a-h][1-8], for example (e5). Give a one line explanation* *of why your destination square is a valid move.* Debate *Here are destination square suggestions from other agents: <other agent responses> Can you double* *check that your destination square is a valid move? Check the valid move justifications from other agents.* *State your final answer in a newline with a 2 letter response following the regex [a-h][1-8].*   
Figure 15: Prompts in each task. List of prompts used in each task Figure 16: Example of a correct GSM8K Debate. Figure 17: Example of Correct GSM8K Debate. Figure 18: Example of Correct GSM8K Debate. Figure 19: Example of Correct GSM8K Debate. Figure 20: Example of Correct GSM8K Debate. Figure 21: Example of Incorrect GSM8K Debate. Figure 22: Example of Incorrect GSM8K Debate. Figure 23: Example of Incorrect GSM8K Debate. Figure 24: Example of Arithmetic Debate. Figure 25: Example of Arithmetic Debate with Summarization. Four separate agents participate in debate, with two illustrated above. Instruction contains the summarized responses across agents. Figure 26: Example of MMLU Debate. Figure 27: Example of Biography Debate. While we found that generated biographies after debate to be more accurate, many facts remain incorrect. Figure 28: Example of Chess Debate. [◄](/html/2305.14324) ![ar5iv homepage](/assets/ar5iv.png)</>   
[Feelinglucky?](/feeling_lucky) </land_of_honey_and_milk>   
[Conversionreport](/log/2305.14325)   
[Reportan issue](https://github.com/dginev/ar5iv/issues/new?template=improve-article--arxiv-id-.md&title=Improve+article+2305.14325)   
[View originalon arXiv](https://arxiv.org/abs/2305.14325)[►](/html/2305.14326)
