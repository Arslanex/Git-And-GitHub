import streamlit as st

st.title("Git ve GitHub Terimleri Açıklama Uygulaması")
st.write("Bu uygulama, Git ve GitHub terimlerini açıklamak için tasarlanmıştır.")

term_list = [
        {"term": "Git", "description": "Dağıtık bir versiyon kontrol sistemi."},
        {"term": "Repository (Depo)", "description": "Projedeki dosyaların ve geçmişin saklandığı yer."},
        {"term": "Commit", "description": "Dosya değişikliklerinin git reposuna kaydedildiği işlem."},
        {"term": "Branch (Dal)", "description": "Projedeki ana kaynaktan türetilen ayrı bir çalışma alanı."},
        {"term": "Merge", "description": "Farklı dallardaki değişikliklerin birleştirildiği işlem."},
        {"term": "Pull Request", "description": "Değişikliklerin ana dala birleştirilmesi için yapılan bir istek."},
        {"term": "Clone", "description": "Uzak repo kaynağının yerel makineye kopyalanması."},
        {"term": "Fork", "description": "Bir projenin tam bir kopyasını kullanıcının GitHub hesabına taşıma işlemi."},
        {"term": "Pull", "description": "Uzak repo kaynağını yerel makineye güncelleme işlemi."}
    ]

selected_term = st.selectbox("Bir terim seçin:", [term["term"] for term in term_list])

for term in term_list:
    if term["term"] == selected_term:
        st.subheader(term["term"])
        st.write(term["description"])