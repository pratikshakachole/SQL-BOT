# -*- coding: utf-8 -*-
"""
Created on Sun Apr  6 15:33:21 2025

@author: prati
"""

import streamlit as st
import google.generativeai as genai

GOOGLE_API_KEY = "GOOGLE_API_KEY"
genai.configure(api_key=GOOGLE_API_KEY)
model = genai.GenerativeModel("gemini-pro")

def main():
    st.set_page_config(page_title="SQL Assistant",page_icon="robat:") 

    st.markdown(
        """
        <div style="text-align:center;">
        <h1>SQL Assistant 🤖✨</h1>
        <h3>Your Personal SQL Query Assistant</h3>
        <p> Your Personal Data Wizard! Simply tell Genie what records you need from the database,
          and it'll craft the perfect SQL query for you along with a detailed explanation. 
          Let the magic of technology simplify your data retrieval process! ✨</p>
        </div>

    """,
    unsafe_allow_html=True,
    )

    text_input= st.text_area("Type your desired query below to unlock the power of SQL Assistant! ✨💬")

    submit = st.button("Generate SQL Query")

    if submit:
        with st.spinner("Generating SQL Query.."):
            template="""
                    Create a SQL query snippet using the below text:

                    ```
                    {text_input}
                    ```  
                    i just want a Sql query         
"""
            formatted_template = template.format(text_input=text_input)
            st.write(formatted_template)
            response = model.generate_content(formatted_template)
            sql_query = response.text
            sql_query= sql_query.strip().lstrip("```sql").rstrip("```")

            expected_output="""
                    What would be the expected response of this SQL query snippet:


                    ```
                    {sql_query}
                    ```  
                    Provide sample tabluer Response with No Explanation        
"""
            expected_output_formatted= expected_output.format(sql_query=sql_query)
            eoutput = model.generate_content(expected_output_formatted)
            eoutput = eoutput.text
            

            explanation="""
                    Explain this sql Query:


                    ```
                    {sql_query}
                    ```  
                    Please provide with simplest of explanation:      
"""
            explanation_formatted = explanation.format(sql_query=sql_query)
            explanation= model.generate_content(explanation_formatted)
            explanation = explanation.text
            with st.container():
                st.success("Your SQL query has been successfully generated. Feel free to copy and paste it into your database management system to retrieve the requested records.")
                st.code(sql_query,language="sql")

                st.success("Expacted output of this SQL Query")
                st.markdown(eoutput)

                st.success("Explanation of SQl Query")
                st.markdown(explanation)



main()