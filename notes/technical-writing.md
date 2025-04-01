# Technical Writing

## Course Summary

| Title and course details | Summary | Pre-Class | In-Class |
| --- | --- | --- | --- |
| [Technical Writing One](https://developers.google.com/tech-writing/one) | Learn the critical basics of technical writing. Take this course before taking any of the other courses. | 2 hours | 2 to 2.5 hours |
| [Technical Writing Two](https://developers.google.com/tech-writing/two) | Practice four intermediate topics in technical writing. | 1 hour | 2 to 2.5 hours |
| [Tech Writing for Accessibility](https://developers.google.com/tech-writing/accessibility) | Develop skills for making documentation more accessible to all. | none | 1.5 hours |
| [Writing Helpful Error Messages](https://developers.google.com/tech-writing/error-messages) | Write clearer, more effective error messages, whether they appear in IDEs, command lines, or GUIs. This course is online only. | 1.5 hours | none |

# Technical Writing One

## Introduction

Technical Writing One teaches you how to write clearer technical documentation.

## Target audience

You need at least a little writing proficiency in English, but you don't need to be a strong writer to take this course.

If you've never taken any technical writing training, this course is perfect for you. If you've taken technical writing training, this class provides an efficient refresher.

## Learning objectives

This course teaches you the fundamentals of technical writing. After completing this class, you will know how to do the following:

- Use terminology—including abbreviations and acronyms—consistently.
- Recognize ambiguous pronouns.
- Distinguish active voice from passive voice.
- Convert passive voice sentences to active voice.
- Identify three ways in which active voice is superior to passive voice.
- Develop at least three strategies to make sentences clearer and more engaging.
- Develop at least four strategies to shorten sentences.
- Understand the difference between bulleted lists and numbered lists.
- Create helpful lists.
- Create effective lead sentences for paragraphs.
- Focus each paragraph on a single topic.
- State key points at the start of each document.
- Identify your target audience.
- Determine what your target audience already knows and what your target audience needs to learn.
- Understand the curse of knowledge.
- Identify and revise idioms.
- State your document's scope (goals) and audience.
- Break long topics into appropriate sections.
- Use commas, parentheses, colons, em dashes, and semicolons properly.
- Develop beginner competency in Markdown.

## Just enough grammar

| Part of Speech | Definition | Example |
| --- | --- | --- |
| Noun | A person, place, concept, or thing | **Sam** runs **races**. |
| Pronoun | A noun that replaces another noun (or larger structure) | Sam runs races. **He** likes to compete. |
| Adjective | A word or phrase that modifies a noun | Sam wears **blue** shoes. |
| Verb | An action word or phrase | Sam **runs** races. |
| Adverb | A word or phrase that modifies a verb, an adjective, or another adverb | Sam runs **slowly**. |
| Preposition | A word or phrase specifying the positional relationship of two nouns | Sam's sneakers are seldom **on** his shelf. |
| Conjunction | A word that connects two nouns or phrases | Sam's trophies **and** ribbons live only in his imagination. |
| Transition | A word or phrase that connects two sentences | Sam runs races weekly. **However**, he finishes races weakly. |

## Words

### Define new or unfamiliar terms

When writing or editing, learn to recognize terms that might be unfamiliar to some or all of your target audience. When you spot such a term, take one of the following two tactics:

- If the term already exists, link to a good existing explanation. (Don't reinvent the wheel.)
- If your document is introducing the term, define the term. If your document is introducing many terms, collect the definitions into a glossary.

### Use terms consistently

The moral: apply the same unambiguous word or term consistently throughout your document. Once you've named a component **thingy**, don't rename it **thingamabob**.

Namely, when introducing a long-winded concept name or product name, you may also specify a shortened version of that name. Then, you may use that shortened name throughout the document.

### Use acronyms propertly

On the initial use of an unfamiliar acronym within a document or a section, spell out the full term, and then put the acronym in parentheses. Put both the spelled-out version and the acronym in boldface.

You may then use the acronym going forward.

Do not cycle back-and-forth between the acronym and the expanded version in the same document.

Here are the guidelines for acronyms:

- Don't define acronyms that would only be used a few times.
- Do define acronyms that meet both of the following criteria:
    - The acronym is significantly shorter than the full term.
    - The acronym appears many times in the document.

### Recognize ambiguous pronouns

Consider the following pronoun guidelines:

- Only use a pronoun *after* you've introduced the noun; never use the pronoun before you've introduced the noun.
- Place the pronoun as close as possible to the referring noun. In general, if more than five words separate your noun from your pronoun, consider repeating the noun instead of using the pronoun.
- If you introduce a second noun between your noun and your pronoun, reuse your noun instead of using a pronoun.

## Active voice vs. passive voice

### Distinguish active voice from passive voice

In an active voice sentence, an actor acts on a target. That is, an active voice sentence follows this formula:

```tsx
Active Voice Sentence = actor + verb + target
```

A passive voice sentence reverses the formula. That is, a passive voice sentence typically follows the following formula:

```tsx
Passive Voice Sentence = target + verb + actor
```

Consider the following example:

```tsx
Active voice: The cat sat on the mat.
Passive voice: The mat was sat on by the cat.
```

Good sentences in technical documentation identify who is doing what to whom.

### Recognize passive verbs

Passive verbs typically have the following formula:

```
passive verb = form of be + past participle verb
```

Although the preceding formula looks daunting, it is actually pretty simple:

- A **form of *be*** in a passive verb is typically one of the following words:
    - is/are
    - was/were
- A **past participle verb** is typically a plain verb plus the suffix *ed*. For example, the following are past participle verbs:
    - interpreted
    - generated
    - formed

## Clear sentences

In technical writing, clarity takes precedence over all other rules. This unit suggests a few ways to make your sentences beautifully clear.

### Choose strong verbs

Many technical writers believe that the verb is the most important part of a sentence. Pick the right verb and the rest of the sentence will take care of itself. Unfortunately, some writers reuse only a small set of mild verbs, which is like serving your guests stale crackers and soggy lettuce every day. Picking the right verb takes a little more time but produces more satisfying results.

### Reduce there is / there are

Sentences that start with **There is** or **There are** marry a generic noun to a generic verb. Generic weddings bore readers. Show true love for your readers by providing a real subject and a real verb.

### Minimize certain adjectives and adverbs

Adjectives and adverbs perform amazingly well in fiction and poetry. Thanks to adjectives, plain old grass becomes **prodigal** and **verdant**, while lifeless hair transforms into something **lustrous** and **exuberant**. Adverbs push horses to run **madly** and **freely** and dogs to bark **loudly** and **ferociously**. Unfortunately, adjectives and adverbs sometimes make technical readers bark loudly and ferociously. That's because adjectives and adverbs tend to be too loosely defined and subjective for technical readers. Worse, adjectives and adverbs can make technical documentation sound dangerously like marketing material.

## Short sentences

Software engineers generally try to minimize the number of lines of code in an implementation for the following reasons:

- Shorter code is typically easier for others to read.
- Shorter code is typically easier to maintain than longer code.
- Extra lines of code introduce additional points of failure.

In fact, the same rules apply to technical writing:

- Shorter documentation reads faster than longer documentation.
- Shorter documentation is typically easier to maintain than longer documentation.
- Extra lines of documentation introduce additional points of failure.

Finding the shortest documentation implementation takes time but is ultimately worthwhile. Short sentences communicate more powerfully than long sentences, and short sentences are usually easier to understand than long sentences.

### Focus each sentence on a single idea

Focus each sentence on a single idea, thought, or concept. Just as statements in a program execute a single task, sentences should execute a single idea. 

### Convert some long sentences to lists

When you see the conjunction **or** in a long sentence, consider refactoring that sentence into a bulleted list. When you see an embedded list of items or tasks within a long sentence, consider refactoring that sentence into a bulleted or numbered list.

### Eliminate or reduce extraneous words

The following table suggests replacements for a few common bloated phrases:

| Wordy | Concise |
| --- | --- |
| at this point in time | now |
| determine the location of | find |
| is able to | can |

### Reduce subordinate clauses

A **clause** is an independent logical fragment of a sentence, which contains an actor and an action. Every sentence contains the following:

- A main clause
- Zero or more subordinate clauses

Subordinate clauses modify the idea in the main clause. As the name implies, subordinate clauses are less important than the main clause.

You can usually identify subordinate clauses by the words that introduce them. The following list (by no means complete) shows common words that introduce subordinate clauses:

- which
- that
- because
- whose
- until
- unless
- since

### Distinguish that from which

**That** and **which** both introduce subordinate clauses. What's the difference between them? Well, in some countries, the two words are pretty much interchangeable. Inevitably though, alert readers from the United States will angrily announce that you confused the two words again.

In the United States, reserve **which** for nonessential subordinate clauses, and use **that** for an essential subordinate clause that the sentence can't live without.

## Lists and tables

Good lists can transform technical chaos into something orderly. Technical readers generally love lists. Therefore, when writing, seek opportunities to convert prose into lists.

### Choose the correct type of list

The following types of lists dominate technical writing:

- Bulleted lists
- Numbered lists
- Embedded lists

Use a **bulleted list** for *unordered* items; use a **numbered list** for *ordered* items. In other words:

- If you rearrange the items in a *bulleted* list, the list's meaning does not change.
- If you rearrange the items in a *numbered* list, the list's meaning *changes*.

An **embedded list** (sometimes called a **run-in** list) contains items stuffed within a sentence.

Generally speaking, embedded lists are a poor way to present technical information. Try to transform embedded lists into either bulleted lists or numbered lists.

### Keep list items parallel

Effective lists are parallel; defective lists tend to be nonparallel. All items in a **parallel** list look like they "belong" together. That is, all items in a parallel list match along the following parameters:

- Grammar
- Logical category
- Capitalization
- Punctuation

Conversely, at least one item in a **nonparallel** list fails at least one of the preceding consistency checks.

### Start numbered list items with imperative verbs

Consider starting all items in a numbered list with an imperative verb. An **imperative verb** is a command, such as **open** or **start**. For example, notice how all of the items in the following parallel numbered list begin with an imperative verb:

1. Download the Frambus app from Google Play or iTunes.
2. Configure the Frambus app's settings.
3. Start the Frambus app.

### Punctuate items appropriately

Though different style guides offer conflicting advice about punctuating list items, the [Google developer documentation style guide](https://developers.google.com/style/lists#capitalization-and-end-punctuation) recommends (with some exceptions) starting each list item with a capital letter.

If a list item is a sentence, use appropriate sentence-ending punctuation. 

### Create useful tables

Analytic minds tend to love tables. Given a page containing multiple paragraphs and a single table, engineers' eyes zoom towards the table.

Consider the following guidelines when creating tables:

- Label each column with a meaningful header. Don't make readers guess what each column holds.
- Avoid putting too much text into a table cell. If a table cell holds more than two sentences, ask yourself whether that information belongs in some other format.
- Although different columns can hold different types of data, strive for parallelism *within* individual columns. For instance, the cells within a particular table column should not be a mixture of numerical data and famous circus performers.

### Introduce each list and table

We recommend introducing each list and table with a sentence that tells readers what the list or table represents. In other words, give the list or table context. Terminate the introductory sentence with a colon rather than a period.

Although not a requirement, we recommend putting the word **following** into the introductory sentence

## Paragraphs

The work of writing is *simply* this: untangling the dependencies among the parts of a topic, and presenting those parts in a logical stream that enables the reader to understand you.

### Write a great opening sentence

The opening sentence is the most important sentence of any paragraph. Busy readers focus on opening sentences and sometimes skip over subsequent sentences. Therefore, focus your writing energy on opening sentences.

Good opening sentences establish the paragraph's central point.

### Focus each paragraph on a single topic

A paragraph should represent an independent unit of logic. Restrict each paragraph to the current topic. Don't describe what will happen in a future topic or what happened in a past topic. When revising, ruthlessly delete (or move to another paragraph) any sentence that doesn't directly relate to the current topic.

### Don’t make paragraphs too long or too short

Long paragraphs are visually intimidating. *Very* long paragraphs form a dreaded "wall of text" that readers ignore. Readers generally welcome paragraphs containing three to five sentences, but will avoid paragraphs containing more than about seven sentences. When revising, consider dividing very long paragraphs into two separate paragraphs.

Conversely, don't make paragraphs too short. If your document contains plenty of one-sentence paragraphs, your organization is faulty. Seek ways to combine those one-sentence paragraphs into cohesive multi-sentence paragraphs or possibly into lists.

### Answer what, why and how

Good paragraphs answer the following three questions:

1. **What** are you trying to tell your reader?
2. **Why** is it important for the reader to know this?
3. **How** should the reader use this knowledge? Alternatively, how should the reader know your point to be true?

## Audience

The course designers believe that you are probably comfortable with mathematics. Therefore, this unit begins with an equation:

> good documentation = knowledge and skills your audience needs to do a task − your audience's current knowledge and skills
> 

In other words, make sure your document provides the information that your audience needs but doesn't already have. Therefore, this unit explains how to do the following:

- Define your audience.
- Determine what your audience needs to learn.
- Fit documentation to your audience.

### Define your audience

Serious documentation efforts spend considerable time and energy on defining their audience. These efforts might involve surveys, user experience studies, focus groups, and documentation testing. You probably don't have that much time, so this unit takes a simpler approach.

Begin by identifying your audience's **role**(s). Sample roles include:

- Software engineers
- Technical, non-engineer roles (such as technical program managers)
- Scientists
- Professionals in scientific fields (for example, physicians)
- Undergraduate engineering students
- Graduate engineering students
- Non-technical positions

Roles, by themselves, are insufficient for defining an audience. That is, you must also consider your audience's *proximity* to the knowledge. The software engineers in Project Frombus know something about related Project Dingus but nothing about unrelated Project Carambola. The average heart specialist knows more about ear problems than the average software engineer but far less than an audiologist.

Time also affects proximity. Almost all software engineers, for example, studied calculus. However, most software engineers don't use calculus in their jobs, so their knowledge of calculus gradually fades. Conversely, experienced engineers typically know vastly more about their current project than new engineers on the same project.

### Determine what your audience needs to learn

Write down a list of everything your target audience needs to learn to accomplish goals. In some cases, the list should hold tasks that the target audience needs to *perform*.

Note that your audience must sometimes master tasks in a certain order. 

If you are writing a design spec, then your list should focus on information your target audience should learn rather than on mastering specific tasks

### Fit documentation to your audience

Writing to meet your audience's needs requires unselfish empathy. You must create explanations that satisfy your audience's curiosity rather than your own. How do you step out of yourself in order to fit documentation to the audience? Unfortunately, we can offer no easy answers. We can, however, offer a few parameters to focus on.

- Match your vocabulary to your audience
- Experts often suffer from the curse of knowledge, which means that their expert understanding of a topic ruins their exaplanations to newcomers.
- Prefer simple overs over complex words
- Keep your writing culturally neutral. Do not require readers to understand the intricacies of NASCAR, cricket, or sumo in order to understand how a piece of software works.

## Documents

You can write sentences. You can write paragraphs. Can you organize all those paragraphs into a coherent document?

### State your document’s scope

A good document begins by defining its scope. A better document additionally defines its non-scope—the topics not covered that the target audience might reasonably expect your document to cover.

Scope and non-scope statements benefit not only the reader but also the writer (you). While writing, if the contents of your document veer away from the scope statement (or venture *into* the non-scope statement), then you must either refocus your document or modify your scope statement. When reviewing your first draft, delete any sections that don't help satisfy the scope statement.

### State your audience

A good document explicitly specifies its audience. Beyond the audience's role, a good audience declaration might also specify any prerequisite knowledge or experience.

In some cases, the audience declaration should also specify prerequisite reading or coursework.

### Summarize key points at the start

Engineers and scientists are busy people who won't necessarily read all 76 pages of your design document. Imagine that your peers might only read the first paragraph of your document. Therefore, ensure that the start of your document answers your readers' essential questions.

Professional writers focus considerable energy on page one to increase the odds of readers making it to page two. However, the start of any long document is the hardest page to write. Be prepared to revise page one many times.

### Write for your audience

**Define your audience’s needs**

Answering the following questions helps you determine what your document should contain:

- Who is your target audience?
- What is your target audience's goal? Why are they reading this document?
- What do your readers already know *before* they read your document?
- What should your readers know or be able to do *after* they read your document?

**Organize the document to meet your audience’s needs**

After defining the audience's needs, organize the document to help readers get the information they need.

## Punctuation

### Commas

In English, by contrast, the rules regarding commas are somewhat hazier. As a guideline, insert a comma wherever a reader would naturally pause somewhere within a sentence. 

Some situations *require* a comma.

You might be wondering about a list's final comma, the one inserted between items N-1 and N. This comma—known as the **serial comma** or **Oxford comma**—is controversial. We recommend supplying that final comma simply because technical writing requires picking the least ambiguous solution.

In sentences that express a condition, place a comma between the condition and the consequence.

Finally, avoid using a comma to paste together two independent thoughts.

### Semicolons

A period separates distinct thoughts; a semicolon unites highly related thoughts.

Before using a semicolon, ask yourself whether the sentence would still make sense if you flipped the thoughts to opposite sides of the semicolon.

The thoughts preceding and following the semicolon must each be grammatically complete sentences.

You should almost always use commas, not semicolons, to separate items in an embedded list.

### Em dashes

Em dashes are compelling punctuation marks, rich with punctuation possibilities. An em dash represents a longer pause—a bigger break—than a comma.

Consider the horizontal punctuation marks shown in the following table:

| Name | Mark | Relative width |
| --- | --- | --- |
| em dash | — | widest (usually, the length of the letter `m`) |
| en dash | – | medium (usually, the length of the letter `n`) |
| hyphen | - | narrowest |

### Colons

In technical writing, use a colon to alert readers that a list or table will follow. In other words, terminate the [sentence that introduces a list or table](https://developers.google.com/tech-writing/one/lists-and-tables#introduce_each_list_and_table) with a colon.

Technical writing prefers bulleted lists or numbered lists to embedded lists. That said, you can use a colon to introduce an embedded list.

### Parentheses

Use parentheses to hold minor points and digressions. Parentheses inform readers that the enclosed text isn't critical. Because the enclosed text isn't critical, some editors feel that text that deserves parentheses doesn't deserve to be in the document. As a compromise, keep parentheses to a minimum in technical writing.

The rules regarding periods and parentheses aren't always clear. Here are the standard rules:

- If a pair of parentheses holds an entire sentence, the period goes inside the closing parenthesis.
- If a pair of parentheses ends a sentence but does not hold the entire sentence, the period goes just outside the closing parenthesis.

## Markdown

**Markdown** is a lightweight markup language that many technical professionals use to create and edit technical documents. With Markdown, you write text in a plain text editor (such as vi or Emacs), inserting special characters to create headers, boldface, bullets, and so on.

A Markdown parser converts Markdown files into HTML. Browsers can then display the resulting HTML to readers.

We recommend becoming comfortable with Markdown by taking one of the following tutorials:

- [www.markdowntutorial.com](https://www.markdowntutorial.com/)
- [Mastering Markdown](https://guides.github.com/features/mastering-markdown/)

## Summary

- Use terms consistently.
- Avoid ambiguous pronouns.
- Prefer active voice to passive voice.
- Pick specific verbs over vague ones.
- Focus each sentence on a single idea.
- Convert some long sentences to lists.
- Eliminate unneeded words.
- Use a numbered list when ordering is important and a bulleted list when ordering is irrelevant.
- Keep list items parallel.
- Start numbered list items with imperative words.
- Introduce lists and tables appropriately.
- Create great opening sentences that establish a paragraph's central point.
- Focus each paragraph on a single topic.
- Determine what your audience needs to learn.
- Fit documentation to your audience.
- Establish your document's key points at the start of the document.

---

# Technical Writing Two introduction

*Technical Writing Two* helps technical people improve their technical communication skills.

## Target audience

We've aimed this course at people who have completed [Technical Writing One](https://developers.google.com/tech-writing/one) and are still hungry for more technical writing training. If you've never taken any technical writing training, we recommend completing *Technical Writing One* before taking this class.

## Learning objectives

This course focuses on several intermediate topics in technical writing. After completing this class, you will know how to do the following:

- Choose among several different tactics to write first drafts and additional tactics for writing second and third drafts.
- Use several techniques to detect mistakes in your own writing.
- Organize large documents.
- Introduce a document's scope and any prerequisites.
- Write clear figure captions.
- Pick the proper information density in technical illustrations.
- Focus the reader's attention in illustrations.
- Establish context through a "big picture" illustration.
- Revise technical illustrations effectively.
- Create useful, accurate, concise, clear, reusable, and well-commented sample code that demonstrates a range of complexity.
- Identify different documentation types.
- Describe just about anything.
- Empathize with a beginner audience and write a tutorial for them.

## Self-editing

The editing tips in this unit can help turn your first draft into a document that more clearly communicates the information your audience needs. Use one tip or use them all; the important thing is to find a strategy that works for you, and then make that strategy part of your writing routine.

### Adopt a style guide

Companies, organizations, and large open source projects frequently either adopt an existing style guide for their documentation or write their own. Many of the documentation projects on the [Google Developers](https://developers.google.com/) site follow the [Google Developer Documentation Style Guide](https://developers.google.com/style). If you've never relied on a style guide before, at first glance the Google Developer Documentation Style Guide might seem a little intimidating, offering detailed guidance on topics such as grammar, punctuation, formatting, and documenting computer interfaces. You might prefer to start by adopting the [style-guide highlights](https://developers.google.com/style/highlights).

Some of the guidelines listed in the highlights are covered in Technical Writing One. You might recall some of the following techniques:

- Use [active voice](https://developers.google.com/tech-writing/one/active-voice) to make clear who's performing the action.
- Format sequential steps as [numbered lists](https://developers.google.com/tech-writing/one/lists-and-tables).
- Format most other lists as bulleted lists.

The highlights introduce many other techniques that can be useful when writing technical documentation, such as:

- [Write in the second person](https://developers.google.com/style/person). Refer to your audience as "you", not "we".
- [Place conditions before instructions](https://developers.google.com/style/sentence-structure), not after.
- Format [code-related text as code font](https://developers.google.com/style/code-in-text).

### Think like your audience

Who is your audience? Step back and try to read your draft from their point of view. Make sure the purpose of your document is clear, and provide definitions for any terms or concepts that might be unfamiliar to your readers.

It can be helpful to outline a persona for your audience

You can then review your draft with your persona in mind. It can be especially useful to tell your audience about any assumptions you've made. You can also provide links to resources where they can learn more if they need to brush up on a specific topic.

Note that relying too heavily on a persona (or two) can result in a document that is too narrowly focused to be useful to the majority of your readers.

### Read it out loud

Depending on the context, the style of your writing can alienate, engage, or even bore your audience. The desired style of a given document depends to an extent on the audience. For example, the contributor guide for a new open source project aimed at recruiting volunteers might adopt a more informal and conversational style, while the developer guide for a commercial enterprise application might adopt a more formal style.

To check if your writing is conversational, read it out loud. Listen for awkward phrasing, too-long sentences, or anything else that doesn't feel natural. Alternatively, consider using a [screen reader](https://en.wikipedia.org/wiki/Screen_reader) to voice the content for you.

For more information on adjusting the style of your writing to suit your audience, see [Style and authorial tone](https://developers.google.com/style/tone).

### Come back to it later

After you write your first draft (or second or third), set it aside. Come back to it after an hour (or two or three) and try to read it with fresh eyes. You'll almost always notice something that you could improve.

### Change the context

Some writers like to print their documentation and review a paper copy, red pencil in hand. A change of context when reviewing your own work can help you find things to improve. For a modern take on this classic tip, copy your draft into a different document and change the font, size, and color.

### Find a peer editor

Just as engineers need peers to review their code, writers need editors to give them feedback on docs. Ask someone to review your document and give you specific, constructive comments. Your peer editor doesn't need to be a subject matter expert on the technical topic of your document, but they do need to be familiar with the style guide you follow.

## Organize large documents

How do you organize a large collection of information into a cohesive document or website? Alternatively, how do you reorganize an existing messy document or website into something approachable and useful? The following tactics can help:

- Choosing to write a single, large document or a set of documents
- Organizing a document
- Adding navigation
- Disclosing information progressively

### When to write large documents

You can organize a collection of information into longer standalone documents or a set of shorter interconnected documents. A set of shorter interconnected documents is often published as a website, wiki, or similar structured format.

Some readers respond more positively than others to longer documents.

So, should you organize your material into a single document or into a set of documents in a website? Consider the following guidelines:

- How-to guides, introductory overviews, and conceptual guides often work better as shorter documents when aimed at readers who are new to the subject matter. For example, a reader who is completely new to your subject matter might struggle to remember lots of new terms, concepts, and facts. Remember that your audience might be reading your documentation to gain a quick and general overview of the topic.
- In-depth tutorials, best practice guides, and command-line reference pages can work well as lengthier documents, especially when aimed at readers who already have some experience with the tools and subject matter.
- A great tutorial can rely on a narrative to lead the reader through a series of related tasks in a longer document. However, even large tutorials can sometimes benefit from being broken up into smaller parts.
- Many longer documents aren't designed to be read in one sitting. For example, users typically scan through a reference page to search for an explanation of a command or flag.

### Organize a document

This section suggests some techniques for planning a longer document, including creating an outline and drafting an introduction. After you've completed the first draft of a document, you can review it against your outline and introduction to make sure you haven't missed anything you originally intended to cover.

**Outline a document**

Starting with a structured, high-level outline can help you group topics and determine where more detail is needed. The outline helps you move topics around before you get down to writing.

You might find it useful to think of an outline as the narrative for your document. There is no standard approach to writing an outline, but the following guidelines provide practical tips you might find useful:

- Before you ask your reader to perform a task, explain to them why they are doing it. For example, the following bullet points illustrate a section of an outline from a tutorial about auditing and improving the accessibility of web pages:
    - Introduce a browser plugin that audits the accessibility of web pages; explain that the reader will use the results of the audit report to fix several bugs.
    - List the steps to run the plugin and audit the accessibility of a web page.
- Limit each step of your outline to describing a concept or completing a specific task.
- Structure your outline so that your document introduces information when it's most relevant to your reader. For example, your reader probably doesn't need to know (or want to know) about the history of the project in the introductory sections of your document when they're just getting started with the basics. If you feel the history of the project is useful, then include a link to this type of information at the end of your document.
- Consider explaining a concept and then demonstrating how the reader can apply it either in a sample project or in their own work. Documents that alternate between conceptual information and practical steps can be a particularly engaging way to learn.
- Before you start drafting, share the outline with your contributors. Outlines are especially useful if you're working with a team of contributors who are going to review and test your document.

**Outline exercise**

Review and update the following high-level outline of an introduction to a long tutorial. To solve this exercise, you can do any of the following:

- Rearrange the existing topics.
- Add any missing topics you feel should be in an introduction.
- Remove any topics you feel are irrelevant for an introduction.

**Introudce a document**

If readers of your documentation can't find relevance in the subject, they are likely to ignore it. To set the ground rules for your users, we recommend providing an introduction that includes the following information:

- What the document covers.
- What prior knowledge you expect readers to have.
- What the document doesn't cover.

Remember that you want to keep your documentation easy to maintain, so don't try to cover everything in the introduction.

After you've completed the first draft, check your entire document against the expectations you set in your overview. Does your introduction provide an accurate overview of the topics you cover? You might find it useful to think of this review as a form of documentation quality assurance (QA).

### Add navigation

Providing navigation and signposting for your readers ensures they can find what they are looking for and the information they need to get unstuck.

Clear navigation includes:

- introduction and summary sections
- a clear, logical development of the subject
- headings and subheadings that help users understand the subject
- a table of contents menu that shows users where they are in the document
- links to related resources or more in-depth information
- links to what to learn next

**Prefer task-based headings**

Choose a heading that describes the task your reader is working on. Avoid headings that rely on unfamiliar terminology or tools. For example, suppose you are documenting the process for creating a new website. To create the site, the reader must initialize the Froobus framework. To initialize the Froobus framework, the reader must run the `carambola` command-line tool. At first glance, it might seem logical to add either of the following headings to the instructions:

- Running the carambola command
- Initializing the Froobus framework

Unless your readers are already very experienced with the terminology and concepts for this topic, a more familiar heading might be preferable, such as *Creating the site*.

**Provide text under each heading**

Most readers appreciate at least a brief introduction under each heading to provide some context. Avoid placing a level three heading immediately after a level two heading.

### Disclose information progressively

Learning new concepts, ideas, and techniques can be a rewarding experience for many readers who are comfortable reading through documentation at their own pace. However, being confronted with too many new concepts and instructions too quickly can be overwhelming. Readers are more likely to be receptive to longer documents that progressively disclose new information to them when they need it. The following techniques can help you incorporate progressive disclosure in your documents:

- Where possible, try introducing new terminology and concepts near the instructions that rely on them.
- Break up large walls of text. To avoid multiple large paragraphs on a single page, aim to introduce tables, diagrams, lists, and headings where appropriate.
- Break up large series of steps. If you have a particularly long list of complicated steps, try to re-arrange them into shorter lists that explain how to complete sub-tasks.
- Start with simple examples and instructions, and add progressively more interesting and complicated techniques. For example, in a tutorial for creating forms, start by explaining how to handle text responses, and then introduce other techniques to handle multiple choice, images, and other response types.

## Illustrating

According to research by [Sung and Mayer (2012)](https://www.sciencedirect.com/science/article/pii/S0747563212000921), providing any graphics—good or bad—makes readers like the document more; however, only *instructive* graphics help readers learn. This unit suggests a few ways to help you create figures truly worth a thousand words.

### Write the caption first

It is often helpful to write the caption *before* creating the illustration. Then, create the illustration that best represents the caption. This process helps you to check that the illustration matches the goal.

Good captions have the following characteristics:

- They are **brief**. Typically, a caption is just a few words.
- They explain the **takeaway**. *After viewing this graphic, what should the reader remember?*
- They **focus** the reader's attention. Focus is particularly important when a photograph or diagram contains a lot of detail.

### Constrain the amount of information in a single drawing

Few intellectual tasks can be quite as rewarding as studying a fine painting, gradually uncovering layers of insight and meaning. People pay good money to do exactly that in the world's art museums.

### Focus the reader’s attention

**Callouts** provide another way to focus the reader's attention. For pictures and line art, a callout helps our eyes find just the right spot to land on. Callouts in pictures are often better than paragraph long explanations of the pictures because callouts focus the reader's attention on the most important aspects of the picture. Then, in your explanation, you can focus directly on the relevant part of the diagram, rather than spending time describing what part of the image you are talking about.

### Illustrating is re-illustrating

As with writing, the first draft of an illustration is seldom good enough. Revise your illustrations to clarify the content. As you revise, ask yourself the following questions:

- How can I simplify the illustration?
- Should I split this illustration into two or more simpler illustrations?
- Is the text in the illustration easy to read? Does the text contrast sufficiently with its background?
- What's the takeaway?

### Illustration tools

There are many options available for creating diagrams. Three options that are free or have free options include:

- [Google Drawings](https://drawings.google.com/)
- [diagrams.net](https://diagrams.net/)
- [LucidChart](https://www.lucidchart.com/pages/)

## Creating sample code

Good sample code is often the best documentation. Even if your paragraphs and lists are as clear as blue water, programmers still prefer good sample code. After all, text and code are different languages, and it is code that the reader ultimately cares about. Trying to describe code with text is like trying to explain an Italian poem in English.

Good samples are **correct** and **concise** code that your readers can **quickly understand** and **easily reuse** with **minimal side effects**.

### Correct

Sample code should meet the following criteria:

- Build without errors.
- Perform the task it claims to perform.
- Be as production-ready as possible. For example, the code shouldn't contain any security vulnerabilities.
- Follow language-specific conventions.

Sample code is an opportunity to directly influence how your users write code. Therefore, sample code should set the best way to use your product. If there is more than one way to code the task, code it in the manner that your team has decided is best. If your team hasn't considered the pros and cons of each approach, take time to do so.

Always test your sample code. Over time, systems change and your sample code may break. Be prepared to test and maintain sample code as you would any other code.

Many teams reuse their unit tests as sample programs, which is sometimes a bad idea. The primary goal of a unit test is to test; the only goal of a sample program is to educate.

A **snippet** is a piece of a sample program, possibly only one or a few lines long. Snippet-heavy documentation often degrades over time because teams tend not to test snippets as rigorously as full sample programs.

Writers should consider describing the expected output or result of sample code, especially for sample code that is difficult to run.

### Concise

Sample code should be short, including only essential components. When a novice C programmer wants to learn how to call the `malloc` function, give that programmer a brief snippet, not the entire Linux source tree. Irrelevant code can distract and confuse your audience. That said, never use bad practices to shorten your code; always prefer correctness over conciseness.

### Understandable

Follow these recommendations to create clear sample code:

- Pick descriptive class, method, and variable names.
- Avoid confusing your readers with hard-to-decipher programming tricks.
- Avoid deeply nested code.
- Optional: Use bold or colored font to draw the reader's attention to a specific section of your sample code. However, use highlighting judiciously—too much highlighting means the reader won't focus on anything in particular.

### Commented

Consider the following recommendations about comments in sample code:

- Keep comments short, but always prefer clarity over brevity.
- Avoid writing comments about *obvious* code, but remember that what is obvious to you (the expert) might not be obvious to newcomers.
- Focus your commenting energy on anything non-intuitive in the code.
- When your readers are very experienced with a technology, don't explain *what* the code is doing, explain *why* the code is doing it.

### Reusable

For your reader to easily reuse your sample code, provide the following:

- All information necessary to run the sample code, including any dependencies and setup.
- Code that can be extended or customized in useful ways.

### Sequenced

A good sample code set demonstrates **a range of complexity**.

Readers completely unfamiliar with a certain technology typically crave simple examples to get started. The first and most basic example in a sample code set is usually termed a [Hello World program](https://wikipedia.org/wiki/%22Hello,_World!%22_program). After mastering the basics, engineers want more complex programs. A good set of sample code provides a healthy range of simple, moderate, and complex sample programs.

## Summary

Technical Writing Two covered the following intermediate lessons of technical writing:

- Adopt a style guide.
- Think like your audience.
- Read documents out loud (to yourself).
- Return to documents well after you've written the draft.
- Find a good peer editor.
- Outline a document. Alternatively, write free form and then organize.
- Introduce a document's scope and any prerequisites.
- Prefer task-based headings.
- Disclose information progressively (in some situations).
- Consider writing the caption *before* creating the illustration.
- Constrain the amount of information in a single drawing.
- Focus the reader's attention on the relevant part of a picture or diagram by describing the takeaway in the caption or by adding a visual cue to the picture.
- Create concise sample code that is easy to understand.
- Keep code comments short, but prefer clarity over brevity.
- Avoid writing comments about *obvious* code.
- Focus your commenting energy on anything non-intuitive in the code.
- Provide not only examples but also anti-examples.
- Provide code samples that demonstrate a range of complexity.
- Make a practice of continuous revision.
- Provide different documentation types for different categories of users.
- Compare and contrast with something that readers are already familiar with.
- In tutorials, reinforce concepts with examples.
- In tutorials, note problems that readers may encounter.

---

# Tech Writing for Accessibility

Our mission statement is to organize the world's information and make it universally accessible and useful. Take this course to learn how to make your documents more accessible for everyone, including people with disabilities. For example, this courses teaches you how to create documentation and websites for screen reader users.

This course is available in the following two formats:

- Instructor-led, which this page describes.
- [Self-study](https://developers.google.com/tech-writing/accessibility/self-study)

Both formats cover similar, though not identical, content.

## Target audience

We've aimed this course at the following roles:

- engineers
- product managers and technical program managers
- technical writers
- anyone else who writes or reviews documents

## Learning objectives

After taking this course, you will know how to do the following:

- Learn to design inclusively.
- Write helpful `alt` text for technical diagrams.
- Check color contrast.
- Create accessible diagrams.
- Detect accessibility errors in documents.

## Design inclusive writing

### Types of disability

Disability can be visible or invisible, and it can be situational, temporary, or permanent. The following table includes some examples.

|  | **Vision** | **Hearing** | **Speech** | **Mobility** | **Cognition** |
| --- | --- | --- | --- | --- | --- |
| **Situational** | DrivingDark room | Noisy environment | In a libraryAt a lecture | In bedArms/hands full | Forgetting informationTime demands |
| **Temporary** | Dilated pupilsCataracts | Ear infection | Laryngitis | Arm or hand injury | No prior trainingMulti-tasking |
| **Permanent** | BlindnessVision impairment | DeafHard-of-hearing | DysarthriaStuttering | AmputationParkinson's disease | Dementia |

According to the [World Health Organization](https://www.who.int/news-room/fact-sheets/detail/disability-and-health), about 16% of the world's population experiences significant disability. However, as the preceding table illustrates, disability shows up in various ways and can affect anyone at different times in life. Inclusive design benefits everyone.

### The curb cut effect

Designing with inclusion in mind often results in benefits beyond the intended use cases.

The *curb cut effect* is a common example of inclusive design in the physical world. Originally, curb cuts (sidewalk ramps) were designed for people in wheelchairs. However, many people benefit from curb cuts, such as anyone with a stroller, suitcase, or delivery cart.

Here are some other examples of the curb cut effect in digital technology:

- **Contrast ratios**: Color contrast requirements were originally designed to help people who have low vision or color blindness. Color contrast requirements also ended up helping people who are trying to see the phone screen on a sunny day, or who had their pupils dilated at the eye doctor.
- **Text to speech and voice commands**: These tools assist people who are blind or have low vision. They also turned out to be useful for hands-free use while driving, cooking, or holding a baby.
- **Keyboard access**: Improving keyboard navigability improves accessibility for screen reader users and people with motor impairments. Keyboard access also improves productivity for power users.
- **Clear language**: Simplifying language increases cognitive inclusion, and it also eases translation and localization.

## Write helpful alt text

*Alternative text* (alt text) is short, descriptive text that acts as a substitute for visual items on a page. The most common use is for describing images.

Alt text supports readers in the following ways:

- Screen readers read alt text for people who are blind or who have low vision.
- Descriptive alt text also helps to [improve search results for images](https://developers.google.com/search/docs/appearance/google-images).

### Write useful alt text

Alt text acts as a functional equivalent of an image for readers who can't view the image. The following subsections describe best practices for writing helpful alt text.

**Explain the image in context**

Explain images in the context of the text. In the context of the surrounding text, you might choose to emphasize or omit aspects of an image in your description. 

**Briefly summarize the image’s purpose**

Use a short phrase or one or two sentences. Long descriptions interrupt the reading flow for screen reader users.

- Don't include extra words like "Image of" or "Photo of."
- Capitalize the first word and include a final period.
- Use other punctuation as necessary.

**Avoid duplicating the surrounding text**

If the meaning of your document would be the same without the image, add an empty alt text attribute to the image (`alt=""`). Assistive technologies ignore the empty attribute.

Use empty alt text in the following situations:

- The image is decorative (not informative), such as an image of a horizontal line that is meant to be a visual border at the end of a page.
    
    Consider making a decorative image a CSS background image, since background images are always ignored by screen readers.
    
- The image duplicates information that is already expressed in text on the page.

**Describe complex images in your document**

The information in a complex image such as a flowchart, graph, or map can be difficult to describe in a few short sentences. In this situation, provide a short description of the image in the alt text and a longer textual description in the main text of your document or on a separate page that you link to.

- For graphs, you can provide a data table on the same page or on a separate page.
- For flowcharts and diagrams, explain the process or parts of your image in the text of your document.

**Include demographic information only when necessary**

When you describe people, include demographic information only if it is critical to the main point of the image. Otherwise, use *person* or another term that provides key context about the person's activity or role in the image, such as *musician*, *basketball player*, *teacher*, or *doctor*.

**Other considerations**

- For repeated images, use consistent alt text.
- Avoid all caps.
    - Words in all caps always have a rectangular shape, whereas words in regular case have distinct shapes. Some people with visual or cognitive disabilities rely more on the shape of words to read them.
    - Screen readers might misread words in all caps as acronyms.
- Introduce diagrams in the body text, not in the alt text.

### Learn more

- Read the Google developer documentation style guidelines on [Accessibility](https://developers.google.com/style/accessibility) and [Alt text](https://developers.google.com/style/images#alt-text)
- Read the [W3C tutorial for images](https://www.w3.org/WAI/tutorials/images/)
- Read the [Web Accessibility in Mind alt text guidelines](https://webaim.org/techniques/alttext/)

## Use sufficient contrast

Higher contrast makes it easier for everyone to read text and images. When there is low contrast, everyone has difficulty viewing content.

## Choose inclusive language

When writing about people with disabilities or about accessibility, be mindful about using unintentionally biased language that may cause harm.

### Write thoughtfully about disability

Don't use euphemisms or patronizing terms:

- **Avoid** describing people without disabilities as *normal* or *healthy*.
- **Better**: *nondisabled person, sighted person, hearing person, person without disabilities, neurotypical person*.
- **Avoid** terms that reflect or project feelings and judgements about a person's disability, such as *victim of, suffering from, wheelchair-bound*.
- **Better**: *experiencing, living with, uses a wheelchair*

### Person-first and identity-first language

When writing about accessibility and people with disabilities, be sure to center the person or community, and avoid terms that remove personhood.

- **Avoid** language like *the disabled*
- **Better**: *people with disabilities*

## Add accessible visuals to writing

### Why visual indicators are insufficient

Visual cues like color, shape, and pattern can be effective tools for communicating information. However, to ensure that content is accessible to a wide audience, don't rely exclusively on the visual elements, such as the following:

- colors
- patterns
- images
- font styling
- directional words (for example, "top-right corner")

Instead, use a mix of these visual elements and accompany them with descriptive text to convey information. It is also important to provide text descriptions or alternative text when using images, diagrams, or other diagrams.

### Examples

- Don’t rely on color alone
- Use text, color and symbold for better accessibility

## Edit for accessibility

### Cultivate an accessibility mindset for doc editing

When you are aware of and focus on the fundamentals of good writing, you also make your documentation more accessible.

With practice, self-editing can help you catch accessibility pitfalls, such as these:

- poor or missing headings
- uninformative link text
- dense, complex text

### Create helpful headings

Headings help your audience understand what's in your document. Clear, well-structured document headings simplify navigatation for people with cognitive disabilities and those who use screen readers.

### Include informative link text

People who use screen readers often use them to scan a page to hear just the links. Use informative link text to ensure that your audience hears meaningful information, not just "Learn more, learn more, learn more."

- Avoid:
    - [Learn more](https://developers.google.com/style/tables)
    - [Click here](https://developers.google.com/style/tables)
    - [This document](https://developers.google.com/style/tables)
- Good:
    - Learn how to [format tables](https://developers.google.com/style/tables).
    - Read about [inclusive design](https://developers.google.com/tech-writing/accessibility/self-study/inclusive-design).

### Use straightforward language and short sentences

Other units in this course talk about visual images and how to use them inclusively. Remember that abstract and unfamiliar *written* representations can also be particularly challenging for users with cognitive or visual impairments.

Avoid unfamiliar jargon, US-based slang, pop-cultural references, and complicated linguistic constructions. Use active voice and short sentences, and define your technical terms on first use if they are not commonly understood.

### Tst your content for accessibility

Finally, to get a feel for some different ways your users might access and consume your document, try these testing tips:

- Change the zoom level to help accommodate readers on small screens or full-size monitors.
- Use only the keyboard to navigate your document. For example, see [Keyboard shortcuts in Chrome](https://support.google.com/chrome/answer/157179).
- Use a screen reader:
    - ChromeVox for ChromeOS
    - VoiceOver for Mac

## Course summary

Technical Writing for Accessibility focused on the following ideas:

- Accessibility in documentation is a type of inclusive design, benefiting people with permanent, temporary, or situational disabilities.
- Every image requires an alt text element. Alt text acts as a functional equivalent for an image by providing a concise summary of the image's purpose and context.
- Sufficient color contrast helps readers with color blindness or low vision.
- Use inclusive language to write for a broad spectrum of readers.
- Avoid relying only on visual indicators, such as colors or patterns, to communicate important information.
- Practice editing for accessibility to ensure proper heading structure, descriptive link text, and clear language.

---

# Write Helpful Error Messages

## Target audience for this course

We've aimed this course at the following audiences:

- Engineers
- Program managers
- Technical writers

## Why take this course?

Bad error messages frustrate users. Good error messages provide critical information when things are not working as expected. Error messages are often the main way developers interact with users when problems occur. Some error messages are caused by invalid user inputs or misuse of certain features and some are caused by product defects; all error messages require users to figure out what to do next.

Data collected through Google support systems and UX research identified the following common problems with *bad* error messages:

- unactionable
- vague
- imprecise
- confusing
- inaccurate
- unclear cause
- unknown next steps

Conversely, *good* error messages provide the following benefits:

- Deliver the best user experience.
- Are actionable.
- Are universally accessible. (To learn more, take [Tech Writing for Accessibility.](https://developers.google.com/tech-writing/accessibility))
- Enable users to help themselves.
- Reduce the support workload.
- Enable faster resolution of issues.

## Learning objectives

After completing this class, you will know how to do the following:

- Write clearer, more helpful error messages.
- Review your teammates' error messages.

### Learning non-objectives

This course does not explain the mechanics of generating error messages. For example, this course does not explain how to display error messages within a GUI.

## General error handling rules

### Don’t fail silently

Failure is inevitable; failing to report failures is inexcusable. Failing silently causes the following problems:

- Users wonder whether something has gone wrong. (*"Why did my order not go through?"*)
- Customer support wonders what caused a problem. (*"The log file gave no indication of a problem."*)

Embrace your software's fallibility. Assume that humans will make mistakes using your software. Try to minimize ways for people to misuse your software, but assume that you can't completely eliminate misuse. Therefore, plan error messages as you design software.

### Follow the programming language guidelines

Follow the guidelines on error handling in Google's programming language guides, including:

- [Google C++ Style Guide](https://google.github.io/styleguide/cppguide.html)
- [Google Java Style Guide](https://google.github.io/styleguide/javaguide.html)
- [Google Python Style Guide,](https://google.github.io/styleguide/pyguide.html) particularly the [Error Messages section](https://google.github.io/styleguide/pyguide.html#3102-error-messages)
- [Google JavaScript Style Guide](https://google.github.io/styleguide/jsguide.html)

### Implement the full error model

Implement the full error model described in the [Errors page of the Google AIP.](https://google.aip.dev/193)

### Avoid swallowing the root cause

API implementations should not swallow the root cause of issues occurring in the back end. For example, many different situations can cause a "Server error" problem, including:

- service failure
- network connection drop
- mismatching status
- permission issues

"Server error" is too general an error message to help users understand and fix the problem. If the server logs contain identification information about the in-session user and operation, we recommend providing additional context on the particular failure case.

### Log the error codes

Numeric **error codes** help customer support monitor and diagnose errors. Consequently, specifying numeric error codes along with textual error messages is often quite valuable.

You can specify error codes for both internal and external errors. For internal errors, provide a proper error code for easy lookup/debugging by internal support personnel and engineers.

Document all error codes.

### Raise errors immediately

Raise errors as early as useful. Holding on to errors and then raising them later increases debugging costs dramatically.

## Identify the error’s cause

Tell users exactly what went wrong. Be specific—vague error messages frustrate users.

## Identify the user’s invalid inputs.

If the error involves values that the user can enter or modify (for example, text, settings, command-line parameters), then the error message should identify the offending value(s).

If the invalid input is a very long value that spans many lines, consider doing one of the following:

- Disclose the bad input progressively; that is, provide one or more clickable ellipses to enable users to control how much additional error information they want to see.
- Truncate the bad input, keeping only its essential parts.

## Specify requirements and constraints

Help users understand requirements and constraints. Be specific. Don't assume that users know the limitations of your system.

## Explain how to fix the problem

Create **actionable error messages**. That is, after explaining the cause of the problem, explain how to fix the problem.

## Provide examples

Supplement explanations with examples that illustrate how to correct the problem.

## Be concise

Write concise error messages. Emphasize what's important. Cut unnecessary text. See the [Short sentences unit of Tech Writing One](https://developers.google.com/tech-writing/one/short-sentences) for tips on reducing sentence length.

Converting from [passive voice to active voice](https://developers.google.com/tech-writing/one/active-voice) often makes sentences conciser and easier to understand.

In your enthusiasm to be concise, don't remove so many words that the resulting error message becomes cryptic.

## Avoid double negatives

A **double negative** is a sentence or phrase that contains two negative words, such as:

- *not*, including contractions like *can't*, *won't*
- *no*

Readers find double negatives hard to parse. ("Wait, do two negatives make a positive or is the author of the error message using two negatives to emphasize something I shouldn't do?")

## Write for the target audience

Tailor the error message to the target audience. That is:

- Use appropriate terminology for that target audience.
- Be mindful of what the target audience knows and doesn't know.

Beware of the [curse of knowledge](https://developers.google.com/tech-writing/one/audience#curse_of_knowledge) when writing error messages. A term familiar to you might not be familiar to your target audience.

## Use terminology consistently

Use terminology consistently for all error messages within a single product area. If you call something a "datastore" in one error message, then call the same thing a "datastore" in all the other error messages.

Error messages must appear consistently with similar formats and non-contradictory content; that is, the same problem must generate the same error message. For example, if different parts of an app each detect problems with internet connection, both parts should emit the same error message.

## Format error messages to enhance readability

### Link to more detailed documentation

When an error requires a lengthy explanation (for example, multiple sentences) and appropriate documentation is available, use links to redirect users to more detailed documentation.

### Use progressive disclosure

Some error messages are long, requiring a lot of text to explain the problem and solution. Unfortunately, users sometimes ignore long error messages, intimidated by the "wall of text." A good compromise is to display a briefer version of the error message and then give users the option to click something to get the full context.

### Place error messages close to the error

For coding errors, place error messages as close as possible to the place where the error occurred.

### Handle font colors carefully

A surprising percentage of readers are color blind, so be careful with colors in error messages.

Many forms of color blindness exist, so just avoiding a red/green combination isn't sufficient. Because you can't depend on all your users being comfortable with color, we recommend pairing color with another visual cue

## Set the right tone

### Be positive

Instead of telling the user what they did wrong, tell the user how to get it right.

### Don't be overly apologetic

While maintaining positivity, avoid the words "sorry" or "please." Focus instead on clearly describing the problem and solution.

### Avoid humor

Don't attempt to make error messages humorous. Humor in error messages can fail for the following reasons:

- Errors frustrate users. Angry users are generally not receptive to humor.
- Users can misinterpret humor. (Jokes don't always cross borders well.)
- Humor can detract from the goal of the error message.

### Don't blame the user

If possible, focus the error message on what went wrong rather than assigning blame.

## Course summary

This course recommended the following best practices when writing error messages:

- Identify the cause of the error.
    - If the user entered an invalid value, specify the invalid value.
    - Specify requirements and constraints, such as required permissions or minimum RAM.
- Explain to fix the problem.
    - When appropriate, provide an example to help demonstrate the fix.
- Write clearly.
    - Be concise, not wordy. However, don't be so concise that the resulting error message becomes cryptic.
    - Avoid double negatives and exceptions to exceptions.
    - Aim the message at the appropriate target audience. Words appropriate for software engineers are often inappropriate for non-technical users.
    - Use terminology consistently. For example, don't use the term *directory* in one part of an error message and a *folder* in another part.
    - Format long error messages carefully, possibly using progressive disclosure or links to expanded documentation.
    - Set a positive tone.
    - Don't be overly apologetic.

## Additional guidelines for back-end engineers

### Supply error codes

If an error code exists, include it as part of the error message. Error codes help technical users identify the error and find more information from an error index or error catalog.

### Include an Error Identifier

Engineers parse logs to learn how and why errors occurred; therefore, include an Error Identifier to help engineers find particular errors more easily. The Error Identifier should stay constant, even if the textual error message changes.

For more information, see the [Errors unit of AIP-193.](https://google.aip.dev/193)