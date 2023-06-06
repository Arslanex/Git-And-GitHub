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

st.title("Hello There")
st.markdown("""
Hoşgeldiniz! 
Evet, Git ve GitHub ile ilgileniyorum ve internette araştırma yaparken bu siteye rastladınız. Bu site, 
kişisel çalışma ve notlarımı kullanarak Git ve GitHub'ı yeni başlayan kişiler için kolay bir başlangıç noktası 
oluşturmak amacıyla hazırlandı.

Git, dağıtık bir sürüm kontrol sistemidir. Yazılım geliştirme sürecinde dosyaların takibini sağlar, değişiklikleri 
kaydeder ve farklı sürümler arasında geçiş yapmayı kolaylaştırır. Git, projelerinizi takip etmek, farklı dallarda 
çalışmak ve değişiklikleri birleştirmek gibi birçok özelliği sunar. Ayrıca, yerel olarak çalışır, yani internet 
bağlantısı olmadan da kullanılabilir.

GitHub ise Git tabanlı bir kod barındırma ve işbirliği platformudur. Projelerinizi Git kullanarak GitHub'a yükleyebilir, 
takip edebilir ve paylaşabilirsiniz. GitHub, geliştiricilerin birlikte çalışmasını kolaylaştıran bir dizi işbirliği 
özelliği sunar. Projenizin bir kopyasını indirebilir, geri bildirim sağlayabilir, hataları rapor edebilir ve projeye 
katkıda bulunabilirsiniz.

Sayfanın sağ tarafında, öğrenme sırasına göre düzenlenmiş sayfalar bulunmaktadır. Bu sayfalar arasında hızlı ve kolay 
bir şekilde gezinebilirsiniz. Herhangi bir sorunla karşılaşırsanız, sağ üst köşedeki menüden benimle iletişime geçebilir 
veya GitHub üzerinde sorun bildirebilirsiniz.

Umarım bu kaynak, Git ve GitHub'ı öğrenmek isteyenlere yardımcı olur! Eğer başka sorularınız varsa sormaktan çekinmeyin.
""")
