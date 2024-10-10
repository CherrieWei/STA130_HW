#!/usr/bin/env python
# coding: utf-8

# # STA130 Homework 05 
# 
# Please see the course [wiki-textbook](https://github.com/pointOfive/stat130chat130/wiki) for the list of topics covered in this homework assignment, and a list of topics that might appear during ChatBot conversations which are "out of scope" for the purposes of this homework assignment (and hence can be safely ignored if encountered)

# <details class="details-example"><summary style="color:blue"><u>Introduction</u></summary>
# 
# ### Introduction
#     
# A reasonable characterization of STA130 Homework is that it simply defines a weekly reading comprehension assignment. 
# Indeed, STA130 Homework essentially boils down to completing various understanding confirmation exercises oriented around coding and writing tasks.
# However, rather than reading a textbook, STA130 Homework is based on ChatBots so students can interactively follow up to clarify questions or confusion that they may still have regarding learning objective assignments.
# 
# > Communication is a fundamental skill underlying statistics and data science, so STA130 Homework based on ChatBots helps practice effective two-way communication as part of a "realistic" dialogue activity supporting underlying conceptual understanding building. 
# 
# It will likely become increasingly tempting to rely on ChatBots to "do the work for you". But when you find yourself frustrated with a ChatBots inability to give you the results you're looking for, this is a "hint" that you've become overreliant on the ChatBots. Your objective should not be to have ChatBots "do the work for you", but to use ChatBots to help you build your understanding so you can efficiently leverage ChatBots (and other resources) to help you work more efficiently.<br><br>
# 
# </details>
# 
# <details class="details-example"><summary style="color:blue"><u>Instructions</u></summary>
# 
# ### Instructions
#     
# 1. Code and write all your answers (for both the "Pre-lecture" and "Post-lecture" HW) in a python notebook (in code and markdown cells) 
#     
# > It is *suggested but not mandatory* that you complete the "Pre-lecture" HW prior to the Monday LEC since (a) all HW is due at the same time; but, (b) completing some of the HW early will mean better readiness for LEC and less of a "procrastentation cruch" towards the end of the week...
#     
# 2. Paste summaries of your ChatBot sessions (including link(s) to chat log histories if you're using ChatGPT) within your notebook
#     
# > Create summaries of your ChatBot sessions by using concluding prompts such as "Please provide a summary of our exchanges here so I can submit them as a record of our interactions as part of a homework assignment" or, "Please provide me with the final working verson of the code that we created together"
#     
# 3. Save your python jupyter notebook in your own account and "repo" on [github.com](github.com) and submit a link to that notebook though Quercus for assignment marking<br><br>
# 
# </details>
# 
# <details class="details-example"><summary style="color:blue"><u>Prompt Engineering?</u></summary>
#     
# ### Prompt Engineering? 
#     
# The questions (as copy-pasted prompts) are designed to initialize appropriate ChatBot conversations which can be explored in the manner of an interactive and dynamic textbook; but, it is nonetheless **strongly recommendated** that your rephrase the questions in a way that you find natural to ensure a clear understanding of the question. Given sensible prompts the represent a question well, the two primary challenges observed to arise from ChatBots are 
# 
# 1. conversations going beyond the intended scope of the material addressed by the question; and, 
# 2. unrecoverable confusion as a result of sequential layers logial inquiry that cannot be resolved. 
# 
# In the case of the former (1), adding constraints specifying the limits of considerations of interest tends to be helpful; whereas, the latter (2) is often the result of initial prompting that leads to poor developments in navigating the material, which are likely just best resolve by a "hard reset" with a new initial approach to prompting.  Indeed, this is exactly the behavior [hardcoded into copilot](https://answers.microsoft.com/en-us/bing/forum/all/is-this-even-normal/0b6dcab3-7d6c-4373-8efe-d74158af3c00)...
# 
# </details>

# ### Marking Rubric (which may award partial credit) 
# 
# - [0.1 points]: All relevant ChatBot summaries [including link(s) to chat log histories if you're using ChatGPT] are reported within the notebook
# - [0.3 points]: Evaluation of written communication for "Question 2"
# - [0.3 points]: Evaluation of written communication for "Question 4"
# - [0.3 points]: Evalution of submission for "Question 8"
# 

# ## "Pre-lecture" HW [*completion prior to next LEC is suggested but not mandatory*]

# ### A. Watch this first pre-lecture video ("Hypothesis testing. Null vs alternative") addressing the question "What is a hypothesis?"<br>
# 
# <details class="details-example"><summary style="color:blue"><u>Further Guidance</u></summary>
#     
# > _The video gives the example that the "Hillary versus Trump" U.S. presidential election campaign could not be turned into a hypothesis test assessing differences in performance between the two as U.S. presidents (because at the time of the election neither had been U.S. presidents). This is different than addressing "Obama versus Bush" within a hypothesis testing framework (because we have eight years worth of performance of both as U.S. presidents). A more contemporarily relevant comparison then would be the aborted election campaign efforts of "Biden versus Trump", which would have been a chimeric hybrid of the two comparisons mentioned above (because we have BOTH four years worth of DATA regarding the performance of both as U.S. presidents BUT we are also likely still [...or, were, prior to Biden dropping out of the presidential race...] interested in asking questions regarding their potential FUTURE performance of both as U.S. presidents for which we do not yet have any data). Anway, despite Biden dropping out of the election, we might still attempt to consider the record of the Biden presidency to be informative and predictive about the furture peformance of a potential Kamala Harris presidency._
# > 
# > _This hopefully (a) makes the examples of the video more contemporarily relevant, and (b) gives another example to further emphasize and contrast the distinction that's being made in the video._
# >
# > _Also, while these are relatively knit-picky, two technical issues that the video somewhat inaccurately introduces are:_
# >
# > - _the video states that "we accept the null hypothesis"; but, actually it would be more correct to say, "we fail to reject the null hypothesis"_
# > - _the video specifies "less than" for the null hypothesis and "less than or equal" for the alternative hypothesis; but, actually, for mathematic reasons "less than or equal" version is the more technically correct choice for how the null hypothesis should be specified_
#     
# </details>

