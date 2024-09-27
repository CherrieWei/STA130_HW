#!/usr/bin/env python
# coding: utf-8

# ## STA130 Homework 03 
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

# 
# ### Marking Rubric (which may award partial credit) 
# 
# - [0.1 points]: All relevant ChatBot summaries [including link(s) to chat log histories if you're using ChatGPT] are reported within the notebook
# - [0.2 points]: Assignment completion confirmed by visual submission for "2" 
# - [0.3 points]: Evaluation of written communication for "3" 
# - [0.1 points]: Correct answers for "4"
# - [0.3 points]: Evidence of meaningful activity for "6"
# 
# <!-- - [0.1 points]: Assignment completion confirmed by ChatBot interaction summaries for "5" -->
# 

# ### "Pre-lecture" HW [*completion prior to next LEC is suggested but not mandatory*]

# 
# #### 1. Use *fig.add_[h/v]line()* and *fig.add_[h/v]rect()* to mark, respspectively, location (mean and median) and scale (range, interquartile range, and a range defined by two standard deviations away from the mean in both directions) of *flipper_length_mm* for each _species_ onto _plotly_ histograms of *flipper_length_mm* for each _species_ in the penguins dataset<br>
# 
# <details class="details-example"><summary style="color:blue"><u>Further Guidance</u></summary>
# 
# **Time Management Warning**: it takes a long time to make a figure, whether you're working with a ChatBot, or building it from scratch based on trial and error changes with your code. ChatBots remove the need to understand the detailed nuances of data visualization library arguments and construction procedures. But after you've passed the 30 minute range of effort working with your ChatBot for this problem to try to get what you want, then your only options are to start a new session and hope for a smoother experience based on improved clarity of your directions, or submit what you have along with a brief note highlighting the duration in your chatlog history where your efforts to make progress did not produce the desired outcome.
# 
# > The code referenced above [*fig.add_[h/v]line()*](https://plotly.com/python/horizontal-vertical-shapes/) and [*fig.add_[h/v]rect()*](https://plotly.com/python/line-charts/) refer to `fig.add_hline()` and `fig.add_hline()` and `fig.add_hrect()` and `fig.add_vrect()` which overly lines rectangles onto a figure from different orientation perspectives.
# >
# > - _There are several considerations in this problem..._
# >     - _The histograms can be on the same figure, on separate figures, or separated into different panels in the same figure_
# >     - _The elements within a figure should be well annotated, probobably using a so-called legend to help make sure annotations don't overlap each other and are clear and readible_
# > - _There are several ways to approach this problem..._
# >     - _You will likely be very pleased when you run the code returned to you as the result of pasting this question in as a prompt into a ChatBot session; but, you will also likely need to interact with the ChatBot to ask for adjustments to the code which give a final satisfactory figure (and this is the recommended approach to get the experience this problem intends you to have)_
# >     - _**When using a ChatBot, if the code provided by your ChatBot results in an error, show the error to your ChatBot and iterate this process with the adjusted "fixed" code provided by the ChatBot... this process usually converges some something workable that's pretty close to what you were going for**_
# >     - <u>**And don't forget, a ChatBot can explain what how code it provides works, if you ask it to...**</u>
# >     - _You could alternatively figure out how to code this plot up for yourself by looking at the provided documentation links and perhaps using some additional google searchers or ChatBot queries to help out with specific issues or examples; and, if you end up interested in figuring out a little more how the code works that's great and definitely feel free to go ahead and do so, but at this stage the point of this problem is to understand the general ideas of figures themselves as opposed to being an expert about the code that generated them_
#     
# </details>
# 

# 

# In[1]:


import pandas as pd 
pingees = pd.read_csv("https://raw.githubusercontent.com/mwaskom/seaborn-data/master/penguins.csv")
pingees


# In[2]:


import plotly.offline as pyo
pyo.init_notebook_mode()


# In[ ]:





# In[ ]:





# In[9]:


import plotly.express as px
import plotly.graph_objects as go
import seaborn as sns
import numpy as np

# Load the penguins dataset
penguins = sns.load_dataset("penguins")

# Calculate statistics for each species
species_stats = penguins.groupby("species")["flipper_length_mm"].agg(
    mean="mean",
    median="median",
    min="min",
    max="max",
    std="std",
    q1=lambda x: np.percentile(x.dropna(), 25),
    q3=lambda x: np.percentile(x.dropna(), 75)
).reset_index()

# Create a histogram for each species
fig = px.histogram(penguins, x="flipper_length_mm", color="species", marginal="box", nbins=30)

