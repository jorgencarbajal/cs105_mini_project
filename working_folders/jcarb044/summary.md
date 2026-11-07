## Violin

- The idea is to find out what holds back students from using AI. We are looking at two personal reasons and one external reason. Does what they say, hold true?

- **Broad Question A**: "When you are working on a homework assignment, how much does each of these keep you from using AI?"
    - Sub questions:
        - "I want to learn the material myself"; (Not alot | a little | somewhat | a lot)
        - "I dont trust its answers"; (Not alot | a little | somewhat | a lot)
        - "My class rules dont allow it" (Not alot | a little | somewhat | a lot)

- We use these "groups" to essentially try and find out if what students say, holds true with there actions. 

- To test this we need to somehow compute an **AI-reliance score**. There is the **Broad Question B**, "How often do you use AI for the following", that was followed by 8 subquestions where students could answer (dont use ai for this | use is rarely | use is sometimes | use it often). The values are 0-3 with not using AI is 0 and using it often is 3. We sum the scores and average to build the score.

    - The limitations of this score are that they build it based on a single questions with its subquestions. We could extend this and try and build a better score from all features giving weight to some over others to build a more reliable score and capture students who may not have answered this question.

After building the AI score we can plot the results. All subplots share the same y axis and x axis. On the y axis we have the **AI-reliance score** and on the x-axis we have the options to the sub questions in **Broad Question A**. Each of the subplots represents one of the sub questions in **Broad Question A**. The idea here is to isolate the reasons that keep students from using AI and to see if there is a trend as these reasons matter more to students.

## Mosaic