# In[1]:


from IPython.display import YouTubeVideo
# First pre-lecture video: 
# "Hypothesis testing. Null vs alternative
# https://www.youtube.com/watch?v=ZzeXCKd5a18
YouTubeVideo('ZzeXCKd5a18', width=800, height=500)


# ### B. Watch this second pre-lecture video ("What is a p-value") providing an intuitivie introduction to p-values <br>
# 
# <details class="details-example"><summary style="color:blue"><u>Further Guidance</u></summary>
#     
# > _This is intended to help you initially make more sense of the technical definition of a p-value, **the probability that a test statistic is as or more extreme than the observed test statistic if the null hypothesis was true**._
# >
# > _The thing is though, once you understand a p-value is, then you'll see how simple and elegant the above definition is... So, your objective in learning what a p-value is should be to be able to read and understand the definition of a p-value given above effortlessly... That way you can communicate with the language of statistical reasoning in 3.5 seconds rather than 3.5 minutes..._
#     
# </details>

# In[1]:


from IPython.display import YouTubeVideo
# Second pre-lecture video
# "What is a p-value"
# https://www.youtube.com/watch?v=9jW9G8MO4PQ
YouTubeVideo('9jW9G8MO4PQ', width=800, height=500)


# ### 1. The "first pre-lecture video" (above) describes hypothesis testing as addressing "an idea that can be tested", and the end of the video then discusses what our actual intended purpose in setting up a null hypothesis is. What is the key factor that makes the difference between ideas that can, and cannot be examined and tested statistically?  What would you describe is the key "criteria" defining what a good null hypothesis is? And what is the difference between a null hypothesis and an alternative hypothesis in the context of hypothesis testing? Answer these questions with concise explanations in your own words.<br>
# 
# <details class="details-example"><summary style="color:blue"><u>Further Guidance</u></summary>
# 
# > _After watching and understanding both of the videos above, you should be well equipped to answer this and the following few questions. But, you can also interact with your favourite ChatBot to see if you understand the concepts correctly and to clarify any open questions you might have about anything that still seems unclear._
# >
# > HOWEVER, as we increasingly tread into the more conceptual statistical concepts of STA130, "vanilla" ChatBots become less and less reilable.
# > 1. First, "vanilla" ChatBots don't know the constraints and scope of the learning objectives of STA130, so in addition to their often verbose nature, they now present the possible risk of tangenting onto topics that do not concern (but may nonetheless potentially confuse and distract) us
# > 2. Second, ChatBots are based on textual information online, and while much of this information is accurate and well articulated, there is also a not insignificant presense of confusion and misunderstanding of statistical concepts and topics online. The downside of this is that since ChatBots don't "reasons" but instead just actually "regurgitate" the freqently occuring patterns between words found in text, it's increasingly possible that responses ChatBots will in fact amount to only meaningless gibberish nonensense.
# >
# > **Therefore, it is recommended that students begin considering and exploring increasingly relying on the STA130 Custom NotebookLM (NBLM) ChatBot** rather than "vanilla" ChatBots when it comes to the specific and technical and conceptual statistical topics of STA130.**
# >
# > _Don't forget to ask for summaries of your ChatBot session(s) and paste these into your homework notebook (including link(s) to chat log histories if you're using ChatGPT) if you are using a ChatBot interaction to help learn and understand something!_
# >
# > In the case of the custom NBLM ChatBot, you can't get a transcript of your conversation, unfortunately (since converational history records outside of an active NBLM ChatBot session are made available to you in the future...); but, that's perfectly fine regarding the requirement of the homework which is only that a summary of any ChatBot interactions is provided with the submission. 
# 
# </details>
# 

# The key factor that makes the difference between ideas that can and cannot be tested statistically is whether there is a value that can be compared. Ideas that are not measurable cannot be tested using statistics. 
# I think the key criteria defining a good null hypothesis are:
# 1) It should be the default value or state of the thing being tested
# 2) It should be reasonable
# 3) It should be something that can be measured or tested mathematically / statistically
# The difference between a null and an alternative hypothesis is that the null hypothesis is what we are trying to test or prove, while the alternate hypothesis is anything that is not the null hypothesis.

# ### 2. Towards the end of the "first pre-lecture" video (above) it is stated that, "It is important to note that outcomes of tests refer to the population parameter, rather than the sample statistic! As such, the result that we get is for the population." In terms of the distinctions between the concepts of $x_i\!$'s, $\bar x$, $\mu$, and $\mu_0$, how would you describe what the sentence above means? Explain this concisely in your own words for a "non-statsitical" audience, defining the technical statistical terminology you use in your answer.<br>
# 
# <details class="details-example"><summary style="color:blue"><u>Further Guidance</u></summary>
# 
# > _A formal **null hypothesis** has the form $H_0: \mu=\mu_0$ which states that the average value $\mu$ of the population is $\mu_0$, while the **alternative hypothesis** would then be $H_A: H_0 \text{ is false}$ which states the average value $\mu$ of the population is not $\mu_0$. This question asks for a clear explanation of the distinguishing characteristics of the between the concepts of observed sample values $x_i$ (for $i = 1, \cdots, n$), the observed sample average $\bar x$, the actual value of $\mu$, and the value $\mu_0$ hypothesized under the null hypothesis relative to hypothesis testing._   
# > 
# > _This question extends "Question 7" from the Week 4 HW that you considered last week in a more formal manner in terms of hypothesis testing notation. It should be getting much easier to delineate the differences between parameters and populations, and samples and statistics; and, to understand how to interpret and apply these concepts in the context of new topics (such as hypothesis testing, as is done here)._ 
# > 
# > _As continually suggested and encouraged regarding the topics of parameters, populations, samples, and statistics, check with your notes or your favourite ChatBot to make sure you have a clear understanding of these terms. At this point in the course, you should be able to read and understand of the meaning of the termenologically dense sentence addressed in the prompt to this question!_ 
# >
# > Don't forget to ask for summaries of your ChatBot session(s) if you are using a ChatBot interaction to help learn and understand something! You only need to include link(s) to chat log histories if you're using ChatGPT, e.g., if you're using the custom STA130 NBLM ChatBot you can't get chat history logs, but you can get summaries, so just paste these into your homework notebook and indicate the both you're using if it can't provide links to chat log histories.
#     
#     
# 
# </details>
# 