# Add lines and rectangles for each species without annotation texts
for _, row in species_stats.iterrows():
    species = row['species']
    mean = row['mean']
    median = row['median']
    min_val = row['min']
    max_val = row['max']
    std = row['std']
    q1 = row['q1']
    q3 = row['q3']
    
    # ±2 standard deviations
    lower_2std = mean - 2 * std
    upper_2std = mean + 2 * std
    
    # Add vertical lines for mean and median
    fig.add_vline(x=mean, line_dash="dash", line_color="blue", row="all")
    fig.add_vline(x=median, line_dash="dot", line_color="red", row="all")
    
    # Add rectangles for ranges
    fig.add_vrect(x0=min_val, x1=max_val, fillcolor="lightgreen", opacity=0.2, line_width=0, row="all")
    fig.add_vrect(x0=q1, x1=q3, fillcolor="lightblue", opacity=0.2, line_width=0, row="all")
    fig.add_vrect(x0=lower_2std, x1=upper_2std, fillcolor="lightcoral", opacity=0.2, line_width=0, row="all")

# Add invisible traces for custom legend
fig.add_trace(go.Scatter(
    x=[None], y=[None],
    mode='lines',
    line=dict(color="blue", dash="dash"),
    showlegend=True,
    name="Mean"
))
fig.add_trace(go.Scatter(
    x=[None], y=[None],
    mode='lines',
    line=dict(color="red", dash="dot"),
    showlegend=True,
    name="Median"
))
fig.add_trace(go.Scatter(
    x=[None], y=[None],
    mode='lines',
    fill='toself',
    marker=dict(color="lightgreen"),
    showlegend=True,
    name="Range (Min-Max)"
))
fig.add_trace(go.Scatter(
    x=[None], y=[None],
    mode='lines',
    fill='toself',
    marker=dict(color="lightblue"),
    showlegend=True,
    name="IQR (Q1-Q3)"
))
fig.add_trace(go.Scatter(
    x=[None], y=[None],
    mode='lines',
    fill='toself',
    marker=dict(color="lightcoral"),
    showlegend=True,
    name="±2 STD"
))

# Show the plot
fig.show()


# #### 2. Transition your ChatBot session from the previous problem to repeat the previous problem, but this time using _seaborn_ **kernel density estimation** (KDE) plots to produce the desired figures organized in row of three plots<br>
# 
# <details class="details-example"><summary style="color:blue"><u>Further Guidance</u></summary>
#     
# **Time Management Warning**: it takes a long time to make a figure, whether you're working with a ChatBot, or building it from scratch based on trial and error changes with your code. ChatBots remove the need to understand the detailed nuances of data visualization library arguments and construction procedures. But after you've passed the 30 minute range of effort working with your ChatBot for this problem to try to get what you want, then your only options are to start a new session and hope for a smoother experience based on improved clarity of your directions, or submit what you have along with a brief note highlighting the duration in your chatlog history where your efforts to make progress did not produce the desired outcome.
#     
# > The `seaborn` library extends `matplotlib` so [_ax.axhspan(...)_](https://matplotlib.org/stable/gallery/subplots_axes_and_figures/axhspan_demo.html#sphx-glr-gallery-subplots-axes-and-figures-axhspan-demo-py) or [_ax.fill_between(...)_](https://matplotlib.org/stable/gallery/lines_bars_and_markers/span_regions.html) from `matplotlib` could be combined with the [_seaborn_ KDE plot](https://seaborn.pydata.org/generated/seaborn.kdeplot.html)... this might be something to share with your ChatBot if it [tries to keep using _plotly_ or a KDE function rather than a _plotly_](https://github.com/pointOfive/stat130chat130/blob/main/CHATLOG/wk3/GPT/SLS/00001_gpt3p5_plotlyseaborn_plotting.md) plotting functionality...
# > 
# > - _When using a ChatBot, if the code provided by your ChatBot results in an error, show the error to your ChatBot and iterate this process with the adjusted "fixed" code provided by the ChatBot... this process usually converges some something workable that's pretty close to what you were going for_
# > - _**Also consider the ways that you might be able to split up the instructions for the ChatBot into multiple steps, creating a sequence of additional directions and extensions along the way as you mold the figure more and more into a form increasingly matching your desired output.**_
# > - And don't forget, a ChatBot can explain what how code it provides works, if you ask it to...
# > 
# > The technical details of the following are beyond the scope of STA130, but if you were interested, you could very briefly examine the [_seaborn_ themes](https://seaborn.pydata.org/tutorial/aesthetics.html) based on `sns.set_style()` and `sns.set_theme()` and [_colors_](https://seaborn.pydata.org/tutorial/color_palettes.html) based on the `palette` parameter, e.g.,
# > 
# > ```python
# > sns.set_style("whitegrid") # sns.set_style("dark")
# > # `sns.set_palette()` exists but functions often access and set that directly
# > sns.boxplot(..., hue='column', palette="colorblind") 
# > ```    
# > 
# > and then attempt to interact with the ChatBot to change the coloring of the figure to something that you like and looks more clear to you... 
# 
# </details>
# 

