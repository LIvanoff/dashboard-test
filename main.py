import streamlit as st
import scipy.stats as sts
from scipy.stats import ttest_ind
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import plotly.express as px

from utils.preproccesing import load_data
from utils.tools import check_pvalue_list, check_pvalue, corr_check

DATA_PATH = './data/data.csv'

# if __name__ == '__main__':

st.set_page_config(layout="wide")

row0_spacer1, row0_1, row0_spacer2, row0_2, row0_spacer3 = st.columns((.1, 2.3, .1, 1.3, .1))
with row0_1:
    st.title("Тестовое задание")
with row0_2:
    st.text("")
    st.subheader('[Ivanov Leonid](https://github.com/LIvanoff/)')

st.sidebar.title("Загрузка данных")

uploaded_file = st.sidebar.file_uploader("Выбери файл CSV", accept_multiple_files=False)

if uploaded_file is not None:
    dataframe = load_data(uploaded_file)
else:
    dataframe = load_data(DATA_PATH)

work_days = st.sidebar.select_slider(
    'Выберите число пропусков рабочих дней',
    options=sorted(dataframe.work_days.unique()))

age = st.sidebar.select_slider(
    'Выберите возраст',
    options=sorted(dataframe.age.unique()))
hypot = dataframe[dataframe.work_days > work_days]

# графики статистик признаков
col0_0, col0_1 = st.columns([3, 1])
col0_0.subheader("Графики статистик по признакам")
fig, ax = plt.subplots(1, 3, figsize=(6, 2))
ax[0].set_title("Пропуски рабочих дней", fontsize=6)
ax[0].hist(hypot.work_days)
ax[1].set_title("Возраст", fontsize=6)
ax[1].hist(hypot.age)
ax[2].set_title("Пол", fontsize=6)
ax[2].pie(list(hypot.sex.value_counts()), explode=(0, 0.1), labels=['Мужчины', 'Женщины'], autopct='%1.1f%%', shadow=True, startangle=90,
       textprops={'fontsize': 5})
col0_0.pyplot(fig, use_container_width=False)

# отрисовка датафрейма
col0_1.subheader(f"Датафрейм")
col0_1.write(hypot)

tab1, tab2 = st.tabs(["Гипотеза 1", "Гипотеза 2"])

#отрисовка вкладки с Гипотезой 1
with tab1:
    male = hypot.work_days[hypot['sex'] == 1]
    female = hypot.work_days[hypot['sex'] == 0]
    _, pvalue_var = sts.f_oneway(male, female)
    stat, pvalue_mean = ttest_ind(male, female)
    corr_matrix = hypot.corr()
    try:
        corr = corr_matrix.work_days.sex
    except:
        corr = 0

    msg, status = check_pvalue_list([pvalue_var, pvalue_mean])

    st.header("Гипотеза 1: " + status)

    st.markdown(
        "*Мужчины пропускают в течение года более 2 рабочих дней (work_days) по болезни значимо чаще женщиню*")
    st.markdown(
        f"t-критерий Стьюдента: уровень значимости при сравнении Средних равен {pvalue_mean}" + check_pvalue(
            pvalue_mean))
    st.markdown(
        f"Дисперсионный анализ (Anova): уровень значимости при сравнении Дисперсий равен {pvalue_var}" + check_pvalue(
            pvalue_var))
    st.markdown(f"Коэффициент корреляции: корреялция между work_days и sex равна {corr}"+corr_check(corr))
    st.markdown(msg)
    st.divider()

    col1_0, col1_1 = st.columns(2)
    fig, ax = plt.subplots(figsize=(2, 2))
    ax.imshow(corr_matrix)
    ax.set_xticks(np.arange(len(corr_matrix.columns)), labels=corr_matrix.columns, fontsize=5)
    ax.set_yticks(np.arange(len(corr_matrix.columns)), labels=corr_matrix.columns, fontsize=5)
    plt.setp(ax.get_xticklabels(), rotation=45, ha="right",
             rotation_mode="anchor", fontsize=5)
    for i in range(len(corr_matrix.columns)):
        for j in range(len(corr_matrix.columns)):
            text = ax.text(j, i, round(corr_matrix.values[i, j], 2),
                           ha="center", va="center", color="w", fontsize=5)

    col1_0.subheader(f"Матрица корреляций")
    col1_0.pyplot(fig, use_container_width=False)

    col1_1.subheader(f"Гистограмма пропущенных дней")
    fig = px.histogram(hypot,
                 x='work_days',
                 color='sex',
                 barmode='group',
                 text_auto=True
                 )
    col1_1.plotly_chart(fig, theme="streamlit", use_container_width=True)

#отрисовка вкладки с Гипотезой 2
with tab2:
    old = hypot[hypot['age'] > age]
    young = hypot[hypot['age'] <= age]
    _, pvalue_var = sts.f_oneway(old.work_days, young.work_days)
    _, pvalue_mean = ttest_ind(old.work_days, young.work_days)
    msg, status = check_pvalue_list([pvalue_var, pvalue_mean])

    st.header("Гипотеза 2: " + status)

    st.markdown(
        "*Работники старше 35 лет (age) пропускают в течение года более 2 рабочих дней (work_days) по болезни значимо чаще своих более молодых коллег.*")
    st.markdown(f"t-критерий Стьюдента: уровень значимости при сравнении Средних: {pvalue_mean}" + check_pvalue(
        pvalue_mean))
    st.markdown(
        f"Дисперсионный анализ (Anova): уровень значимости при сравнении Дисперсий: {pvalue_var}" + check_pvalue(
            pvalue_var))
    st.markdown(msg)
    st.divider()

    fig, ax = plt.subplots(2, 2, figsize=(6, 4))

    scatter = ax[0, 0].scatter(x=young['work_days'], y=young['age'], c=list(young['sex']))
    ax[0, 0].legend(*scatter.legend_elements(), loc='upper right', bbox_to_anchor=(2.7, 1))
    ax[0, 0].set_xticks(old['work_days'])
    ax[0, 0].set_ylabel('Возраст, лет', fontsize=5)
    ax[0, 0].set_title(f"Выборка до {age} лет включительно", fontsize=8)
    ax[1, 0].set_xlabel('Пропуски рабочих дней, дни', fontsize=5)
    ax[0, 1].scatter(x=old['work_days'], y=old['age'], c=list(old['sex']))
    ax[0, 1].set_title(f"Выборка после {age} лет", fontsize=8)
    ax[1, 1].set_xlabel('Пропуски рабочих дней, дни', fontsize=6)

    ax[1, 0].hist(young.work_days)
    ax[1, 1].hist(old.work_days)

    st.pyplot(fig, use_container_width=False)