# It means that the conclusion drawn from the hypothesis tests should apply to the population, which is the target group of individuals that we are interested in investigating and want to generalize the conclusion to. The data we obtain from a sample is only part of the population, and we assume it is representative of the population. In a hypothesis test, we are using the symbol μ to represent the parameters, and μ is referring to the population rather than the sample. Therefore, it is important to know that even though we are using sample statistics to test our hypothesis, the conclusion should be generalized to the population because it is what we are aiming to investigate.

# ### 3. The second "Pre-lecture" video (above) explains that we "imagine a world where the null hypothesis is true" when calculating a p-value? Explain why this is in your own words in a way that makes the most sense to you.<br>
# 
# <details class="details-example"><summary style="color:blue"><u>Further Guidance</u></summary>
# 
# > _Hint: your answer will likely be most efficiently correct and clear if it discusses the relavence of the sampling distribution of the test statistic under the null hypothesis._
#     
# </details>

# The video is explaining that when we are calculating a p-value, we would want to know how probable our data points would lie on different certain values. In other words, we want to test how probable the null hypothesis is true under all of the probable outcomes that we can get. By calculating how our sample data is distributed, we can then test how likely it is for the data to lie within the range of our null hypothesis. 

# ### 4. The second "Pre-lecture" video (above) describes suggest that a smaller p-value makes the null hypothesis look more ridiculous. Explain why this is in your own words in a way that makes the most sense to you, clarifying the meaning of any technical statistical terminology you use in your answer.<br>
# 
# <details class="details-example"><summary style="color:blue"><u>Further Guidance</u></summary>
# 
# > _Hint: your answer will likely be most efficiently correct and clear if it discusses how the observed test statistic relates to the sampling distribution of the test statistic under the null hypothesis._
#     
# </details> 

# When performing a hypothesis test, the sampling distribution of the test statistic is based on the assumption that the null hypothesis is true. Because we assume random sample, the distribution shows the range of possible values that the test statistic can have if the null hypothesis is true. A small p-value means that it is not very probable for the null hypothesis to be true. The lower the p-value, the lower the probability, and therefore the more ridiculous the null hypothesis would look. 

# ### 5. Güntürkün (2003) recorded how kissing couples tilt their heads. 80 out of 124 couples, or 64.5% tilted their heads to the right. Simulate a **p-value** using a "50/50 coin-flipping" model for the assumption of the **null hypothesis** $H_0$ that the population of humans don't have left or right head tilt tendencies when kissing, and use the table below to determine the level of evidence we have against $H_0$. <br>
# 
# <details class="details-example"><summary style="color:blue"><u>Further Guidance</u></summary>
# 
# > _The previous three "Questions 2-4" are highly relevant here. For this question, you need to first (along the lines of "Question 2") understand what the problem context describes to you in terms of something analogous to $x_i\!$'s, $\bar x$, $\mu$, and $\mu_0$. Then you need to (along the lines of "Question 3") figure out how to "imagine a world where the null hypothesis is true" so that you can go about computing a (**simulation** based) p-value calcuation for the null hypothesis under consideration relative to the available data. And finally, you need to make a determination about your potential decision to reject the null hypothesis on the strength of the data at hand on the basis of the "strength of evidence" table given below (which indeed supports the necessary interpretation required to provide an explanation answering "Question 4")._
# >    
# > _Regarding Güntürkün (2003) itself, click [here](https://www.nature.com/articles/news030210-7) if you want to know more!_    
#     
# </details> 
# 
# 
# |p-value|Evidence|
# |-|-|
# |$$p > 0.1$$|No evidence against the null hypothesis|
# |$$0.1 \ge p > 0.05$$|Weak evidence against the null hypothesis|
# |$$0.05 \ge p > 0.01$$|Moderate evidence against the null hypothesis|
# |$$0.01 \ge p > 0.001$$|Strong evidence against the null hypothesis|
# |$$0.001 \ge p$$|Very strong evidence against the null hypothesis|
# 
# ![Rodin's sculpture, "The Kiss"
# ](https://upload.wikimedia.org/wikipedia/commons/thumb/d/d1/Rodin_-_Le_Baiser_06.jpg/409px-Rodin_-_Le_Baiser_06.jpg)
# 

# Null hypothesis: The population of humans don't have left or right head tilt tendencies when kissing
# H0: 𝜇0 = 0.5
# H1: 𝜇 ≠ 0.5

# In[1]:


import numpy as np

# Simulation parameters
n_simulations = 10000  # Number of simulations
n_couples = 124        # Total number of couples
right_tilt_observed = 80  # Observed number of right tilts
prob_right_tilt = 0.5  # Null hypothesis: equal probability of tilting right or left

# Simulating n_simulations number of experiments, each with 124 "coin flips"
simulations = np.random.binomial(n=n_couples, p=prob_right_tilt, size=n_simulations)

# Calculate p-value: proportion of simulations where right tilts are >= 80
p_value = np.mean(simulations >= right_tilt_observed)

p_value


# Since 0.0006 < 0.001, according to the column 0.001 ≥ 𝑝, there is very strong evidence against the null hypothesis.

# Chatbot link: https://chatgpt.com/share/6706eeeb-dfc4-8003-8f87-60678df0e08e

# <details class="details-example"><summary style="color:blue"><u>Continue now...?</u></summary>
# 
# ### Pre-lecture VS Post-lecture HW
# 
# Feel free to work on the \"Postlecture\" HW below if you're making good progress and want to continue: the next questions will continue addressing and building on the topics from the videos, so, it's just a choice whether or not you want to work a head a little bit...
#     
# *The benefits of continue would are that (a) it might be fun to try to tackle the challenge of working through some problems without additional preparation or guidance; and (b) this is a very valable skill to be comfortable with; and (c) it will let you build experience interacting with ChatBots (and beginning to understand their strengths and limitations in this regard)... it's good to have sense of when using a ChatBot is the best way to figure something out, or if another approach (such as course provided resources or a plain old websearch for the right resourse) would be more effective*
#     
# </details>    

