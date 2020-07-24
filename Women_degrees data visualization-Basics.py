#!/usr/bin/env python
# coding: utf-8

# In[18]:


get_ipython().magic('matplotlib inline')
import pandas as pd
import matplotlib.pyplot as plt

women_degrees = pd.read_csv('percent-bachelors-degrees-women-usa.csv')
cb_dark_blue = (0/255,107/255,164/255)
cb_orange = (255/255, 128/255, 14/255)
stem_cats = ['Engineering', 'Computer Science', 'Psychology', 'Biology', 'Physical Sciences', 'Math and Statistics']

fig = plt.figure(figsize=(18, 3))

for sp in range(0,6):
    ax = fig.add_subplot(1,6,sp+1)
    ax.plot(women_degrees['Year'], women_degrees[stem_cats[sp]], c=cb_dark_blue, label='Women', linewidth=3)
    ax.plot(women_degrees['Year'], 100-women_degrees[stem_cats[sp]], c=cb_orange, label='Men', linewidth=3)
    ax.spines["right"].set_visible(False)    
    ax.spines["left"].set_visible(False)
    ax.spines["top"].set_visible(False)    
    ax.spines["bottom"].set_visible(False)
    ax.set_xlim(1968, 2011)
    ax.set_ylim(0,100)
    ax.set_title(stem_cats[sp])
    ax.tick_params(bottom="off", top="off", left="off", right="off")
    
    if sp == 0:
        ax.text(2005, 87, 'Men')
        ax.text(2002, 5, 'Women')
    elif sp == 5:
        ax.text(2005, 62, 'Men')
        ax.text(2001, 30, 'Women')
plt.show()


# # Put 17 line charts in one diagram

# In[17]:


stem_cats = ['Engineering', 'Computer Science', 'Psychology', 'Biology', 'Physical Sciences', 'Math and Statistics']
lib_arts_cats = ['Foreign Languages', 'English', 'Communications and Journalism', 'Art and Performance', 'Social Sciences and History']
other_cats = ['Health Professions', 'Public Administration', 'Education', 'Agriculture','Business', 'Architecture']

fig=plt.figure(figsize=(16,16))
#for stem_cats
for r in range(0,6):
    ax=fig.add_subplot(6,3,3*r+1)
    ax.plot(women_degrees['Year'],women_degrees[stem_cats[r]],c=cb_dark_blue, label='Women', linewidth=3)
    ax.plot(women_degrees['Year'],100-women_degrees[stem_cats[r]],c=cb_orange,label='Men',linewidth=3)
    for key,spine in ax.spines.items():
        spine.set_visible(False)
        ax.set_xlim(1968,2011)
        ax.set_ylim(0,100)
        ax.set_title(stem_cats[r])    
        ax.tick_params(bottom="off", top="off", left="off", right="off")
    if r==0:
        ax.text(2005,87,'Men')
        ax.text(2002,8,'Women')
    elif r==5:
        ax.text(2005,65,'Men')
        ax.text(2005,35,'Women')

#For lib_arts_cats
for r in range(0,5):
    ax=fig.add_subplot(6,3,3*r+2)
    ax.plot(women_degrees['Year'],women_degrees[lib_arts_cats[r]],c=cb_dark_blue,label='Women',linewidth=3)
    ax.plot(women_degrees['Year'],100-women_degrees[lib_arts_cats[r]],c=cb_orange,label='Men',linewidth=3)
    for key,spine in ax.spines.items():
        spine.set_visible(False)
        ax.set_xlim(1968,2011)
        ax.set_ylim(0,100)
        ax.set_title(lib_arts_cats[r])
        ax.tick_params(bottom="off", top="off", left="off", right="off")
    if r==0:
        ax.text(2005,20,'Men')
        ax.text(2005,80,'Women')
#For other_cats
for r in range(0,6):
    ax=fig.add_subplot(6,3,3*r+3)
    ax.plot(women_degrees['Year'],women_degrees[other_cats[r]],c=cb_dark_blue,label='Women',linewidth=3)
    ax.plot(women_degrees['Year'],100-women_degrees[other_cats[r]],c=cb_orange,label='Men',linewidth=3)
    for key,spine in ax.spines.items():
        spine.set_visible(False)
        ax.set_xlim(1968,2011)
        ax.set_ylim(0,100)
        ax.set_title(other_cats[r])
        ax.tick_params(bottom='off',top='off',left='off',right='off')
    if r==0:
        ax.text(2005,90,'Women')
        ax.text(2005,5,'Men')
    elif r==5:
        ax.text(2005,65,'Men')
        ax.text(2005,25,'Women')


# # Hiding X-axis Label

# In[19]:


