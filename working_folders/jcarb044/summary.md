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

## Waffle

- The idea is to find out if stress pushes students to go to AI instead of their professor or TA. When students are stressed, do they skip office hours and go straight to AI?

- **Broad Question A**: "During the past 7 days how much did you experience each of the following, on a scale of 1-5?"
    - Sub question:
        - "Stress about coursework"; (1 | 2 | 3 | 4 | 5)

- We use this to split students into two "groups": **less stressed** (1-3) and **stressed** (4-5). Only 10 students answered 1 or 2, so 3 had to go with the less stressed group to make it big enough.

- To compare the groups we need to somehow compute an **AI-instead-of-professor score**. There is the **Broad Question B**, "When you needed help with the following tasks during the past 7 days, how often did you consult AI without consulting your professor or TA?", that was followed by 3 subquestions (understanding a course concept | understanding what an assignment is asking | figuring out how to solve a problem) where students could answer (never | rarely | sometimes | often | all the time). The values are 0-4 with never being 0 and all the time being 4. We sum the scores and average to build the score. Then we put each student into a bucket: **Rarely** (0-1), **Sometimes** (above 1, up to 2), and **Often** (above 2).

    - The limitations of this score are that it is built from only 3 subquestions and only looks at the past 7 days, so it is a snapshot of one week. Stress also comes from a single question. We also can't tell which one causes the other, stress could push students to AI, or something else like time management could be causing both.

After building the score we can plot the results. There are two grids, one for the less stressed group and one for the stressed group. The groups are not the same size (34 vs 49 students), so each grid is scaled to 100 squares where each square is 1% of that group, not one student. This way both grids are the same size and can be compared directly. The darker the square, the more often students went to AI instead of their professor/TA, and the squares are sorted light to dark so the "Often" students form one dark block. The idea here is to see if the dark block gets bigger as students get more stressed.

- What we found is that only about 12 out of every 100 less stressed students often go to AI first, while in the stressed group it is 51 out of every 100, about half the grid.

