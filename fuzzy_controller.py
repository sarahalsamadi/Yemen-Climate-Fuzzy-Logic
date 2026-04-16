import numpy as np

# دوال الانتماء لمناطق اليمن
# المناطق الجبلية

def cold_membership_mountain(temp):
    if temp <= 10:
        return 1.0  # بارد جداً
    elif 10 < temp <= 15:
        return (15 - temp) / 5.0  # أقل برودة
    else:
        return 0.0  # غير بارد

def comfortable_membership_mountain(temp):
    if 15 < temp <= 20:
        return (temp - 15) / 5.0  # أكثر راحة
    elif 20 < temp <= 25:
        return (25 - temp) / 5.0  # أقل راحة
    else:
        return 0.0  # غير مريح

def hot_membership_mountain(temp):
    if temp > 25:
        return (temp - 25) / 0.5  # أكثر سخونة
    else:
        return 0.0  # غير ساخن

# المناطق الساحلية والصحراوية

def cold_membership_coastal_desert(temp):
    if temp <= 20:
        return 1.0  # بارد جداً
    elif 20 < temp <= 24:
        return (24 - temp) / 4.0  # أقل برودة
    else:
        return 0.0  # غير بارد

def comfortable_membership_coastal_desert(temp):
    if 20 < temp <= 26:
        return (temp - 20) / 6.0  # أكثر راحة
    elif 26 < temp <= 30:
        return (30 - temp) / 4.0  # أقل راحة
    else:
        return 0.0  # غير مريح

def hot_membership_coastal_desert(temp):
    if temp > 30:
        return (temp - 30) / 0.5  # أكثر سخونة
    else:
        return 0.0  # غير ساخن

# دوال الانتماء لمستويات التدفئة

def low_heating(membership):
    return membership * 20  # تدفئة منخفضة

def medium_heating(membership):
    return membership * 50  # تدفئة متوسطة

def high_heating(membership):
    return membership * 100  # تدفئة عالية

# تطبيق القواعد الضبابية

def fuzzy_inference(temp, region):
    if region == 'mountain':
        cold = cold_membership_mountain(temp)
        comfortable = comfortable_membership_mountain(temp)
        hot = hot_membership_mountain(temp)
    elif region == 'coastal_desert':
        cold = cold_membership_coastal_desert(temp)
        comfortable = comfortable_membership_coastal_desert(temp)
        hot = hot_membership_coastal_desert(temp)
    else:
        raise ValueError("المنطقة غير معروفة. استخدم 'mountain' أو 'coastal_desert'.")

    # تطبيق القواعد
    heating_low = low_heating(hot)
    heating_medium = medium_heating(comfortable)
    heating_high = high_heating(cold)

    # دمج النتائج
    total_membership = cold + comfortable + hot
    if total_membership == 0:
        return 0

    # حساب مستوى التدفئة
    heating = (heating_low + heating_medium + heating_high) / total_membership
    return heating

# إدخال الدرجة من المستخدم

def main():
    try:
        room_temperature = float(input('ادخل درجة حرارة الغرفة: '))
        region = input('ادخل المنطقة (mountain/coastal_desert): ').strip().lower()
    except ValueError:
        print('الرجاء إدخال رقم صحيح.')
        return

    # حساب مستوى التدفئة باستخدام المنطق الضبابي
    heating_level = fuzzy_inference(room_temperature, region)

    # طباعة النتيجة
    print(f'مستوى التدفئة المطلوب هو {heating_level:.2f}%')

if __name__ == '__main__':
    main()