# In[10]:


import seaborn as sns
import matplotlib.pyplot as plt

# Load the penguins dataset
penguins = sns.load_dataset("penguins")

# Initialize a FacetGrid to create 3 KDE plots in a row, one for each species
g = sns.FacetGrid(penguins, col="species", col_wrap=3, height=4, aspect=1.5)

# Map the KDE plot to each species
g.map(sns.kdeplot, "flipper_length_mm", fill=True)

# Add titles and axis labels
g.set_axis_labels("Flipper Length (mm)", "Density")
g.set_titles("{col_name} Species")

# Adjust the layout for better spacing
plt.tight_layout()

# Show the plot
plt.show()


# #### 3. Search online for some images of **box plots**, **histograms**, and **kernel density estimators** (perhaps for the same data set); describe to a ChatBot what you think the contrasting descriptions of these three "data distribution" visualization methods are; and then see if the ChatBot agrees and what "pros and cons" list of these three "data distribution" visualization methods your ChatBot can come up with; finally, describe your preference for one or the other and your rationale for this preference<br>
# 
# <details class="details-example"><summary style="color:blue"><u>Further Guidance</u></summary>
# 
# > The details of the ["kernel"](https://en.wikipedia.org/wiki/Kernel_density_estimation) and how it works in [kernel density estimation](https://plotly.com/python/violin/#split-violin-plot) are beyond the scope of STA130; but, there is typically a so-called "bandwidth" **argument** (e.g., `bw_adjust` in [_seaborn_](https://stackoverflow.com/questions/37932283/confusion-with-bandwidth-on-seaborns-kdeplot)) that "controls the width of the kernel" which is analgous to the "number of bins parameter" of a histogram (e.g., `nbins` in [_plotly_](https://www.google.com/search?client=safari&rls=en&q=plotly+nbins&ie=UTF-8&oe=UTF-8))  <!-- 4. Report on your preferences between `plotly` and `seaborn` in terms of usability and the general visual aestetics -->
# > 
# > _Don't forget to ask for summaries of your ChatBot session(s) and paste these into your homework notebook (including link(s) to chat log histories if you're using ChatGPT)_
#     
# </details>

# #### 4. Run the code below and look at the resulting figure of distrubutions and then answer the following questions
# 
# 1. Which datasets have similar means and similar variances
# 2. Which datasets have similar means but quite different variances
# 3. Which datasets have similar variances but quite different means
# 4. Which datasets have quite different means and quite different variances
#     
# <details class="details-example"><summary style="color:blue"><u>Further Guidance</u></summary>
#     
# > Can you answer these questions immediately? If not, first review what the basic ideas of **sample means** and **sample standard deviations** (and **sample variances**) are. Their mathematical definitions are given below, and are useful for understanding the intuition of these concepts in terms of "averages" of things, like "observations" or "squared differences" (and then perhaps square-rooted). But there are other ways to "intuitively visually" understand **sample means** and **sample standard deviations** (and **sample variances**) which a ChatBot would be able to discuss with you.
# >
# > - sample mean $\displaystyle \bar x = \frac{1}{n}\sum_{i=1}^n x_i$ 
# > - sample variance $\displaystyle s^2 = \frac{1}{n-1}\sum_{i=1}^n (x_i-\bar x)^2$
# > - sample standard deviation $\displaystyle s = \sqrt{s^2}$
# >
# > It's potentially maybe possible that you or a ChatBot could answer these questions by looking at the code that produced the data you're considering. But if you're trying to check and understand things that way, you should instead consider just calculate the statistics that answer the questions themselves...
# > - `np.mean(df.col)` or `df.col.mean()`
# > - `np.std(df.col, dof=1)` / `np.var(df.col, dof=1)` or `df.col.std(dof=1)` / `df.col.var(dof=1)`
# >
# > _If you are resorting to calculating the statistics that answer the questions, try to understand the answers after you have them... just getting the "right" answers kind of defeats the point of this exercise..._
# >
# > - The difference between trying to answer this question using the code that produced the data versus calculating the statistics from the data comes down to the difference between **parameters** and **statistics**, but this will be discussed in the lecture... in the meantime, howevever, if you're curious about this... you could consider prompting a ChatBot to explain the difference between **parameters** and **statistics**...
# >     - ... this would naturally lead to some discussion of the relationship between **populations** and **samples**, and from there it would only be a little further to start working to understand the relationship between **statistics** and **parameters** and how they connect to *populations* and *samples* (and hence each other)...    
#     
# </details>  

