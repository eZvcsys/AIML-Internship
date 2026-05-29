import streamlit as st
import pandas as pd

# Title
st.title("📊 Python Pandas & Visualization Quiz")

st.write("Answer the following multiple-choice questions. Your trainer will evaluate your responses later.")

# Questions and options
questions = [
    {"question": "Pandas DataFrame is best described as:",
     "options": ["A one-dimensional labeled array", "A two-dimensional labeled data structure", "A dictionary of lists", "A matrix without labels"]},
    {"question": "Which method is used to read a CSV file into a Pandas DataFrame?",
     "options": ["pd.read_excel()", "pd.read_csv()", "pd.DataFrame()", "pd.read_table()"]},
    {"question": "Difference between loc and iloc in Pandas?",
     "options": ["loc uses integer positions, iloc uses labels", "loc uses labels, iloc uses integer positions", "Both use labels", "Both use integer positions"]},
    {"question": "Which function gives a quick statistical summary of a DataFrame?",
     "options": ["df.info()", "df.describe()", "df.head()", "df.shape()"]},
    {"question": "To remove missing values from a DataFrame, you use:",
     "options": ["df.dropna()", "df.fillna()", "df.replace()", "df.remove()"]},
    {"question": "GroupBy in Pandas is used for:",
     "options": ["Sorting data", "Aggregating data based on categories", "Filtering rows", "Merging DataFrames"]},
    {"question": "Which method merges two DataFrames based on a common column?",
     "options": ["pd.concat()", "pd.merge()", "pd.join()", "pd.append()"]},
    {"question": "To get the first 10 rows of a DataFrame, you use:",
     "options": ["df.tail(10)", "df.head(10)", "df.sample(10)", "df.iloc[10]"]},
    {"question": "Matplotlib is primarily used for:",
     "options": ["Machine learning models", "Data visualization", "Web development", "File handling"]},
    {"question": "Which function in Matplotlib is used to plot a line graph?",
     "options": ["plt.bar()", "plt.plot()", "plt.scatter()", "plt.line()"]},
    {"question": "In Seaborn, which function is used to plot a heatmap?",
     "options": ["sns.barplot()", "sns.heatmap()", "sns.scatterplot()", "sns.lineplot()"]},
    {"question": "To show a histogram using Matplotlib, you use:",
     "options": ["plt.hist()", "plt.bar()", "plt.plot()", "plt.show()"]},
    {"question": "Seaborn is built on top of:",
     "options": ["NumPy", "Pandas", "Matplotlib", "SciPy"]},
    {"question": "Which Seaborn function is used to visualize the distribution of a single variable?",
     "options": ["sns.distplot()", "sns.histplot()", "sns.boxplot()", "sns.violinplot()"]},
    {"question": "To display the plot in Matplotlib, you must call:",
     "options": ["plt.show()", "plt.display()", "plt.plot()", "plt.run()"]}
]

# Collect responses
responses = {}
for i, q in enumerate(questions):
    st.subheader(f"Q{i+1}: {q['question']}")
    choice = st.radio("Select your answer:", q["options"], key=i)
    responses[f"Q{i+1}"] = choice

# Submit and download
if st.button("Submit Responses"):
    st.info("✅ Your answers have been recorded. The trainer will evaluate them.")
    st.write("Here are your selected responses:")
    st.json(responses)

    # Convert to DataFrame
    df = pd.DataFrame(list(responses.items()), columns=[
                      "Question", "Selected Answer"])

    # Download button
    csv = df.to_csv(index=False).encode("utf-8")
    st.download_button(
        label="📥 Download Responses as CSV",
        data=csv,
        file_name="quiz_responses.csv",
        mime="text/csv"
    )