# ## "Post-lecture" HW [*submission along with "Pre-lecture" HW is due prior to next TUT*]

# ### 6. Can a smaller p-value definitively prove that the null hypothesis is false? Is it possible to definitively prove that Fido (from the "second pre-lecture video") is innocent using a p-value? Is it possible to difinitively prove that Fido is guilty using a p-value? How low or high does a p-value have to be to definitely prove one or the other? Explain this concisely in your own words.<br>

# A smaller p-value cannot definitively prove that the null hypothesis is false, it also means that the probability that the null hypothesis is true is very low. Is it not possible to definitively prove that Fido is innocent or guilty using a p-value. A p-value have to be 0 or 1 in order to definitely prove that the null hypothesis is false or true, but this is very unlikely. Even if the p-value is extremely low or high, we still cannot say that we 'prove' the hypothesis because our hypothesis test is performed based on the sample data and does not include the whole population completely. Hence, there would always be some uncertainty in terms of the conclusion we draw.

# ### 7. In the second half of the "first pre-lecture video" the concept of a "one sided" (or "one tailed") test is introduced in contrast to a "two sided" (or "two tailed") test. Work with a ChatBot to adjust the code from "Demo II of  the Week 5 TUT" (which revisits the "Vaccine Data Analysis Assignment" from Week 04 HW "Question 8") in order to compute a p-value for a "one sided" (or "one tailed") hypothesis test rather than the "two sided" (or "two tailed") version it provides. Describe (perhaps with the help of your ChatBot) what changed in the code; how this changes the interpretation of the hypothesis test; and whether or not we should indeed expect the p-value to be smaller in the "one tailed" versus "two tailed" analysis. <br>
# 
# <details class="details-example"><summary style="color:blue"><u>Further Guidance</u></summary>
# 
# > _[Demo II of the The Week 5 TUT](https://github.com/pointOfive/stat130chat130/blob/main/TUT/STA130F24_TUT05_Oct04.ipynb) revisiting the "[Vaccine Data Analysis Assignment](https://github.com/pointOfive/stat130chat130/blob/main/HW/STA130F24_HW04_DueOct03.ipynb)" illustrates using simulation to estimate a two-sided (or "two tailed") p-value._
# >
# > _The notion of "one sided" or "two sided" tests is also referred to as "one tailed" or "two tailed" because (other than using "$\leq$" and "$>$" [or "$\geq$" and "$<$"] rather than "$=$" and "$\neq$" when specifying $H_0$ and $H_A$) the actual place where this distinction has a practical impact is in the calculation of p-values, which is done in the "tails" of the sampling distribution of the statistic of interest under the assumption that the null hypothesis is true._
# >
# > Don't forget to ask for summaries of your ChatBot session(s) if you are using a ChatBot interaction to help learn and understand something! You only need to include link(s) to chat log histories if you're using ChatGPT, e.g., if you're using the custom STA130 NBLM ChatBot you can't get chat history logs, but you can get summaries, so just paste these into your homework notebook and indicate the both you're using if it can't provide links to chat log histories.
# 
# </details>

# In[23]:


print(pd.DataFrame({'HealthScoreChange': patient_data['HealthScoreChange'],
                    '> 0 ?': patient_data['HealthScoreChange']>0}))

random_difference_sign = np.random.choice([-1, 1], size=len(patient_data))
pd.DataFrame({'HealthScoreChange': random_difference_sign*patient_data['HealthScoreChange'].abs(),
              '> 0 ?': (random_difference_sign*patient_data['HealthScoreChange'])>0})


# In[25]:


np.random.seed(1)  # make simulation reproducible
number_of_simulations = 10000  # experiment with this... what does this do?
n_size = len(patient_data)  # 10
IncreaseProportionSimulations_underH0random = np.zeros(number_of_simulations)

# generate "random improvement" proportions assuming H0 (vaccine has no average effect) is true 
# meaning that the "before and after" differences are positive or negative at "random"
for i in range(number_of_simulations):
    
    # why is this equivalent to the suggested idea above?
    random_improvement = np.random.choice([0,1], size=len(patient_data), replace=True)  # <<< `replace=True` ^^^

    # why is .mean() a proportion? 
    IncreaseProportionSimulations_underH0random[i] = random_improvement.mean()

population_parameter_value_under_H0 = 0.5

observed_statistic = (patient_data.HealthScoreChange>0).mean()
simulated_statistics = IncreaseProportionSimulations_underH0random

SimStats_as_or_more_extreme_than_ObsStat = \
    abs(simulated_statistics - population_parameter_value_under_H0) >= \
    abs(observed_statistic - population_parameter_value_under_H0) 
    
print('''Which simulated statistics are "as or more extreme"
than the observed statistic? (of ''', observed_statistic, ')', sep="")

pd.DataFrame({'(Simulated) Statistic': simulated_statistics,
              '>= '+str(observed_statistic)+" ?": ['>= '+str(observed_statistic)+" ?"]*number_of_simulations, 
              '"as or more extreme"?': SimStats_as_or_more_extreme_than_ObsStat})


# In[31]:


import numpy as np
import plotly.figure_factory as ff
import plotly.graph_objects as go

# Create histogram data with small random noise added for visualization purposes
hist_data = [IncreaseProportionSimulations_underH0random + np.random.uniform(-0.05, 0.05, size=len(IncreaseProportionSimulations_underH0random))]
group_labels = ['SYNTHETICALLY<br>SIMULATED<br>Sampling<br>Distribution<br>of the<br>Sample<br>Mean<br><br>assuming<br>that the<br>H0 null<br>hypothesis<br>IS TRUE']

# Create the distribution plot
fig = ff.create_distplot(hist_data, group_labels, curve_type='normal',
                         show_hist=True, show_rug=False, bin_size=0.1)

# Define variables for the plot
pv_y = 2.5
pv_y_ = .25

