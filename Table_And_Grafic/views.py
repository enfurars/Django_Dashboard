from django.shortcuts import render
from .models import User, Simulation
import pandas as pd
import matplotlib.pyplot as plt
import os
from datetime import datetime, timedelta
from django.db.models import Count  

def index(request):
    # Şirketlerin toplam kullanıcı sayısını hesaplama
    company_user_counts = User.objects.values('simulation__company_name').annotate(total_users=Count('user_id')).order_by('simulation__company_name')

    # Kullanıcı sayısının günlük gelişimini hesaplama
    users = User.objects.all().values('signup_datetime')
    df = pd.DataFrame(users)
    df['signup_date'] = pd.to_datetime('1899-12-30') + pd.to_timedelta(df['signup_datetime'], 'D')
    daily_user_counts = df.groupby(df['signup_date'].dt.date).size().reset_index(name='new_users')
    daily_user_counts['cumulative_users'] = daily_user_counts['new_users'].cumsum()

    # Günlük gelişim grafiği oluşturma
    plt.figure(figsize=(10, 6))
    plt.plot(daily_user_counts['signup_date'], daily_user_counts['cumulative_users'], marker='o')
    plt.title('Ludi\'deki Toplam Kullanıcı Sayısının Günlük Gelişimi')
    plt.xlabel('Tarih')
    plt.ylabel('Toplam Kullanıcı Sayısı')
    plt.grid(True)
    plt.xticks(rotation=45)
    plt.tight_layout()
    if not os.path.exists('Table_And_Grafic/static'):
        os.makedirs('Table_And_Grafic/static')
    plt.savefig('Table_And_Grafic/static/Table_And_Grafic/daily_user_growth.png')

    context = {
        'company_user_counts': company_user_counts,
    }
    return render(request, 'Table_And_Grafic/index.html', context)