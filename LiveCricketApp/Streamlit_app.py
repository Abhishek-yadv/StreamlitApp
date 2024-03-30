import streamlit as st
import time
from urllib.request import Request, urlopen
from bs4 import BeautifulSoup
from plyer import notification
URL = 'http://www.cricbuzz.com/cricket-match/live-scores'
def notify(title, score):
    # Truncate the title and message if they exceed the maximum length
    max_title_length = 64
    max_message_length = 128
    truncated_title = title[:max_title_length]
    truncated_message = score[:max_message_length]

# streamlit run d:\PythonProject\Day1\1DAY\Streamlit_app.py

    notification.notify(
        title=truncated_title,
        message=truncated_message,
        app_name="Cricket Live Scores",  # Optional app name
        timeout=30,  # Duration in seconds
    )
def fetch_live_scores():
    try:
        request = Request(URL, headers={'User-Agent': 'XYZ/3.0'})
        response = urlopen(request, timeout=20).read()
        data_content = response
        soup = BeautifulSoup(data_content, 'html.parser')        
        scores = []
        for score in soup.find_all('div', attrs={'class': 'cb-col cb-col-100 cb-plyr-tbody cb-rank-hdr cb-lv-main'}):
            header = score.find('div', attrs={'class': 'cb-col-100 cb-col cb-schdl'})
            header = header.text.strip()
            status = score.find('div', attrs={'class': 'cb-scr-wll-chvrn cb-lv-scrs-col'})
            s = status.text.strip()
            scores.append((header, s))
        
        return scores
    except Exception as e:
        print("An error occurred:", e)
        return []

def main():
    st.title("Live Cricket Scores")    
    while True:
        scores = fetch_live_scores()        
        if scores:
            for header, score in scores:
                notify(header, score)
                
                st.write(f"**{header}**: {score}")
                
        time.sleep(10)

if __name__ == "__main__":
    main()
    


