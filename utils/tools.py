def check_pvalue_list(pv_list, pvalue=0.05):
    for pv in pv_list:
        if pv < pvalue:
            text = '''На основе полученных уровеней значимости можно :red[отвергнуть] Нулевую гипотезу'''
            status = ''':green[Принимается]'''
            return text, status
    text = '''При данных уровнях значимости Нулевая гипотеза :green[не отвергается]'''
    status = ''':red[Отвергнута]'''
    return text, status


def check_pvalue(pv, pvalue=0.05):
    if pv < pvalue:
        return ''' - :red[Не принимается]'''
    return ''' - :green[Принимается]'''


def corr_check(corr):
    if 0.81 <= corr:
        return ''' :green[Очень высокая связь]'''
    elif 0.61 <= corr and corr >= 0.8:
        return ''' :green[Высокая связь]'''
    elif 0.41 <= corr and corr >= 0.6:
        return ''' [Средняя связь]'''
    elif 0.21 <= corr and corr >= 0.4:
        return ''' :red[Слабая связь]'''
    elif 0.20 > corr:
        return ''' :red[Очеень слабая связь]'''