# In[11]:


from scipy import stats
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import numpy as np

n = 1500
data1 = stats.uniform.rvs(0, 10, size=n)
data2 = stats.norm.rvs(5, 1.5, size=n)
data3 = np.r_[stats.norm.rvs(2, 0.25, size=int(n/2)), stats.norm.rvs(8, 0.5, size=int(n/2))]
data4 = stats.norm.rvs(6, 0.5, size=n)

fig = make_subplots(rows=1, cols=4)

fig.add_trace(go.Histogram(x=data1, name='A', nbinsx=30, marker=dict(line=dict(color='black', width=1))), row=1, col=1)
fig.add_trace(go.Histogram(x=data2, name='B', nbinsx=15, marker=dict(line=dict(color='black', width=1))), row=1, col=2)
fig.add_trace(go.Histogram(x=data3, name='C', nbinsx=45, marker=dict(line=dict(color='black', width=1))), row=1, col=3)
fig.add_trace(go.Histogram(x=data4, name='D', nbinsx=15, marker=dict(line=dict(color='black', width=1))), row=1, col=4)

fig.update_layout(height=300, width=750, title_text="Row of Histograms")
fig.update_xaxes(title_text="A", row=1, col=1)
fig.update_xaxes(title_text="B", row=1, col=2)
fig.update_xaxes(title_text="C", row=1, col=3)
fig.update_xaxes(title_text="D", row=1, col=4)
fig.update_xaxes(range=[-0.5, 10.5])

for trace in fig.data:
    trace.xbins = dict(start=0, end=10)
    
# This code was produced by just making requests to Microsoft Copilot
# https://github.com/pointOfive/stat130chat130/blob/main/CHATLOG/wk3/COP/SLS/0001_concise_makeAplotV1.md

fig.show() # USE `fig.show(renderer="png")` FOR ALL GitHub and MarkUs SUBMISSIONS


# 1. Graph A and C have similar means and variances.
# 2. Graph B and C have similar means but quite different variances
# 3. Graph B and D have similar variances but quite different means.
# 4. Graph C and D have quite different means and variances.

# Chatbot summaries:
# 1. Penguins Dataset - Plotly Customization:
# You asked about using fig.add_hline(), fig.add_vline(), fig.add_hrect(), and fig.add_vrect() in Plotly to mark statistics such as mean, median, range, interquartile range (IQR), and ±2 standard deviations for the flipper_length_mm variable in histograms for each species. I provided a detailed example using these functions to mark the relevant statistics for each species and explained how to set up the graph with vertical lines and rectangles.
# 
# 2. Custom Legends in Plotly:
# You requested help with adding a legend to avoid overlapping annotations on the graph. I explained how to add custom legends using invisible traces (showlegend=True and visible='legendonly') to keep the graph clean while still displaying the necessary information in the legend. When you reported still seeing text on the graph, I suggested removing the annotation_text parameter to prevent annotation clutter.
# 
# 3. Seaborn KDE Plot (Penguins Dataset):
# You asked how to generate Seaborn KDE plots organized in a row of three plots using the same penguins dataset. I provided an example using sns.FacetGrid() to display KDE plots for flipper_length_mm of each species in a row, with options to customize axis labels and titles for clarity.
# 
# 4. Discussion on Data Visualization Methods:
# You shared insights from your research on box plots, histograms, and kernel density estimators (KDE), explaining the different ways they visualize the distribution of data. I agreed with your assessment and elaborated on how each method highlights different aspects of the distribution, such as summary statistics, modes, and the overall shape of the data.
# 
# 5. Pros and Cons of Box Plots, Histograms, and KDE:
# You asked for a pros and cons list of box plots, histograms, and KDEs. I provided a detailed comparison, outlining the strengths and weaknesses of each visualization method in terms of clarity, precision, flexibility, and their common use cases.
# 
# 6. Final Request - Summary for Submission:
# You asked for a summary of all our interactions to submit as part of a homework assignment, which I have provided here.
# 
# Link:https://chatgpt.com/share/66f61a9a-0b3c-8003-b54d-aa537313c2f1

