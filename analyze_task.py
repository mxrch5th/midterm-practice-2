# 파일명: analyze_task.py
import pandas as pd
import matplotlib.pyplot as plt

def show_chart():
    # 데이터 생성
    data = {'Subject': ['Math', 'Eng', 'Sci'], 'Score': [90, 85, 95]}
    df = pd.DataFrame(data) # <--- 오류 1
    
    # 그래프 그리기
    plt.bar(df['Subject'], df['Score'])
    plt.title('My Grades')
    plt.show()

if __name__ == "__main__":
    show_chart()