# Add a line for the observed statistic
fig.add_shape(type="line", x0=observed_statistic, y0=0, 
              x1=observed_statistic, y1=pv_y,
              line=dict(color="Green", width=4), name="Observed Statistic")

# Add a text label for the observed statistic
fig.add_trace(go.Scatter(x=[observed_statistic], y=[pv_y+pv_y_], 
                         text=["Observed<br>Statistic<br>^"], mode="text", showlegend=False))

# Add a transparent rectangle for the upper extreme region (one-tailed)
fig.add_shape(type="rect", x0=observed_statistic, y0=0, x1=1.25, y1=pv_y,
              fillcolor="LightCoral", opacity=0.5, line_width=0)

# Update layout for one-tailed test
fig.update_layout(
    title="SYNTHETICALLY SIMULATED Sampling Distribution<br>under H0 with One-Tailed p-value Region",
    xaxis_title="Mean Health Score Change", 
    yaxis_title="Density", 
    yaxis=dict(range=[0, pv_y+2*pv_y_])
)

# Show the figure
fig.show()  # Use `fig.show(renderer="png")` for GitHub and MarkUs submissions


# In[30]:


# Calculate the observed statistic (proportion of positive changes)
observed_statistic = (patient_data.HealthScoreChange > 0).mean()
simulated_statistics = IncreaseProportionSimulations_underH0random

# One-tailed test: check if simulated statistics are greater than or equal to observed statistic
# Since we're interested in whether the observed statistic is significantly greater,
# we don't need the absolute values; we just compare directly.
SimStats_more_extreme_than_ObsStat = (simulated_statistics >= observed_statistic)

# Calculate the p-value for the one-tailed test
p_value = SimStats_more_extreme_than_ObsStat.sum() / number_of_simulations

# Print results
print("Number of Simulations: ", number_of_simulations, "\n\n",
      "Number of simulated statistics (under H0)\n",
      'that are "as or more extreme" than the observed statistic: ',
      SimStats_more_extreme_than_ObsStat.sum(), "\n\n",
      'p-value\n(= simulations "as or more extreme" / total simulations): ', p_value, sep="")


# Key Changes:
# - Removed Symmetric Statistic: Since this is a one-tailed test, we no longer consider the lower "symmetric" extreme. The symmetric_statistic and its corresponding green line are no longer needed.
# - Upper Extreme Region Only: We now only shade the region to the right of the observed statistic, where the p-value is calculated. This represents the "as or more extreme" region for a one-tailed test.
# - Title and Labels: The plot title now reflects that this is a one-tailed test, and the figure only highlights the right-hand side where the observed statistic lies.
# 
# By changing to a one-tailed test, we narrow the focus of our hypothesis test to only one direction of interest, which can enhance the power of the test to detect an effect in that direction. For a two-teiled test, we cannot see the direction of changes clearly if we reject the null hypothesis. For example in this case, performing a right-tail test allows us to focus on whether patients' health score improved over time rather than merely "changed" over time. However, it's essential to ensure that our research question justifies a one-tailed approach, as this limits the conclusions we can draw to that specific direction. 
# 
# We should generally expect the p-value to be smaller in a one-tailed test compared to a two-tailed test, given the same dataset and hypothesis parameters. This is because a one-tailed test focuses solely on one direction, it can lead to smaller p-values for the same observed effect when compared to a two-tailed test. In a one-tailed test, the p-value is calculated based on the area in one tail of the distribution. This means we are only considering extreme values in one direction.

# ### 8. Complete the following assignment. 

# ### Fisher's Tea Experiment
# 
# **Overview**
# 
# A most beloved piece of [statistical lore](https://rss.onlinelibrary.wiley.com/doi/full/10.1111/j.1740-9713.2012.00620.x) about the (most famous) statistician Ronald Fisher involves cups of tea with milk. Fisher and his friend and colleague, Dr. Muriel Bristol, worked at Cambridge in the 1920s and regularly had tea together. During one of their afternoon tea times, Bristol refused a cup of tea from Fisher because he put milk in first BEFORE pouring in the tea. Bristol said she could taste the difference, and much preferred the taste of tea when the milk was poured in afterward the tea. Fisher didn't think that there could be a difference and proposed a hypothesis test to examine the situation.
# 
# Fisher made 8 cups of tea, 4 with milk added in first and 4 with tea added in first, and gave them to Dr. Bristol without her seeing how they were made and she would say if she thought the tea or the milk was poured first. As it turned out, Bristol correctly identified if the tea or milk was poured first for all 8 of the cups. Fisher, being a skeptical statistician wanted to test if this could be happening by chance with Bristol just randomly guessing (or whether there was evidence against an assumption of Bristol just randomly guessing), and subsequently designed a statistical hypothesis test to do so.
# 
# Suppose you run an experiment like this with students in STA130. You get a random sample of 80 STA130 students to each taste one cup of tea and tell you whether they think the milk or tea was poured first. **Suppose 49 students are able to correctly state which was poured first.** Provide a statistical analysis of this experiment as guided through the following set of questions.
# 
# **Data**
# 
# 49 out of a sample of 80 students are able to correctly state which was poured first.
# 
# **Deliverables**
# 
# While you can choose how to approach the project, we are interested in evaluating your report relative to the following deliverables: 
# - Clarity of your documentation, code, and written report 
# - Description of the population (and sample) and parameter of interest (and corresponding observed test statistic) 
# - Formal null hypotheses $H_0$ 
#     - Provide a formal version $H_0$ based on the population parameter 
#     - Provide an informal interpretive statement explaining $H_0$ in more casual everyday common language
#     - Alternative hypothesis $H_A$ in terms of $H_0$
# - Quantitative analysis addressing the validity of $H_0$
#     - Explanation of the method clearly articulating the purpose of the usage of statistic(s) to address $H_0$ the population parameter of interest 
# 
# 
# **Comments**
# 
# - Regarding the population (and the sample), there is a clear difference between the experiment with STA130 students considered here and the original motivating experimental context of Fisher and Bristol.
#     - the sample size is different.
#     - but so too is the nature of the population. the parameter in question might be considered more personalized in the original experiment; whereas, the parameter in the context of STA130 students might be a more abstract concept
# - The analysis here could be approached from the perspective of formal hypothesis testing.
#     - which would likely involve the simulation of a sampling distribution under $H_0$ in order to estimate p-value with respect to the null hypothesis based on the observed test statistic (how?), concluding with the assement of $H_0$ based on an interpretation of the meaning of the p-value relative to $H_0$
#     - but a confidence interval approach to considering the hypothesis could also be considered.
# 
# > Consider organizing your report within the following outline template.
# > - Problem Introduction 
# >     - Relationship between this experiment and the original with Fisher and Bristol
# >     - Statements of the Null Hypothesis and Alternative hypothesis
# > - Quantitative Analysis
# >     - Methodology Code and Explanations
# >     - *(if needed/optional)* Supporting Visualizations 
# > - Findings and Discussion
# >     - Conclusion regarding the Null Hypothesis
# 
# #### Further Instructions:
# - When using random functions, you should make your analysis reproducible by using the `np.random.seed()` function
# 

