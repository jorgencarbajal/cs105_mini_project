# Brainstorming: Main Topic Question

Column letters (e.g. `BS`, `DE`) refer to the spreadsheet columns listed in [`data/features.txt`](data/features.txt).

## Where we are

- **Current topic** (`project_description/current_project_topic.pdf`): *Why some students use AI more than others.*
- **Current main question:** How does how much students use AI depend on their obligations outside school, what they do when stuck, what holds them back, and how much they think classmates use it?
- **Requirements** (from the project description): at least 8 visualizations with at least 6 different types, at least 3 hypotheses, and at least one correlation test and one chi-squared test.
- **Dataset:** about 75 responses. Roughly 67–69 are usable for the AI questions, because about 6–8 people skipped that section.

## How well the data supports the current question

| Part of the main question | Columns | Problem |
|---|---|---|
| Obligations outside school | AO–AT (hours worked, caregiving, etc.) | Most answers are 0: 46 of 71 don't work and 66 of 71 aren't caregivers. Very little to compare. |
| What they do when stuck | BS–BU | **This is the strongest signal in the dataset** (see below). |
| What holds them back | DE–DJ | Good. The answers are spread out across the scale. |
| What classmates do | none | **We never measured this directly.** The only proxy is the "Most of my classmates use it" checkbox in DD. |

### The standout finding (BS–BU: stuck on a problem for 15 minutes)

```
                     Try on own   Ask AI hint   AI full solution
More than enough time    39           14              2
Just enough time         16           32              4
Not enough time           1           37             18
```

"Try on my own" almost disappears and "full solution" goes up 9×. This alone could carry the project.

## Three possible directions

### A. Time pressure (recommended)

> *How does students' reliance on AI depend on time pressure (deadlines, procrastination, outside obligations, stress) and on what holds them back from using it?*

- It keeps our own questions (BS–BU and DE–DJ) at the center.
- Other groups' columns add the time-pressure side:
  - when students start assignments (BG–BM)
  - how often they finish late (CR–CT)
  - "I rely on AI more after I procrastinate" (CU)
  - stress (AN, FF–FG)
- **The thing we measure (outcome):** days of AI use in the past week (FP, 1–7), or an AI-reliance score averaged from the CA–CH ratings.

### B. Dependence and confidence

> *Do students who use AI more feel less able to do the work without it?*

- Uses confidence with vs. without AI (CI–CP), worry about working without AI (FL–FN), grade satisfaction (BR), and GPA (N).
- It's a clean story, but it moves away from the questions we wrote.

### C. Learner vs. shortcut

> *Do students who say "I want to learn it myself" use AI differently, asking for hints rather than full solutions?*

- Compares the deterrent ratings (DE, DF) with hint-vs-solution choices and with what they use AI for (CV–DC, DL–DP).
- It works well as one hypothesis inside Direction A, but it's narrow for the whole project.

## Rough plan for Direction A

### Visualizations (8+, with 6+ types)

1. **Stacked 100% bar chart:** what students do when stuck, by time left (BS–BU). *(Junwen's idea)*
2. **Heatmap:** how often AI is used for each study activity (CA–CH). *(Junwen's idea)*
3. **Parallel coordinates plot:** each student's profile across the deterrents (DE–DJ), colored by how often they use AI. *(fits Khant's idea)*
4. **Radar/spider chart:** average deterrent strength, heavy vs. light AI users. *(fits Shiyao's idea)*
5. **Box plot:** days of AI use (FP) by "relies on AI more after procrastinating" (CU).
6. **Scatter plot with a trend line:** stress or procrastination score vs. AI-reliance score.
7. **Histogram or KDE:** minutes of AI use per week (FQ). It's skewed, so a log scale probably helps.
8. **Violin plot:** AI-reliance score, working vs. not working (AO).
9. **Correlation heatmap:** all the numeric predictors vs. the AI score.

### Hypotheses

- **H1 (chi-squared):** what students do when stuck depends on how much time is left. Use BS vs. BU, with the answers grouped into Self / Peer-TA / AI so every cell has enough students for the test.
- **H2 (correlation):** students with stronger "I want to learn it myself" ratings (DE) use AI on fewer days (FP). Spearman correlation, since the ratings are ordered categories.
- **H3 (Spearman or Mann-Whitney):** procrastination (CR–CU, BG–BM) or stress (AN, FF–FG) is positively related to AI reliance.
- **H4 (optional, chi-squared):** saying "rely on AI more after procrastinating" (CU) is linked to choosing "full solution" when out of time (BU).

## Data cleanup to expect

- **Work hours (AO):** change to a simple works / doesn't work.
- **GPA (N):** drop "Prefer not to say" and the freshman answer.
- **On-time submissions (FS):** free text ("5 ; 3", "3;3", "3.0") that needs parsing.
- **Minutes of AI use (FQ):** has outliers and 13 blanks.
- **Skipped AI section:** about 6–8 people skipped it. Exclude them consistently.

## Open decisions for the group

1. Do we go with Direction A, or with B or C?
2. What do we do about the "what classmates do" part of the main question? We never measured it, so we can either drop it or rely only on the DD checkbox ("Most of my classmates use it").
3. Which outcome do we use for "how much students use AI": FP (days per week), FQ (minutes), or a combined score from CA–CH?