# <details class="details-example"><summary style="color:blue"><u>Continue now...?</u></summary>
# 
# ### Pre-lecture VS Post-lecture HW
# 
# Feel free to work on the "Post-lecture" HW below if you're making good progress and want to continue: the next questions will just continue working on data visualization related topics, so, it's just a choice whether or not you want to work a head a little bit... 
# 
# - The previous suggestions regarding **parameters** versus **statistics** would be a very good thing to look at carefully in preparation for the upcoming lecture...
#     
# *The benefits of continue would are that (a) it might be fun to try to tackle the challenge of working through some problems without additional preparation or guidance; and (b) this is a very valable skill to be comfortable with; and (c) it will let you build experience interacting with ChatBots (and beginning to understand their strengths and limitations in this regard)... it's good to have sense of when using a ChatBot is the best way to figure something out, or if another approach (such as course provided resources or a plain old websearch for the right resourse) would be more effective*
#     
# </details> 
# 
# 

# ### "Post-lecture" HW [*submission along with "Pre-lecture" HW is due prior to next TUT*]
# 
# #### 5. Start a new ChatBot session to explore the general relationship between the *mean* and *median* and "right" and "left" skewness (and why this is); what the following code does and how it works; and then explain (in your own words) the relationship between the *mean* and *median* and "right" and "left" skewness and what causes this, using and extending the code to demonstrate your explanation through a sequence of notebook cells.<br>
# 
# ```python
# from scipy import stats
# import pandas as pd
# import numpy as np
#   
# sample1 = stats.gamma(a=2,scale=2).rvs(size=1000)
# fig1 = px.histogram(pd.DataFrame({'data': sample1}), x="data")
# # USE `fig1.show(renderer="png")` FOR ALL GitHub and MarkUs SUBMISSIONS
# 
# sample1.mean()
# np.quantile(sample1, [0.5]) # median
# 
# sample2 = -stats.gamma(a=2,scale=2).rvs(size=1000)
# ```
# 
# <details class="details-example"><summary style="color:blue"><u>Further Guidance</u></summary>
#     
# > You could start this session perhaps something like [this](https://github.com/pointOfive/stat130chat130/blob/main/CHATLOG/wk3/GPT/SLS/00003_GPT3p5_meanVmedian.md)?
# > 
# > _Don't forget to ask for summaries of your ChatBot session(s) and paste these into your homework notebook (including link(s) to chat log histories if you're using ChatGPT)..._
# 
# </details> 
# 
# 

# In[15]:


from scipy import stats
import pandas as pd
import numpy as np
  
sample1 = stats.gamma(a=2,scale=2).rvs(size=1000)
fig1 = px.histogram(pd.DataFrame({'data': sample1}), x="data")
# USE `fig1.show(renderer="png")` FOR ALL GitHub and MarkUs SUBMISSIONS

sample1.mean()
np.quantile(sample1, [0.5]) # median

sample2 = -stats.gamma(a=2,scale=2).rvs(size=1000)

fig1.show()


# 5. The relationship between the mean and median can tell us whether a dataset is right skewed or left skewed. When the mean is equal to the median, it means that the dataset has a perfect symmetrical distribution. When the mean is greater than median, this means that the dataset is right-skewed. This is because for a right-skewed data set, most data points lie on the lower end but there are a few extreme values on the higher end that contribute to a higher value of mean, making the mean to become greater than the medium. For a left-skewed dataset, it is the opposite. Most data lie on the higher end, but a few extreme data points on the lower end pull the mean down and causing it to become smaller than the median.

# In[16]:


from scipy import stats
import pandas as pd
import numpy as np
  
sample1 = stats.gamma(a=2,scale=2).rvs(size=1000)
fig1 = px.histogram(pd.DataFrame({'data': sample1}), x="data")
# USE `fig1.show(renderer="png")` FOR ALL GitHub and MarkUs SUBMISSIONS

sample1.mean()
np.quantile(sample1, [0.5]) # median

sample2 = -stats.gamma(a=2,scale=2).rvs(size=1000)
fig2 = px.histogram(pd.DataFrame({'data': sample2}), x="data")

sample2.mean()
np.quantile(sample2, [0.5])

fig1.show()
fig2.show()


# 

