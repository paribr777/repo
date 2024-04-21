import streamlit as st

def main():
    st.title('Maximum of Three Numbers')
    num1 = st.number_input('Enter the 1st number:', value=0)
    num2 = st.number_input('Enter the 2nd number:', value=0)
    num3 = st.number_input('Enter the 3rd number:', value=0)
    if st.button('Find Maximum'):
        maximum = max(num1, num2, num3)
        st.success(f'The maximum is {maximum}.')

if __name__ == '__main__':
    main()
