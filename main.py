import streamlit as st
from _LinearRegressionModel import LinearRegressionModel

def main():
    st.set_page_config(page_title='Bank Loan Simulate', page_icon=':moneybag:', layout='centered', initial_sidebar_state='auto')

    st.title('Linear Regression :blue[Example]')

    st.latex(r'''
    \hat{Y} = \beta_0 + \beta_1 X
    ''')

    st.sidebar.title('Bank Loan Simulate')
    st.sidebar.write('This app simulates the approval of a bank loan based on the client\'s salary. The data is fictitious. Study on linear regression')
    
    st.sidebar.title('Linear Regression Algorithm')
    st.sidebar.write('Linear regression is a machine learning method used to model the relationship between a dependent variable (target) and one or more independent variables (features). The core idea is to find the straight line (or hyperplane in the case of multiple variables) that best fits the data. The equation for simple linear regression is:')
    st.sidebar.latex(r'''
    \hat{Y} = \beta_0 + \beta_1 X
    ''')    
    
    st.sidebar.write('[GitHub](https://github.com/devlucascfarias)')

    model = LinearRegressionModel('data/BaseDados_RegressaoLinear.xlsx')

    salary = st.number_input('Enter the client\'s salary', format='%f')

    if st.button('Predict'):
        prediction = model.predict(salary)
        st.write(f'The client is likely to receive a loan of ${prediction[0][0]:.2f}')




if __name__ == '__main__':
    main()

