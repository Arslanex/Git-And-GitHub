import streamlit as st

st.set_page_config(
    page_title="Git&GitHub",
    page_icon=":smile:",
    initial_sidebar_state="expanded",
    menu_items={
        'Get Help': 'https://www.linkedin.com/in/enes-arslan-/',
        'Report a bug': "https://github.com/Arslanex",
        'About': "Who knows"
    }
)
with st.sidebar:
    st.title("Ana Sayfa")

st.title("Hoş Geldiniz! Git'e Adım Atın: Temel Git Eğitimi")
st.markdown("""
Merhaba! Git, modern yazılım geliştirme süreçlerinin vazgeçilmez bir parçası haline gelmiş güçlü bir versiyon kontrol 
sistemi ve kaynak kod yönetim aracıdır. Eğer yazılım geliştirmeye ilgi duyuyorsanız veya zaten bir geliştiriciyseniz, 
Git'i öğrenmek sizin için önemli bir adımdır.

Bu web sitesi, Git'in temellerini öğrenmek ve başlamak için ihtiyaç duyduğunuz bilgilere erişmenizi sağlamak için 
tasarlanmıştır. Git hakkında hiçbir bilginiz olmasa bile endişelenmeyin! Adım adım ilerleyerek Git'in nasıl çalıştığını, 
temel kavramları ve en sık kullanılan komutları öğreneceksiniz.

**Git Eğitimi İçeriği :**
- Git Temel Kavramları: Git'in temel kavramlarını anlamak, repository (depolar), commit (kayıt), branch (dallar) gibi 
terimlerin ne anlama geldiğini öğrenmek için bu bölümü inceleyin.
- Temel Git Komutları: Git'in en sık kullanılan komutlarını öğrenmek için bu sayfaya göz atın. Add (ekle), commit (kaydet), 
push (yükle), pull (çek) ve clone (kopyala) gibi temel komutları adım adım öğreneceksiniz.
- Git Sözlüğü: Git'in terimler ve kısaltmalarla dolu dünyasında kaybolmayın. Bu sayfada Git sözlüğünde sıkça kullanılan 
terimlerin açıklamalarını bulabilirsiniz.
Bu web sitesi, interaktif bir şekilde öğrenmeyi sağlayan kullanıcı dostu bir arayüzle size rehberlik edecek. Her konu 
için açıklamalar, örnekler ve pratik alıştırmalar bulunacak. Ayrıca, Git hakkında daha fazla kaynak ve referanslar için 
kullanabileceğiniz bağlantılar da sunulacak.
- Takım Çalışması ve Git: Git'in takım çalışması süreçlerinde nasıl kullanıldığını öğrenmek için bu sayfayı ziyaret edin. 
Branch (dal), merge (birleştir) ve conflict (çakışma) gibi kavramları keşfedin.

**Hazır mısınız?**

O zaman, Git dünyasına adım atmak için hemen başlayalım! Sizi temel Git eğitimimize yönlendirmek için aşağıdaki "Başla" 
düğmesine tıklayın ve Git'in gücünü keşfetmeye başlayın.

Başla
""")