#adding parame to ax.tick_params()
stem_cats = ['Engineering', 'Computer Science', 'Psychology', 'Biology', 'Physical Sciences', 'Math and Statistics']
lib_arts_cats = ['Foreign Languages', 'English', 'Communications and Journalism', 'Art and Performance', 'Social Sciences and History']
other_cats = ['Health Professions', 'Public Administration', 'Education', 'Agriculture','Business', 'Architecture']

fig=plt.figure(figsize=(16,16))
#for stem_cats
for r in range(0,6):
    ax=fig.add_subplot(6,3,3*r+1)
    ax.plot(women_degrees['Year'],women_degrees[stem_cats[r]],c=cb_dark_blue, label='Women', linewidth=3)
    ax.plot(women_degrees['Year'],100-women_degrees[stem_cats[r]],c=cb_orange,label='Men',linewidth=3)
    for key,spine in ax.spines.items():
        spine.set_visible(False)
        ax.set_xlim(1968,2011)
        ax.set_ylim(0,100)
        ax.set_title(stem_cats[r])    
        ax.tick_params(bottom="off", top="off", left="off", right="off",labelbottom='off')
    if r==0:
        ax.text(2005,87,'Men')
        ax.text(2002,8,'Women')
    elif r==5:
        ax.text(2005,65,'Men')
        ax.text(2005,35,'Women')

#For lib_arts_cats
for r in range(0,5):
    ax=fig.add_subplot(6,3,3*r+2)
    ax.plot(women_degrees['Year'],women_degrees[lib_arts_cats[r]],c=cb_dark_blue,label='Women',linewidth=3)
    ax.plot(women_degrees['Year'],100-women_degrees[lib_arts_cats[r]],c=cb_orange,label='Men',linewidth=3)
    for key,spine in ax.spines.items():
        spine.set_visible(False)
        ax.set_xlim(1968,2011)
        ax.set_ylim(0,100)
        ax.set_title(lib_arts_cats[r])
        ax.tick_params(bottom="off", top="off", left="off", right="off",labelbottom='off')
    if r==0:
        ax.text(2005,20,'Men')
        ax.text(2005,80,'Women')
#For other_cats
for r in range(0,6):
    ax=fig.add_subplot(6,3,3*r+3)
    ax.plot(women_degrees['Year'],women_degrees[other_cats[r]],c=cb_dark_blue,label='Women',linewidth=3)
    ax.plot(women_degrees['Year'],100-women_degrees[other_cats[r]],c=cb_orange,label='Men',linewidth=3)
    for key,spine in ax.spines.items():
        spine.set_visible(False)
        ax.set_xlim(1968,2011)
        ax.set_ylim(0,100)
        ax.set_title(other_cats[r])
        ax.tick_params(bottom='off',top='off',left='off',right='off',labelbottom='off')
    if r==0:
        ax.text(2005,90,'Women')
        ax.text(2005,5,'Men')
    elif r==5:
        ax.text(2005,65,'Men')
        ax.text(2005,25,'Women')


# # Setting y-axis label, only show 0 and 100

# In[20]:


#adding parame to ax.tick_params()
stem_cats = ['Engineering', 'Computer Science', 'Psychology', 'Biology', 'Physical Sciences', 'Math and Statistics']
lib_arts_cats = ['Foreign Languages', 'English', 'Communications and Journalism', 'Art and Performance', 'Social Sciences and History']
other_cats = ['Health Professions', 'Public Administration', 'Education', 'Agriculture','Business', 'Architecture']

fig=plt.figure(figsize=(16,16))
#for stem_cats
for r in range(0,6):
    ax=fig.add_subplot(6,3,3*r+1)
    ax.plot(women_degrees['Year'],women_degrees[stem_cats[r]],c=cb_dark_blue, label='Women', linewidth=3)
    ax.plot(women_degrees['Year'],100-women_degrees[stem_cats[r]],c=cb_orange,label='Men',linewidth=3)
    for key,spine in ax.spines.items():
        spine.set_visible(False)
        ax.set_xlim(1968,2011)
        ax.set_ylim(0,100)
        ax.set_title(stem_cats[r])    
        ax.tick_params(bottom="off", top="off", left="off", right="off",labelbottom='off')
        ax.set_yticks([0,100])
    if r==0:
        ax.text(2005,87,'Men')
        ax.text(2002,8,'Women')
    elif r==5:
        ax.text(2005,65,'Men')
        ax.text(2005,35,'Women')

#For lib_arts_cats
for r in range(0,5):
    ax=fig.add_subplot(6,3,3*r+2)
    ax.plot(women_degrees['Year'],women_degrees[lib_arts_cats[r]],c=cb_dark_blue,label='Women',linewidth=3)
    ax.plot(women_degrees['Year'],100-women_degrees[lib_arts_cats[r]],c=cb_orange,label='Men',linewidth=3)
    for key,spine in ax.spines.items():
        spine.set_visible(False)
        ax.set_xlim(1968,2011)
        ax.set_ylim(0,100)
        ax.set_title(lib_arts_cats[r])
        ax.tick_params(bottom="off", top="off", left="off", right="off",labelbottom='off')
        ax.set_yticks([0,100])
    if r==0:
        ax.text(2005,20,'Men')
        ax.text(2005,80,'Women')