# #### 6. Go find an interesting dataset and use summary statistics and visualizations to understand and demonstate some interesting aspects of the data<br>
# 
# 1. Your approach should likely follow what was suggested for the **Week 02 TUT Communication Activity from TUT**
# 2. In the **Week 03 TUT Communication Activity from TUT** you will be put in groups and determine which group members dataset introduction will be presented by the group
# 
# <details class="details-example"><summary style="color:blue"><u>Further Guidance</u></summary>
# 
# > A good place to browse datasets is [TidyTuesday](https://github.com/rfordatascience/tidytuesday/blob/master/README.md) as working with ChatBots to find unconventional and entertaining datasets is not particularly productive and only seems to end up with the datasets seen here and other (more interesting?) suggestions like [iris](https://gist.githubusercontent.com/netj/8836201/raw/6f9306ad21398ea43cba4f7d537619d0e07d5ae3/iris.csv), [superheros](https://raw.githubusercontent.com/steview-d/superhero-dashboard/master/static/data/superheroData.csv), [hauntings](https://raw.githubusercontent.com/andreamoleri/Hauntings/main/hauntings.csv), [bigfoot](https://raw.githubusercontent.com/hannahramirez/BigfootVsUfos/main/bigfoot_mod.csv), [ufos](https://raw.githubusercontent.com/hannahramirez/BigfootVsUfos/main/ufo_mod.csv), [sharks](https://raw.githubusercontent.com/IbaiGallego/DataCleaning_SharkAttack/main/data/jaws.csv), [legos](https://raw.githubusercontent.com/seankross/lego/master/data-tidy/legosets.csv), [bees](https://gist.githubusercontent.com/bootshine2/ba15d3cb38e2ed31129aeca403405a12/raw/10949901cd8a6a75aa46c86b804c42ff410f929e/Bee%2520Colony%2520Loss.csv), [housing](https://raw.githubusercontent.com/slavaspirin/Toronto-housing-price-prediction/master/houses_edited.csv), and [gapminder](https://raw.githubusercontent.com/kirenz/datasets/master/gapminder.csv)
# > ```python
# > # Maybe something like this? Feel free to use this one 
# > # if it strikes your fancy after look around a bit
# > import pandas as pd
# > df = pd.read_csv("https://raw.githubusercontent.com/manuelamc14/fast-food-Nutritional-Database/main/Tables/nutrition.csv")
# > df # df.columns
# > ```
# 
# </details>

# In[17]:


import pandas as pd
df = pd.read_csv("https://raw.githubusercontent.com/manuelamc14/fast-food-Nutritional-Database/main/Tables/nutrition.csv")
df


# In[24]:


import pandas as pd
import plotly.express as px

df = pd.read_csv("https://raw.githubusercontent.com/manuelamc14/fast-food-Nutritional-Database/main/Tables/nutrition.csv")

summary_stats = df.describe()
print(summary_stats)


# In[28]:


import pandas as pd
import plotly.express as px

df = pd.read_csv("https://raw.githubusercontent.com/manuelamc14/fast-food-Nutritional-Database/main/Tables/nutrition.csv")

print(df.head())
print(df.info())

print(df.columns)

df['calories'] = pd.to_numeric(df['calories'], errors='coerce')
df['total fat (g)'] = pd.to_numeric(df['total fat (g)'], errors='coerce')
df['sodium (mg)'] = pd.to_numeric(df['sodium (mg)'], errors='coerce')

print("Rows with NaN values:\n", df.isnull().sum())

df = df.dropna(subset=['calories', 'total fat (g)', 'sodium (mg)'])

summary_stats = df.describe()
print(summary_stats)


# In[29]:


fig_calories = px.histogram(df, x='calories', title='Distribution of Calories')
fig_calories.show(renderer="png")

fig_fat = px.box(df, y='total fat (g)', title='Box Plot of Total Fat Content')
fig_fat.show(renderer="png")

fig_calories_sodium = px.scatter(df, x='calories', y='sodium (mg)', title='Calories vs. Sodium')
fig_calories_sodium.show(renderer="png")

skewness = df[['calories', 'total fat (g)', 'sodium (mg)']].skew()
print("Skewness:\n", skewness)
fig_calories.show(renderer="png")


# ChatBot summaries:
# 1. Understanding Mean, Median, and Skewness:
# 
# You inquired about the relationships between mean and median concerning left and right skewness. We discussed how in right-skewed distributions, the mean is typically greater than the median, while in left-skewed distributions, the mean is usually less than the median.
# 
# 2. Demonstrating Mean and Median Differences with Code:
# 
# You shared a code snippet using the scipy and plotly libraries to generate gamma-distributed data and visualize the differences between mean and median in skewed data. We discussed how the resulting plots illustrate the differences based on skewness.
# 
# 3. Applying Summary Statistics and Visualizations to a New Dataset:
# 
# You provided a dataset from a fast-food nutritional database and sought guidance on producing summary statistics and visualizations.
# I provided an example code that included data loading, summary statistics, and visualizations (histograms and box plots).
# 
# 4. Handling Errors in Code:
# 
# You encountered a ValueError related to column naming and data types. We addressed the error by ensuring the correct column names were used and then converting relevant columns to numeric types while handling non-numeric entries.
# After implementing data cleaning steps, we adjusted the code to visualize and analyze the data effectively.
# 
# 5. Final Adjustments and Conclusion:
# 
# I provided updated code that included data type conversions, NaN handling, and visualizations to facilitate a comprehensive analysis of the nutritional data, along with skewness calculations.
# 
# LinK: https://chatgpt.com/share/66f627bc-3980-8003-bf97-cfb022e6585e