# ### Problem Introduction
# - Relationship between this experiment and the original with Fisher and Bristol
#     The relationship between this and the original experiment with Fisher and Bristol is that they both have the same hypothesis. Both experiments are trying to test whether the participants can correctly identify whether is tea or milk that got poured in first statistically. The orignal experiment on Bristol only had a sample size of 1, and this experiment allows further and more generalizable conclusion to be drawn about identifying tea and milk.
# - Statements of the Null Hypothesis and Alternative hypothesis
#   $H_0$: p = 0.5
#   $H_1$: p ≠ 0.5
#   The population parameter of interest is the proportion of all possible responses in the population that correctly identify whether tea or milk was poured first. Since there is only two choices (tea and milk), the null hypothesis in this case is 0.5 because we are assuming that the proportion of students that can identify correctly is 50%, meaning they got the right answer purely by chance. The alternate hypothesis would be p ≠ 0.5, meaning that the students do not get the right answers just by guessing. In the context of this experiment, the sample parameter for the proportion will be calculated using the number of students that identify tea or milk correctly (49) over the total number of students (80).

# ### Quantitative Analysis
#   - Methodology Code and Explanations
#   - (if needed/optional) Supporting Visualizations

# In[10]:


# Importing numpy for the code to work
import numpy as np

# Observed data
observed_correct = 49
n_students = 80
observed_proportion = observed_correct / n_students

# Number of bootstrap samples
n_bootstrap_samples = 10000

# Bootstrapping: Resample with replacement
bootstrap_proportions = np.zeros(n_bootstrap_samples)
for i in range(n_bootstrap_samples):
    bootstrap_sample = np.random.choice([1, 0], size=n_students, p=[observed_proportion, 1-observed_proportion])
    bootstrap_proportions[i] = bootstrap_sample.mean()

# Confidence interval: 95% percentile-based
lower_bound = np.percentile(bootstrap_proportions, 2.5)
upper_bound = np.percentile(bootstrap_proportions, 97.5)

# Generate null distribution under H0: p = 0.5
null_proportions = np.zeros(n_bootstrap_samples)
for i in range(n_bootstrap_samples):
    null_sample = np.random.choice([1, 0], size=n_students, p=[0.5, 0.5])
    null_proportions[i] = null_sample.mean()

# P-value for a one-tailed test (proportion greater than 0.5)
p_value_bootstrap = np.mean(null_proportions >= observed_proportion)

lower_bound, upper_bound, p_value_bootstrap


# In[8]:


import matplotlib.pyplot as plt
import seaborn as sns

# Plotting
plt.figure(figsize=(10, 6))

# Plot bootstrap distribution
sns.histplot(bootstrap_proportions, color='blue', kde=True, label='Bootstrap Distribution', stat='density')

# Plot null distribution under H0
sns.histplot(null_proportions, color='red', kde=True, label='Null Distribution (H0: p=0.5)', stat='density')

# Add vertical lines for observed proportion and confidence intervals
plt.axvline(observed_proportion, color='green', linestyle='--', label=f'Observed Proportion ({observed_proportion:.3f})')
plt.axvline(lower_bound, color='orange', linestyle='--', label=f'95% CI Lower Bound ({lower_bound:.3f})')
plt.axvline(upper_bound, color='orange', linestyle='--', label=f'95% CI Upper Bound ({upper_bound:.3f})')

# Shading p-value area in the null distribution
plt.fill_betweenx([0, 5], observed_proportion, 1, color='lightcoral', alpha=0.5, label='P-value region (right tail)')

# Add title and labels
plt.title('Bootstrap Distribution vs Null Distribution', fontsize=16)
plt.xlabel('Proportion of Correct Answers', fontsize=12)
plt.ylabel('Density', fontsize=12)
plt.legend()

# Show plot
plt.savefig("bootstrap_vs_null_distribution.png", format='png', dpi=300)

plt.show()


# ### Findings and Discussion
# Based on the calculated p-value and confidence interval, we can reject the null hypothesis because p-value=0.0296 < 0.05. It can be concluded that the students can identify whether tea or milk is poured first correctly at a 95% confidence level.

# Chatbot link: https://chatgpt.com/share/670730ab-b780-8003-8b17-1448f622ea95

