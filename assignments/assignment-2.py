import streamlit as st
import pandas as pd

# Title
st.title("📊 Power BI Quiz")

st.write("Answer the following multiple-choice questions. Your trainer will evaluate your responses later.")

# Power BI Questions
questions = [
    {"question": "Power BI Desktop is primarily used for:",
     "options": ["Creating reports and dashboards", "Managing databases", "Writing SQL queries only", "Cloud storage"]},
    {"question": "Which feature in Power BI allows you to combine data from multiple sources?",
     "options": ["Data Modeling", "Power Query", "DAX Functions", "Visualizations"]},
    {"question": "DAX stands for:",
     "options": ["Data Analysis Expressions", "Data Aggregation XML", "Dynamic Analytics Exchange", "Data Access Extension"]},
    {"question": "In Power BI, a relationship between tables is defined by:",
     "options": ["Primary and foreign keys", "Column formatting", "Report filters", "Visual hierarchy"]},
    {"question": "Which visualization is best suited for showing categorical comparisons?",
     "options": ["Line chart", "Bar chart", "Scatter plot", "Map"]},
    {"question": "Power BI Service is used for:",
     "options": ["Building models locally", "Publishing and sharing reports online", "Writing SQL queries", "Editing Excel sheets"]},
    {"question": "To create calculated columns or measures, you use:",
     "options": ["Power Query", "DAX formulas", "SQL scripts", "Pivot tables"]},
    {"question": "Which feature allows you to schedule automatic data refreshes in Power BI Service?",
     "options": ["Power Query Editor", "Gateway connection", "DAX formula", "Report filters"]},
    {"question": "Power BI Dashboard differs from a report because:",
     "options": ["Dashboards can have multiple pages", "Dashboards are single-page, reports can have multiple pages", "Reports cannot use visuals", "Dashboards cannot be shared"]},
    {"question": "Which visualization is best for showing geographical data?",
     "options": ["Line chart", "Map visual", "Histogram", "Pie chart"]}
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
        file_name="powerbi_quiz_responses.csv",
        mime="text/csv"
    )
