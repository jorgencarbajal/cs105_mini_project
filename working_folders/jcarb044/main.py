import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.stats import spearmanr
from pathlib import Path

ROOT_PATH = Path(__file__).resolve().parent.parent.parent
DATA_PATH = ROOT_PATH / "data/uncleaned_data.csv"

# read the csv
df = pd.read_csv(DATA_PATH)


def find_col(text) -> str:
    """
    takes in the question string as parameter, list comprehension to loop through columns to find a match, asserts there is only one match, return the match.
    """
    matches = [c for c in df.columns if text in c]
    assert len(matches) == 1, f"{text!r} matched {len(matches)} columns"
    return matches[0]


def ai_use_to_num(answer):
    """
    Convert one 'How often do you use AI for...' answer to 0-3.
    """
    if pd.isna(answer):
        return np.nan
    answer = answer.lower()
    if "very often" in answer:
        return 3
    if "sometimes" in answer:
        return 2
    if "rarely" in answer:
        return 1
    if "don" in answer:  # "I don't use AI for this" (broken apostrophe, so match on part of it)
        return 0
    return np.nan        # "Prefer not to answer"


def main():
    # list comprehension for ai use columns that will help calculate the ai-reliance score
    ai_use_cols = [c for c in df.columns if c.startswith("How often do you use AI for the following:")]

    # storing the columns in a dict
    group_cols = {
        "learn_myself": find_col("[I want to learn the material myself]"),
        "no_trust":     find_col("trust its answers]"),  # the apostrophe in "don't" is a broken character in the data
        "rules":        find_col("[My class rules don't allow it]"),
    }

    # print(len(ai_use_cols), "AI-use columns:")
    # for c in ai_use_cols:
    #     print("  ", c.split("[")[-1].rstrip("]"))

    # convert that column answers into values through the function. here we take the answers to the ai use questions to obtain values for those answers
    ai_use = df[ai_use_cols].map(ai_use_to_num) # (86, 8)

    # create a new df that contains the shortened names as columns and the Series of each answer
    violin_df = pd.DataFrame({name: df[col] for name, col in group_cols.items()}) # (86, 3)
    violin_df["reliance_score"] = ai_use.mean(axis=1) # (86, 4)
    # for students who had less than six answers, remove the reliance score
    violin_df.loc[ai_use.notna().sum(axis=1) < 6, "reliance_score"] = np.nan

    # print("Students with a reliance score:", violin_df["reliance_score"].notna().sum(), "of", len(violin_df))
    # print(violin_df.shape)
    # ai_use.shape

    GROUP_ORDER = ["Not at all / A little", "Somewhat", "A lot"]
    merge_low = {"Not at all": "Not at all / A little", "A little": "Not at all / A little"}

    for name in group_cols:
        violin_df[name + "_group"] = pd.Categorical(
            violin_df[name].replace(merge_low), categories=GROUP_ORDER, ordered=True
        )

    # print(violin_df.head())

    # (column short name, panel title, internal/external)
    PANELS = [
        ("learn_myself", "\"I want to learn the material myself\"", "internal"),
        ("no_trust",     "\"I don't trust its answers\"",          "internal"),
        ("rules",        "\"My class rules don't allow it\"",      "external"),
    ]

    # Group sizes and medians behind the plot (one small table per reason)
    for name in group_cols:
        print(name)
        print(violin_df.groupby(name + "_group")["reliance_score"].agg(["count", "median"]).round(2))
        print()

    # COLORS = {"internal": "#4C72B0", "external": "#B0B0B0"}

    # fig, axes = plt.subplots(1, 3, figsize=(15, 5.5), sharey=True)

    # for ax, (name, title, kind) in zip(axes, PANELS):
    #     group_col = name + "_group"
    #     panel = violin_df.dropna(subset=["reliance_score", group_col])  # drop blanks for THIS panel    only

    #     sns.violinplot(data=panel, x=group_col, y="reliance_score", order=GROUP_ORDER,
    #                    cut=0, inner="quartile", color=COLORS[kind], linewidth=1, ax=ax)
    #     sns.stripplot(data=panel, x=group_col, y="reliance_score", order=GROUP_ORDER,
    #                   color="black", size=3, alpha=0.5, jitter=0.15, ax=ax)

    #     counts = panel[group_col].value_counts()
    #     ax.set_xticks(range(len(GROUP_ORDER)))
    #     ax.set_xticklabels([f"{g}\n(n={counts[g]})" for g in GROUP_ORDER])
    #     ax.set_title(f"{title}\n({kind} reason)")
    #     ax.set_xlabel("How much this keeps them from using AI")
    #     ax.set_ylabel("")

    # axes[0].set_ylabel("AI-reliance score\n(0 = never, 3 = very often)")
    # axes[0].set_ylim(-0.1, 3.1)
    # fig.suptitle("Personal reasons go with less AI use; class rules make little difference",    fontsize=14)
    # fig.tight_layout()
    # plt.show()

if __name__ == "__main__":
    main()