# Summary of Interactions:
# Hypothesis Test Setup:
# 
# You were analyzing an experiment with 49 students correctly identifying whether tea or milk was poured first out of 80 students.
# We discussed using 
# 𝑝
# =
# 0.5
# p=0.5 as the null hypothesis (random guessing) and performed a one-tailed hypothesis test to see if the observed proportion of correct answers is greater than 0.5.
# We confirmed that using 
# 𝑝
# =
# 0.5
# p=0.5 was a valid setup, and the population parameter would be 0.5 while the sample proportion was 
# 49
# 80
# ≈
# 0.6125
# 80
# 49
# ​
#  ≈0.6125.
# Statistical Tests:
# 
# We performed a Z-test for proportions using the observed data:
# Z-test statistic: ~2.07
# P-value: 0.0194
# Since the p-value was less than the significance level 
# 𝛼
# =
# 0.05
# α=0.05, we rejected the null hypothesis, indicating that the proportion of students correctly identifying tea or milk was statistically significantly greater than 0.5.
# Bootstrapping Approach:
# 
# You wanted to explore bootstrapping to estimate the confidence interval and calculate the p-value.
# We generated bootstrap samples from the observed proportion and calculated the 95% confidence interval:
# 95% CI: [0.500, 0.713]
# P-value (using bootstrap): 0.029
# The p-value was again less than 
# 𝛼
# =
# 0.05
# α=0.05, leading us to reject the null hypothesis.
# Visualization:
# 
# I provided code to visualize the results by comparing the bootstrap distribution and the null distribution under 
# 𝑝
# =
# 0.5
# p=0.5, highlighting the observed proportion and confidence interval, and shading the p-value region.
# Randomness & Reproducibility:
# 
# We discussed how to use np.random.seed() to ensure reproducibility of results when generating random numbers, and how it works with functions like np.random.choice() to produce consistent random selections in simulations.
# Error Handling:
# 
# When you encountered an error using plt.show(renderer="png"), I provided guidance on how to properly save the plot to a PNG file using plt.savefig() instead of using the renderer argument in plt.show().
# 

# ### 9. Have you reviewed the course wiki-textbook and interacted with a ChatBot (or, if that wasn't sufficient, real people in the course piazza discussion board or TA office hours) to help you understand all the material in the tutorial and lecture that you didn't quite follow when you first saw it?<br>
#     
# <details class="details-example"><summary style="color:blue"><u>Further Guidance</u></summary>
#  
# >  _Here is the link of [wiki-textbook](https://github.com/pointOfive/stat130chat130/wiki) in case it gets lost among all the information you need to keep track of_  : )
# >    
# > _Just answering "Yes" or "No" or "Somewhat" or "Mostly" or whatever here is fine as this question isn't a part of the rubric; but, the midterm and final exams may ask questions that are based on the tutorial and lecture materials; and, your own skills will be limited by your familiarity with these materials (which will determine your ability to actually do actual things effectively with these skills... like the course project...)_
#     
# </details>
# 
# _**Don't forget to ask for summaries of your ChatBot session(s) and paste these into your homework notebook (including link(s) to chat log histories if you're using ChatGPT)!**_ **But if you're using the STA130 custom NBLM ChatBot, you'll only be able to ask for summaries, of course!**

# Somewaht