# #### 7. Watch the classic [Gapminder Video](https://www.youtube.com/watch?v=jbkSRLYSojo), then have a look at the [`plotly` version](https://plotly.com/python/animations/) and recreate the animation (perhaps after optionally exploring and changing the [style](https://plotly.com/python/templates/), if you wish)

# In[32]:


get_ipython().system('pip install plotly pandas')

import plotly.express as px
import pandas as pd

df = pd.DataFrame({
    "year": [2000, 2001, 2002, 2003, 2004] * 3,
    "country": ["USA", "USA", "USA", "USA", "USA", "Canada", "Canada", "Canada", "Canada", "Canada", "Mexico", "Mexico", "Mexico", "Mexico", "Mexico"],
    "gdpPercap": [40000, 41000, 42000, 43000, 44000, 35000, 35500, 36000, 36500, 37000, 20000, 21000, 22000, 23000, 24000],
    "population": [300, 310, 320, 330, 340, 30, 31, 32, 33, 34, 100, 110, 120, 130, 140]
})

fig = px.scatter(
    df,
    x="gdpPercap",
    y="population",
    animation_frame="year",
    animation_group="country",
    size="population",
    color="country",
    hover_name="country",
    log_x=True,
    size_max=60,
    range_y=[0, 400],
    title="GDP per Capita vs. Population Over Time"
)

fig.show()


# 

# In[ ]:





# #### 8. Provide a second version of the figure from the previous problem where you edit the `fig = px.scatter()` function from the Gapminder code so that `x` is "percent change", `y` is "rank", `size` is "percent", and `color`="sex", `animation_frame` is "year", and `animation_group` and `hover_name` are "name". Then use `size_max=50`, `range_x=[-0.005,0.005])` and remove the `log_x=True` and `range_y` parameters
# 
# > ```python
# > bn = pd.read_csv('https://raw.githubusercontent.com/hadley/data-baby-names/master/baby-names.csv')
# > bn['name'] = bn['name']+" "+bn['sex'] # make identical boy and girl names distinct
# > bn['rank'] = bn.groupby('year')['percent'].rank(ascending=False)
# > bn = bn.sort_values(['name','year'])
# > # the next three lines create the increaes or decrease in name prevalence from the last year 
# > bn['percent change'] = bn['percent'].diff()
# > new_name = [True]+list(bn.name[:-1].values!=bn.name[1:].values)
# > bn.loc[new_name,'percentage change'] = bn.loc[new_name,'percent'] 
# > bn = bn.sort_values('year')
# > bn = bn[bn.percent>0.001] # restrict to "common" names
# > fig = px.scatter(bn, x="", y="", animation_frame="", animation_group="",
# >                  size="", color="", hover_name="",size_max=50, range_x=[-0.005,0.005]) # range_y removed
# > fig.update_yaxes(autorange='reversed') # this lets us put rank 1 on the top
# > fig.show(renderer="png") # USE `fig.show(renderer="png")` FOR ALL GitHub and MarkUs SUBMISSIONS
# > ```
# 

# In[34]:


import plotly.express as px
import pandas as pd

df = pd.DataFrame({
    "year": [2000, 2001, 2002, 2003, 2004] * 3,
    "name": ["Country A", "Country B", "Country C"] * 5,
    "percent change": [0.001, 0.002, -0.003, 0.004, 0.002, 0.003, 0.007, 0.001, 0.006, 0.005, 0.008, 0.009, -0.001, 0.002, 0.003],
    "rank": [1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3],
    "percent": [50, 60, 55, 65, 70, 75, 80, 85, 90, 95, 100, 105, 110, 115, 120],
    "sex": ["Male", "Female", "Male", "Female", "Male", "Female", "Male", "Female", "Male", "Female", "Male", "Female", "Male", "Female", "Male"]
})

fig = px.scatter(
    df,
    x="percent change",
    y="rank",
    size="percent",
    color="sex",
    animation_frame="year",
    animation_group="name",
    hover_name="name",
    size_max=50,               
    range_x=[-0.005, 0.005],   
    title="Percent Change vs. Rank Over Time"
)

fig.show()


# ChatBot summaries:
# 1. Initial Inquiry: You requested guidance on how to recreate an animation from a Plotly example, specifically seeking steps to create a similar animated scatter plot.
# 
# 2. Installation Guidance: I provided instructions to install the required libraries (plotly and pandas) and included a sample DataFrame for demonstration purposes.
# 
# 3. Code Example: I presented a basic example of how to create an animated scatter plot using Plotly, specifying parameters for the x-axis, y-axis, animation frames, marker size, and colors.
# 
# 4. Customization Request: You asked for modifications to the px.scatter() function to:
# 
# Set the x-axis to "percent change"
# Set the y-axis to "rank"
# Size the markers based on "percent"
# Color the markers by "sex"
# Use "year" for the animation frame
# Use "name" for animation grouping and hover names.
# 
# 5. Updated Code: I provided the modified code to reflect your specifications and included an example DataFrame structure.
# 
# 6. Further Modifications: You requested additional changes to the code:
# 
# Change size_max to 50
# Set the x-axis range to [-0.005, 0.005]
# Remove log_x=True and range_y parameters.
# 
# 7. Final Code Example: I delivered the complete code with all the requested modifications, ensuring that it met your requirements for the animated scatter plot.
# 
# Link:https://chatgpt.com/share/66f6264b-7100-8003-8a99-4779e361c65d

# #### 9. Have you reviewed the course [wiki-textbook](https://github.com/pointOfive/stat130chat130/wiki) and interacted with a ChatBot (or, if that wasn't sufficient, real people in the course piazza discussion board or TA office hours) to help you understand all the material in the tutorial and lecture that you didn't quite follow when you first saw it?<br><br>
#   
# <details class="details-example"><summary style="color:blue"><u>Further Guidance</u></summary>
#     
# > _Just answering "Yes" or "No" or "Somewhat" or "Mostly" or whatever here is fine as this question isn't a part of the rubric; but, the midterm and final exams may ask questions that are based on the tutorial and lecture materials; and, your own skills will be limited by your familiarity with these materials (which will determine your ability to actually do actual things effectively with these skills... like the course project...)_
#     
# </details>

# Somewhat

# # Recommended Additional Useful Activities [Optional]
# 
# The "Ethical Profesionalism Considerations" and "Current Course Project Capability Level" sections below **are not a part of the required homework assignment**; rather, they are regular weekly guides covering (a) relevant considerations regarding professional and ethical conduct, and (b) the analysis steps for the STA130 course project that are feasible at the current stage of the course
# 
# <br><details class="details-example"><summary style="color:blue"><u>Ethical Professionalism Considerations</u></summary>
# 
# ### Ethical Professionalism Considerations
# 
# |![](https://handsondataviz.org/images/14-detect/gdp-baseline-merged-annotated.png)|
# |-|
# | |
# 
# Mark Twain's statment that, "There are lies, damn lies, and statistics", reflects a general skepticism towards statistical analysis that has been reinforced through through popular books such as [How to Lie with Statistics](https://en.wikipedia.org/wiki/How_to_Lie_with_Statistics). One place "statistics" can be used to decieve is through misuse of charts.  As discussed [here](https://handsondataviz.org/how-to-lie-with-charts.html) and many other places, a primary tactic that can be used to give a misleading impression using a chart is the manipulation of axes or the addition of additional dimensions which distort the meaning of size. **What are the problems with the following graphs?**
# 
# |![](https://images.ctfassets.net/jicu8fwm4fvs/260tj0wxTFCAlbf4yTzSoy/2b002a49921831ab0dc05415616a1652/blog-misleading-gun-deaths-graph.jpeg)|![](https://photos1.blogger.com/blogger/5757/110/1600/macgraph.jpg)|
# |-|-|
# | | |
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
# At this point in the course you should be able to create a `for` loop to iterate through and provide **visualizations** of some of the interesting columns in the course project data
# 
# 1. Create a `for` loop with a **conditional logic structure** that appropriately controls the kind of visualization that gets made for a given column of data based on its data type
# 
# *Being able run your code with different subsets (of different types) of columns demonstrates the desirability of the programming design principle of "polymorphism" (which means "many uses") which states that code is best when it's "resuable" for different purposes... such as automatically providing the appropriate visualizations as interest in different variables dynamically changes...* 
#     
# </details>            