#For other_cats
for r in range(0,6):
    ax=fig.add_subplot(6,3,3*r+3)
    ax.plot(women_degrees['Year'],women_degrees[other_cats[r]],c=cb_dark_blue,label='Women',linewidth=3)
    ax.plot(women_degrees['Year'],100-women_degrees[other_cats[r]],c=cb_orange,label='Men',linewidth=3)
    for key,spine in ax.spines.items():
        spine.set_visible(False)
        ax.set_xlim(1968,2011)
        ax.set_ylim(0,100)
        ax.set_title(other_cats[r])
        ax.tick_params(bottom='off',top='off',left='off',right='off',labelbottom='off')
        ax.set_yticks([0,100])
    if r==0:
        ax.text(2005,90,'Women')
        ax.text(2005,5,'Men')
    elif r==5:
        ax.text(2005,65,'Men')
        ax.text(2005,25,'Women')


# # Add a axhline to show 50-50 Top and Bottom

# In[21]:


#adding parame to ax.tick_params()
stem_cats = ['Engineering', 'Computer Science', 'Psychology', 'Biology', 'Physical Sciences', 'Math and Statistics']
lib_arts_cats = ['Foreign Languages', 'English', 'Communications and Journalism', 'Art and Performance', 'Social Sciences and History']
other_cats = ['Health Professions', 'Public Administration', 'Education', 'Agriculture','Business', 'Architecture']

fig=plt.figure(figsize=(16,16))
#for stem_cats
for r in range(0,6):
    ax=fig.add_subplot(6,3,3*r+1)
    ax.plot(women_degrees['Year'],women_degrees[stem_cats[r]],c=cb_dark_blue, label='Women', linewidth=3)
    ax.plot(women_degrees['Year'],100-women_degrees[stem_cats[r]],c=cb_orange,label='Men',linewidth=3)
    for key,spine in ax.spines.items():
        spine.set_visible(False)
        ax.set_xlim(1968,2011)
        ax.set_ylim(0,100)
        ax.set_title(stem_cats[r])    
        ax.tick_params(bottom="off", top="off", left="off", right="off",labelbottom='off')
        ax.set_yticks([0,100])
        ax.axhline(50, c=(171/255, 171/255, 171/255), alpha=0.3)
    if r==0:
        ax.text(2005,87,'Men')
        ax.text(2002,8,'Women')
    elif r==5:
        ax.text(2005,65,'Men')
        ax.text(2005,35,'Women')

#For lib_arts_cats
for r in range(0,5):
    ax=fig.add_subplot(6,3,3*r+2)
    ax.plot(women_degrees['Year'],women_degrees[lib_arts_cats[r]],c=cb_dark_blue,label='Women',linewidth=3)
    ax.plot(women_degrees['Year'],100-women_degrees[lib_arts_cats[r]],c=cb_orange,label='Men',linewidth=3)
    for key,spine in ax.spines.items():
        spine.set_visible(False)
        ax.set_xlim(1968,2011)
        ax.set_ylim(0,100)
        ax.set_title(lib_arts_cats[r])
        ax.tick_params(bottom="off", top="off", left="off", right="off",labelbottom='off')
        ax.set_yticks([0,100])
        ax.axhline(50, c=(171/255, 171/255, 171/255), alpha=0.3)
    if r==0:
        ax.text(2005,20,'Men')
        ax.text(2005,80,'Women')
#For other_cats
for r in range(0,6):
    ax=fig.add_subplot(6,3,3*r+3)
    ax.plot(women_degrees['Year'],women_degrees[other_cats[r]],c=cb_dark_blue,label='Women',linewidth=3)
    ax.plot(women_degrees['Year'],100-women_degrees[other_cats[r]],c=cb_orange,label='Men',linewidth=3)
    for key,spine in ax.spines.items():
        spine.set_visible(False)
        ax.set_xlim(1968,2011)
        ax.set_ylim(0,100)
        ax.set_title(other_cats[r])
        ax.tick_params(bottom='off',top='off',left='off',right='off',labelbottom='off')
        ax.set_yticks([0,100])
        ax.axhline(50, c=(171/255, 171/255, 171/255), alpha=0.3)
    if r==0:
        ax.text(2005,90,'Women')
        ax.text(2005,5,'Men')
    elif r==5:
        ax.text(2005,65,'Men')
        ax.text(2005,25,'Women')


# In[ ]:




