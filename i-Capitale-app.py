
# import library
import matplotlib.pyplot as plt
import streamlit as st
from streamlit_option_menu import option_menu
from PIL import Image
import numpy as np
import yfinance as yf
import requests  # pip install requests
from streamlit_lottie import st_lottie  # pip install streamlit-lottie


st.set_page_config(page_title="i-Capitale App",page_icon="📈️",layout="centered",initial_sidebar_state="expanded")



def load_lottieurl(url: str):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()


def MainPage():
    # front end elements of the web page
    html_temp = """ 
                <div style ="background-color:gold;padding:13px"> 
                <h1 style ="color:black;text-align:center;">i-Capitale App</h1> 
                </div> 
                """
    st.markdown(html_temp, unsafe_allow_html=True)
    st.write(" ##### by PandaEyes")

    left_col, center_col, right_col = st.columns(3)
    with center_col:
        lottie_hello = load_lottieurl("https://assets4.lottiefiles.com/packages/lf20_gxtah1wp.json")
        st_lottie(
            lottie_hello,
            speed=1,
            reverse=False,
            loop=True,
            quality="medium",  # medium ; high
            height=750,
            width=750,
            key=None,
        )


    st.write("\n")
    st.write("\n")
    st.write("\n")
    st.write("\n")


    left_col,right_col = st.columns(2)

    with left_col:
        st.header("How it works?")
        st.image(
            "https://miro.medium.com/max/1400/1*Eg-kn38i5jR3g6UZy2vmXw.jpeg"
        )
    with right_col:
        st.text("\n")
        st.text("\n")
        st.text("\n")

        st.write("#### Predicting Stock Market Trends")
        st.write("The nature of stock market movement has always been ambiguous for investor because of"
                " various influential factors. Here, ***i-Capitale*** aims to significantly reduce the risk of trend"
                " prediction with machine learning algorithms.")

    st.text("\n")
    st.text("\n")
    st.text("\n")
    st.text("\n")
    st.text("\n")
    st.text("\n")
    st.text("\n")
    st.text("\n")


    st.header("Why use i-Capitale?")

    left_col, center_col, right_col = st.columns(3)
    with left_col:
        # front end elements of the web page
        html_temp = """ 
               <div style ="background-color:#ecdd9c; height:150px; padding:13px"> 
               <p style ="color:black;text-align:center;">The best App for forecasting the chaotic stock market movement in the future</p> 
               </div> 
               """

        # display the front end aspect
        st.markdown(html_temp, unsafe_allow_html=True)
        lottie_hello1 = load_lottieurl("https://assets4.lottiefiles.com/packages/lf20_73dJ0v.json")
        st_lottie(
            lottie_hello1,
            speed=1,
            reverse=False,
            loop=True,
            quality="low",  # medium ; high
            height=400,
            width=400,
            key=None,
        )


    with center_col:
        # front end elements of the web page
        html_temp = """ 
               <div style ="background-color:#ecdd9c ; height:150px; padding:13px"> 
               <p style ="color:black;text-align:center;">Accelerate the process of decision making in stock trading strategy</p> 
               </div> 
               """

        # display the front end aspect
        st.markdown(html_temp, unsafe_allow_html=True)
        lottie_hello2 = load_lottieurl("https://assets4.lottiefiles.com/packages/lf20_maea5tig.json")
        st_lottie(
            lottie_hello2,
            speed=1,
            reverse=False,
            loop=True,
            quality="low",  # medium ; high
            height=400,
            width=400,
            key=None,
        )

    with right_col:
        # front end elements of the web page
        html_temp = """ 
               <div style ="background-color:#ecdd9c; height:150px; padding:13px"> 
               <p style ="color:black;text-align:center;">Beginner-friendly</p> 
               </div> 
               """

        # display the front end aspect
        st.markdown(html_temp, unsafe_allow_html=True)

        lottie_hello3 = load_lottieurl("https://assets4.lottiefiles.com/packages/lf20_wX1chG.json")
        st_lottie(
            lottie_hello3,
            speed=1,
            reverse=False,
            loop=True,
            quality="low",  # medium ; high
            height=400,
            width=400,
            key=None,
        )

    st.text("\n")
    st.text("\n")
    st.text("\n")
    st.text("\n")
    st.text("\n")
    st.text("\n")
    st.text("\n")
    st.text("\n")

    st.header("FAQ About i-Capitale")

    with st.expander("⚙️How to use i-Capitale?", expanded=False):
        st.write(
            """    
            1. Go to Menu sidebar
            2. Click 'Prediction Results' button.
            3. Select one of the 22 companies you desired to visualize.
            4. You are able to get visualizations to evaluate its performance for further insights now!
            """
        )

    with st.expander("⚙️Why i-Capitale is our primary choice?", expanded=False):
        st.write(
            """    
            Our model discovers the future value of company stock with an average accuracy of above 80%.
            """
        )

    with st.expander("⚙️What is the main purpose of i-Capitale?", expanded=False):
        st.write(
            """    
            To predict the daily closing prices of 22 selected stocks for the next 90 days starting 1 Jan 2022 to help the investors in proper decision-making.
            """
        )





def OurModel():
    left_col, right_col = st.columns(2)
    with left_col:
        lottie_hello = load_lottieurl("https://assets2.lottiefiles.com/packages/lf20_nzco8tvf.json")
        st_lottie(
            lottie_hello,
            speed=1,
            reverse=False,
            loop=True,
            quality="medium",  # medium ; high
            height=750,
            width=750,
            key=None,
        )

    with right_col:
        st.write("\n")
        st.write("\n")
        st.write("\n")
        st.write("\n")
        st.write("\n")
        st.write("\n")
        st.write("\n")
        st.write("\n")
        st.write("\n")
        st.write("\n")
        st.write("\n")
        st.write("\n")
        st.write("\n")
        st.write("\n")
        st.write("\n")
        st.write("\n")
        st.title("Long Short Term Memory")
        st.title("(LSTM) model")

    st.write("\n")
    st.write("\n")
    st.write("##### There are *4* technical indicators used in technical analysis:")
    """ 
    * Exponential Moving Average(EMA)
    * Moving Average Convergence Divergence(MACD)
    * Volume Oscillator
    * Relative Strength Index(RSI) 
    """
    st.write("\n")
    st.write("\n")

    st.subheader("Highlight Of i-Capitale")
    st.write("#### Highlight 1: ")
    st.write("Our model is extended to analyze unstructured textual information from Twitter and classify the polarity of a given text "
            "at the sentence level or class level, whether it reflects a positive, negative, or neutral. ")
    st.write("#### Highlight 2: ")
    st.write("Our model predict well for sudden changes in the trend of stock data. "
            "For instance, external factors and real-world changes such as ***Financial Crisis*** and ***COVID 19 Pandemic***.")

    st.text("\n")
    st.text("\n")
    st.text("\n")
    st.text("\n")

    # front end elements of the web page
    html_temp = """ 
                    <div style ="background-color:#ecdd9c;padding:13px"> 
                    <h2 style ="color:black;text-align:left;">Data Visualization</h2> 
                    </div> 
                    """

    # display the front end aspect
    st.markdown(html_temp, unsafe_allow_html=True)
    st.text("\n")
    st.text("\n")

    option = st.selectbox(
        'Please select a company: ',
        ('-','AHEALTH', 'APM', 'BIOHLDG','BSTEAD', 'CAPITALA', 'EUPE','HPMT', 'ICAP', 'KGB',
         'KRONO', 'LUXCHEM', 'MKH','OCK', 'OCNCASH', 'PADINI','PARKSON', 'SALUTE', 'SAM','SURIA', 'TONGHER',
         'UTDPLT', 'WELLCAL'))

    st.write('You selected: ', option)

    st.text("\n")
    st.text("\n")
    st.text("\n")
    st.text("\n")

    if(option!='-'):
        st.subheader("Volume vs Stock movement")
        st.image(
            "https://images.moneycontrol.com/static-mcnews/2018/01/BSE_Sensex_Budget_2017_volatile1.jpg?impolicy=website&width=770&height=431",
            width=600,  # Manually Adjust the width of the image as per requirement
        )
        st.text("\n")
        st.subheader("Open Price vs Stock movement")
        st.image(
            "https://images.moneycontrol.com/static-mcnews/2018/01/BSE_Sensex_Budget_2017_volatile1.jpg?impolicy=website&width=770&height=431",
            width=600,  # Manually Adjust the width of the image as per requirement
        )
        st.text("\n")
        st.subheader("Close Price vs Stock movement")
        st.image(
            "https://images.moneycontrol.com/static-mcnews/2018/01/BSE_Sensex_Budget_2017_volatile1.jpg?impolicy=website&width=770&height=431",
            width=600,  # Manually Adjust the width of the image as per requirement
        )
        st.markdown("\n")
        st.subheader("Confusion Matrix")
        st.write("##### Training")
        st.image(
            "https://images.moneycontrol.com/static-mcnews/2018/01/BSE_Sensex_Budget_2017_volatile1.jpg?impolicy=website&width=770&height=431",
            width=600,  # Manually Adjust the width of the image as per requirement
        )
        st.text("\n")
        st.text("\n")
        st.write("##### Validation")
        st.image(
            "https://images.moneycontrol.com/static-mcnews/2018/01/BSE_Sensex_Budget_2017_volatile1.jpg?impolicy=website&width=770&height=431",
            width=600,  # Manually Adjust the width of the image as per requirement
        )
        st.text("\n")
        st.text("\n")
        st.write("##### Testing")
        st.image(
            "https://images.moneycontrol.com/static-mcnews/2018/01/BSE_Sensex_Budget_2017_volatile1.jpg?impolicy=website&width=770&height=431",
            width=600,  # Manually Adjust the width of the image as per requirement
        )
        st.text("\n")
        st.text("\n")
    else:
        st.info('Hey! HERE for you to choose a company to have a better data visualization.')



def Results():
    left_col, right_col = st.columns(2)
    with left_col:
        lottie_hello = load_lottieurl("https://assets2.lottiefiles.com/private_files/lf30_ps1145pz.json")
        st_lottie(
            lottie_hello,
            speed=1,
            reverse=False,
            loop=True,
            quality="medium",  # medium ; high
            height=750,
            width=750,
            key=None,
        )

    with right_col:
        st.write("\n")
        st.write("\n")
        st.write("\n")
        st.write("\n")
        st.write("\n")
        st.write("\n")
        st.write("\n")
        st.write("\n")
        st.write("\n")
        st.write("\n")
        st.write("\n")
        st.write("\n")
        st.write("\n")
        st.write("\n")
        st.write("\n")
        st.write("\n")
        st.title("Stock Prediction")

    st.markdown(
        '<div style="text-align: justify;">Daily closing prices of 22 selected stocks for the next 90 days are predicted.</div>',
        unsafe_allow_html=True)
    st.text("\n")

    # https://towardsdatascience.com/how-to-get-stock-data-using-python-c0de1df17e75
    # define the ticker symbol
    tickerSymbol = 'GOOGL'
    # get data on this ticker
    tickerData = yf.Ticker(tickerSymbol)
    # get the historical prices for this ticker
    tickerDf = tickerData.history(period='1d', start='2010-5-31', end='2020-5-31')
    # Open	High	Low	Close	Volume	Dividends	Stock Splits

    st.text("\n")
    st.text("\n")
    st.text("\n")

    option = st.selectbox(
        'Please select a company: ',
        ('-', 'AHEALTH', 'APM', 'BIOHLDG', 'BSTEAD', 'CAPITALA', 'EUPE', 'HPMT', 'ICAP', 'KGB',
         'KRONO', 'LUXCHEM', 'MKH', 'OCK', 'OCNCASH', 'PADINI', 'PARKSON', 'SALUTE', 'SAM', 'SURIA', 'TONGHER',
         'UTDPLT', 'WELLCAL'))

    st.write('You selected: ', option)

    st.text("\n")
    st.text("\n")
    st.text("\n")
    st.text("\n")

    if (option != '-'):
        st.write("""
                   ## Closing Price 					
                   """)
        st.line_chart(tickerDf.Close)
    else:
        st.info('Hey! HERE for you to visualize the closing price of your selected company.')

    st.write("\n")
    st.write("\n")
    st.write("\n")
    st.write("\n")
    st.write("\n")
    st.write("\n")
    st.write("\n")
    st.write("\n")

    st.subheader("Future Prediction(Closing Price)")
    st.text_input("Date/Month/Year")
    if st.button("Predict"):
        st.write("Closing Price: RM111")




def Consultants():
    left_col, right_col = st.columns(2)
    with left_col:
        lottie_hello = load_lottieurl("https://assets5.lottiefiles.com/packages/lf20_djwnoxew.json")
        st_lottie(
            lottie_hello,
            speed=1,
            reverse=False,
            loop=True,
            quality="medium",  # medium ; high
            height=750,
            width=750,
            key=None,
        )

    with right_col:
        st.write("\n")
        st.write("\n")
        st.write("\n")
        st.write("\n")
        st.write("\n")
        st.write("\n")
        st.write("\n")
        st.write("\n")
        st.write("\n")
        st.write("\n")
        st.write("\n")
        st.write("\n")
        st.write("\n")
        st.write("\n")
        st.write("\n")
        st.write("\n")
        st.title("Professor Consultants")

    st.text("\n")

    st.write("##### Our professor consultant teams from i-Capitale are here to guide you now!")
    st.write("Consultant Cost per hour: **RM200** ")
    st.write("Help your company to earn at least RM10000 in **ONE** month!")
    st.write("Don't miss this opportunity!")

    st.image(
        "https://images.assetsdelivery.com/compings_v2/terrry4/terrry42001/terrry4200100119.jpg",
        width=500,  # Manually Adjust the width of the image as per requirement
    )

    st.text("\n")
    st.text("\n")
    st.info("All information during consultation are strictly confidential.")



def AboutUs():
    left_col, right_col = st.columns(2)
    with left_col:
        lottie_hello = load_lottieurl("https://assets2.lottiefiles.com/packages/lf20_qct0ydor.json")
        st_lottie(
            lottie_hello,
            speed=1,
            reverse=False,
            loop=True,
            quality="medium",  # medium ; high
            height=700,
            width=700,
            key=None,
        )

    with right_col:
        st.write("\n")
        st.write("\n")
        st.write("\n")
        st.write("\n")
        st.write("\n")
        st.write("\n")
        st.write("\n")
        st.write("\n")
        st.write("\n")
        st.write("\n")
        st.write("\n")
        st.write("\n")
        st.write("\n")
        st.write("\n")
        st.write("\n")
        st.write("\n")
        st.title("Introduction to our team")

    st.title("")
    st.text("\n")
    st.text("\n")

    st.write("#### We are a team of freshmen from **University Of Malaya**. ")
    st.write("##### Team Member : ")
    st.write("Leader : Regina Tang Heu Yan")
    st.write("Member : Tan Jia Xuan ")
    st.write("Member : Ong Shu Ying ")
    st.write("Member : Ham Zhi Ying ")
    st.write("Member : Tan Wei Ling")

    st.text("\n")
    st.text("\n")

    st.write("###### Connect with us")
    st.write("013-3333333")

    st.text("\n")
    st.text("\n")
    st.text("\n")
    st.text("\n")
    st.text("\n")
    st.text("\n")
    st.text("\n")
    st.text("\n")

    feedback = st.slider('How much would you rate this app?', min_value=0, max_value=5, step=1)

    if feedback:
        st.header("Thank you for rating the app!")




with st.sidebar:
    st.title("i-Capitale App")
    selected=option_menu(
        menu_title="Menu",
        options=["Home Page","Our Model", "Prediction Results", "Consultants","About Us"],
        icons=["house","wrench","clipboard-check","journal-medical","info-circle"],
        menu_icon="bookmark-star",
        default_index=0,
    )

if selected == "Home Page":
    MainPage()

elif selected == "Our Model":
    OurModel()

elif selected == "Prediction Results":
    Results()

elif selected == "Consultants":
    Consultants()

elif selected == "About Us":
    AboutUs()