# # Recommended Additional Useful Activities [Optional]
# 
# The "Ethical Profesionalism Considerations" and "Current Course Project Capability Level" sections below **are not a part of the required homework assignment**; rather, they are regular weekly guides covering (a) relevant considerations regarding professional and ethical conduct, and (b) the analysis steps for the STA130 course project that are feasible at the current stage of the course 
# 
# <br>
# <details class="details-example"><summary style="color:blue"><u>Ethical Professionalism Considerations</u></summary>
#     
# ### Ethical Professionalism Considerations
#     
# Using p-values and hypothesis testing appropriately is an important ethical and professional responsibility of anyone doing data analysis. Actually, there is quite the quiet Contra-Versy (or is it Con-TROV-ersy?) around p-values. First, on a general level, it seems quite clear that p-values and hypothesis testing methodologies MUST play some ongoing contributing role in the so-called "replication crisis" rampantly afflicting mordern science; namely, "significant findings" made in scientific studies are not able to be reproduced by future studies at an alarming rate; and, this whole paradigm of "significant findings" is based on p-values and hypothesis testing... so, something's going on with this methodology in some way...
#     
# More specifically however, p-values are themselves quite problematic. To see this, just briefly consider the following article titles...
# 
# - [Why are p-values controversial?](https://www.tandfonline.com/doi/full/10.1080/00031305.2016.1277161) 
# - [What a nerdy debate about p-values shows about science and how to fix it](https://www.vox.com/science-and-health/2017/7/31/16021654/p-values-statistical-significance-redefine-0005)
# - [The reign of the p-value is over: what alternative analyses could we employ to fill the power vacuum?](https://royalsocietypublishing.org/doi/10.1098/rsbl.2019.0174)
# - [Scientists rise up against statistical significance](https://www.nature.com/articles/d41586-019-00857-9)
# - [Statistics experts urge scientists to rethink the p-value](https://www.spectrumnews.org/news/statistics-experts-urge-scientists-rethink-p-value)
# 
# While the issues here are relatively advanced and subtle (as introduced [here](https://www2.stat.duke.edu/~berger/p-values.html), presented [here](https://www.jarad.me/courses/stat587Eng/slides/Inference/I06-Pvalues/why_pvalues_dont_mean_what_you_think_they_mean.pdf), and demonstrated using simulation [here](https://jaradniemi.shinyapps.io/pvalue/)), the problem essentially comes down to the fact that most scientists (or just people) don't know how to really interpret the numeric value of a p-value. There are therefore two current proposed solutions to address this challenge.
#     
# 1. Just interpreting p-values using the follwing table (which really isn't that hard, so it's surprising that this solution isn't more broadly adopted...)
#     
# |p-value|Evidence|
# |-|-|
# |$$p > 0.1$$|No evidence against the null hypothesis|
# |$$0.1 \ge p > 0.05$$|Weak evidence against the null hypothesis|
# |$$0.05 \ge p > 0.01$$|Moderate evidence against the null hypothesis|
# |$$0.01 \ge p > 0.001$$|Strong evidence against the null hypothesis|
# |$$0.001 \ge p$$|Very strong evidence against the null hypothesis|
#     
# 
# 2. Only do **hypothesis testing** on the basis of confidence intervals, not **p-values** (which might be the best solution wherever doing so is a realistic, convenient  possibility...)
# 
# With this quite broad introductory context in mind, what does your favorite ChatBot thinks about the following statements? 
#     
# 1. Hypothesis testing is not a "mathematical proof"<br><br>
# 
#     1. We do not prove $H_0$ false, we instead give evidence against the $H_0$: "We reject the null hypothesis with a p-value of XYZ, meaning we have ABC evidence against the null hypothesis"
#     2. We do not prove $H_0$ is true, we instead do not have evidence to reject $H_0$: "We fail to reject the null hypothesis with a p-value of XYZ"<br><br>
# 
# 2. Implying that a "non-significant result" means there is "no effect" misleads an audience because this may in actual fact simply indicate that there was insufficient evidence to reject the null hypothesis. So this therefore overlooks the possibility of sample size limitations, or Type II errors (which means a test incorrectly concludes that there is no effect or difference when, in fact, there is one). 
#     
# > Similarly, analagously, a "significant result" used to reject the null hypothsis could alternatively be a Type I error (which means a test actually incorrectly rejected a null hypothesis when it was actually true)... we're only providing a measure of evidence against the null hypothesis... but the evidence could still incorrectly suggest the wrong conclusion... it really depends on how strong the evidence is...
# >
# > - all of which is why just interpreting p-values using the table above is a good idea...
# 
# 3. The p-values used for hypothesis testing are contructed upone the assumptions of the null hypotheses they correspond to; but, null hypotheses are actually often presented in simple forms that routinely hide a lot of information that is implicitly used to construct the p-values. For example, distributional assumptions about the population, estimated "plug-in" values that can used to simplify the problem calculations, and the reliance upon "random sampling", etc...<br><br>
#            
# 4. Drawing overly broad conclusions, or making recommendations based on findings that reject the null hypothesis in a specific context is fraught with the problematic risks of overgeneralization errors. Further exacerbating this issue, null hypotheses are typically so called "point null hypotheses" which is meant to emphasize that they are mathematically increadibly sharply specific; whereas, alternative hypotheses are usually very unspecific. An alternative hypothesis that "the null hypothesis is false" doesn't say much... we should wonder, "how, specfically, is the null false?"
#     
# As an example really giving a demonstrating this, consider rejecting a null hypothesis that there is no correlation between rain and pizza's delivered. Such a decision doesn't specify what the actual hypothetical correlation might be. In fact, it doesn't even indicate if there are more or less pizzas delivered when it rains... 
# 
# > which, actually, shows very clearly why statistical inference using hypothesis testing is inferior to statistical inference based on confidence intervals...
# > 
# > - a confidence interval provides a range of plausible values of what the parameter in question might be; whereas, ...
# > - trying to more clearly address what the plausible values of the parameter in question might be on the basis of hypothesis testing would require conducting further experiements to continously reject increasingly detailed hypothesies to narrow down what the alternative hypothesis might actually include... which would indeed be an utterly vapid misuse of the intended purpose of hypothesis testing entrprise... 
#     
# </details>
# 
# <details class="details-example"><summary style="color:blue"><u>Current Course Project Capability Level</u></summary>
#     
# ### Current Course Project Capability Level
#     
# **Remember to abide by the [data use agreement](https://static1.squarespace.com/static/60283c2e174c122f8ebe0f39/t/6239c284d610f76fed5a2e69/1647952517436/Data+Use+Agreement+for+the+Canadian+Social+Connection+Survey.pdf) at all times.**
# 
# Information about the course project is available on the course github repo [here](https://github.com/pointOfive/stat130chat130/tree/main/CP), including a draft [course project specfication](https://github.com/pointOfive/stat130chat130/blob/main/CP/STA130F23_course_project_specification.ipynb) (subject to change). 
# - The Week 01 HW introduced [STA130F24_CourseProject.ipynb](https://github.com/pointOfive/stat130chat130/blob/main/CP/STA130F24_CourseProject.ipynb), and the [available variables](https://drive.google.com/file/d/1ISVymGn-WR1lcRs4psIym2N3or5onNBi/view). 
# - Please do not download the [data](https://drive.google.com/file/d/1mbUQlMTrNYA7Ly5eImVRBn16Ehy9Lggo/view) accessible at the bottom of the [CSCS](https://casch.org/cscs) webpage (or the course github repo) multiple times.
#     
# > ### NEW DEVELOPMENT<br>New Abilities Achieved and New Levels Unlocked!!!    
# > **As noted, the Week 01 HW introduced the [STA130F24_CourseProject.ipynb](https://github.com/pointOfive/stat130chat130/blob/main/CP/STA130F24_CourseProject.ipynb) notebook.** _And there it instructed students to explore the notebook through the first 16 cells of the notebook._ The following cell in that notebook (there marked as "run cell 17") is preceded by an introductory section titled, "**Now for some comparisons...**", _**and all material from that point on provides an example to allow you to start applying what you're learning about Hypothesis Testing to the CSCS data**_ as now suggested next below.
# 
#     
# At this point in the course there should be two kinds of hypothesis testing analyses you should be able to use to provide evidence against a null hypothesis (about some of the interesting columns from the Canadian Social Connection Survey data):
#     
# 1. Any "before and after" data that can be made into differences can be used to test a null hypothesis of "no effect" of an intervention on the average change in the population (as illustrated through the example of the Week 5 TUT **Demo**)
#     
# 2. Any binary data that could be approached analagously to the "Stella's Wheel of Destiny" example of the Week 5 TUT **Communication Activity** can be used to test a null hypothesis about the (population) chance of success `p` (using a `np.random.choice([0,1], p)` population to simulate the sampling distribution under the null)
#     
#     1. [For Advanced Students Only] And actually, hypothesis testing for other numerical data could be approached analagously to the method based on assuming a distibution for the population (such as `stats.norm(loc=mu0, scale=x.std)` in place of `np.random.choice([0,1], p)`... if you see what this means?)
#     2. Or it could be based on seeing if a hypothesized parameter value was contained within a bootstrapped confidence interval...
#     
# 
# 1. How do hypothesis testing analyses correspond to bootstrapped confidence intervals? 
#     
# 2. Create a **null hypothesis** about a population parameter than you can test using the Canadian Social Connection Survey data
# 
# 3. Carry out the hypothesis test using simulation, and interpret the result of the estimated p-value relative to the null hypothesis
#     
# </details>    

# In[ ]:




