

def check_pvalue_list(pv_list, pvalue=0.05):
    for pv in pv_list:
        if pv < pvalue:
            text = '''На основе полученных уровеней значимости можно :red[отвергнуть] основную Нулевую гипотезу'''
            status = ''':red[Отвергнута]'''
            return text, status
    text = '''При данных уровнях значимости Нулевая гипотеза :green[не отвергается]'''
    status = ''':green[Не отвергнута]'''
    return text, status

def check_pvalue(pv, pvalue=0.05):
    if pv < pvalue:
        return ''' - :red[Не принимается]'''
    return ''' - :green[Принимается]'''

# def corr_check(corr):
#     if 0.81 <= corr >= 1:
#         return "Сильная "