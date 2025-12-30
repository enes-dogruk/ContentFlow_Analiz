import streamlit as st
import joblib
import pandas as pd

# Modeli yükle
model = joblib.load('contentflow_churn_model.pkl')

st.title("🚀 ContentFlow AI - Müşteri Kayıp (Churn) Tahmini")
st.write("Müşteri bilgilerini girerek sistemden ayrılma riskini analiz edin.")

# Kullanıcı Girişleri
st.sidebar.header("Müşteri Parametreleri")
paket = st.sidebar.selectbox("Paket Tipi", ["Başlangıç", "Profesyonel", "Sınırsız"])
icerik_sayisi = st.sidebar.slider("Aylık İçerik Sayısı", 0, 100, 20)
gelir = st.sidebar.number_input("Aylık Gelir (TL)", value=1500)
memnuniyet = st.sidebar.slider("Müşteri Memnuniyeti (1-10)", 1, 10, 5)

# Paket verisini modele uygun sayısal değere çevir
paket_map = {"Başlangıç": 0, "Profesyonel": 1, "Sınırsız": 2}
api_maliyeti = icerik_sayisi * 3.5 # Önceki mantığımız
brut_kar = gelir - api_maliyeti

# Tahmin için veri çerçevesi (Modelin beklediği sütun sırasıyla aynı olmalı!)
input_data = pd.DataFrame([[icerik_sayisi, gelir, memnuniyet, api_maliyeti, brut_kar, paket_map[paket]]], 
                         columns=['Aylık_İçerik_Sayısı', 'Aylık_Gelir_TL', 'Müşteri_Memnuniyeti_Skoru', 
                                  'Tahmini_API_Maliyeti_TL', 'Brüt_Kar_TL', 'Paket_Sira'])

if st.button("Risk Analizi Yap"):
    prediction = model.predict(input_data)
    probability = model.predict_proba(input_data)[0][1] # Churn olma ihtimali
    
    if prediction[0] == 1:
        st.error(f"⚠️ KRİTİK RİSK: Bu müşteri %{probability*100:.2f} ihtimalle ayrılacak!")
        st.write("Öneri: Hemen özel bir indirim tanımlayın veya müşteriyle iletişime geçin.")
    else:
        st.success(f"✅ GÜVENLİ: Bu müşteri sadık görünüyor. (Ayrılma riski: %{probability*100:.2f})")